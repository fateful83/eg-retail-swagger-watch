#!/usr/bin/env python3
"""
EG Retail Swagger History Page Generator

Builds a browsable history page from snapshots created by
`eg_retail_swagger_watch_agent.py`.

What it generates
- .swagger_watch_state/history.html

What it shows
- all services/environments with saved snapshots
- earliest snapshot timestamp
- latest snapshot timestamp
- snapshot count
- quick compare links for:
  - earliest vs latest
  - previous vs latest

Optional outputs
- per-service/env compare reports under:
  .swagger_watch_state/history_reports/

Usage
    python eg_retail_swagger_history_page.py

Optional
    python eg_retail_swagger_history_page.py --state-dir .swagger_watch_state
"""

from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
SNAPSHOT_SUFFIX = ".normalized.json"


@dataclass
class SnapshotInfo:
    timestamp: str
    normalized_path: Path
    hash_path: Optional[Path]


@dataclass
class ServiceEnvHistory:
    service_name: str
    environment: str
    directory_name: str
    snapshots: List[SnapshotInfo]


def safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_").lower()


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sha_short(path: Optional[Path]) -> str:
    if not path or not path.exists():
        return ""
    return path.read_text(encoding="utf-8").strip()[:12]


def schema_signature(schema: Any) -> str:
    if schema is None:
        return ""
    return str(abs(hash(json.dumps(schema, sort_keys=True, ensure_ascii=False))))[:12]


def flatten_paths(spec: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    paths = spec.get("paths", {}) or {}
    out: Dict[str, Dict[str, Any]] = {}
    for path, methods in paths.items():
        if not isinstance(methods, dict):
            continue
        for method, op in methods.items():
            if str(method).lower() not in HTTP_METHODS:
                continue
            out[f"{str(method).upper()} {path}"] = op if isinstance(op, dict) else {}
    return out


def operation_signature(op: Dict[str, Any]) -> Dict[str, Any]:
    parameters = []
    for p in op.get("parameters", []) or []:
        if not isinstance(p, dict):
            continue
        parameters.append(
            {
                "name": p.get("name"),
                "in": p.get("in"),
                "required": p.get("required"),
                "schema": schema_signature(p.get("schema")),
            }
        )

    request_body = op.get("requestBody") or {}
    request_content = {}
    for content_type, body_desc in sorted((request_body.get("content") or {}).items()):
        request_content[content_type] = schema_signature((body_desc or {}).get("schema"))

    responses = {}
    for status, resp in sorted((op.get("responses") or {}).items(), key=lambda x: str(x[0])):
        content = {}
        for content_type, body_desc in sorted(((resp or {}).get("content") or {}).items()):
            content[content_type] = schema_signature((body_desc or {}).get("schema"))
        responses[str(status)] = content

    return {
        "summary": op.get("summary"),
        "operationId": op.get("operationId"),
        "tags": op.get("tags") or [],
        "parameters": parameters,
        "requestBody": request_content,
        "responses": responses,
        "security": op.get("security") or [],
        "deprecated": bool(op.get("deprecated", False)),
    }


def diff_specs(old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, List[str]]:
    old_ops = flatten_paths(old)
    new_ops = flatten_paths(new)
    old_keys = set(old_ops)
    new_keys = set(new_ops)

    added = sorted(new_keys - old_keys)
    removed = sorted(old_keys - new_keys)
    changed = [k for k in sorted(old_keys & new_keys) if operation_signature(old_ops[k]) != operation_signature(new_ops[k])]
    return {"added": added, "removed": removed, "changed": changed}


def parse_service_env_from_dirname(dirname: str) -> Tuple[str, str]:
    match = re.match(r"^(.*)_\[(DEV|TEST|PROD)\]$", dirname, flags=re.IGNORECASE)
    if not match:
        return dirname, ""
    raw_service = match.group(1).replace("_", " ").strip()
    return raw_service, match.group(2).upper()


def collect_histories(state_dir: Path) -> List[ServiceEnvHistory]:
    histories: List[ServiceEnvHistory] = []
    for child in sorted(state_dir.iterdir() if state_dir.exists() else []):
        if not child.is_dir():
            continue
        if child.name in {"history_reports", "data", "reports", "snapshots"}:
            continue
        snapshots_dir = child / "snapshots"
        if not snapshots_dir.exists():
            continue
        snapshot_map: Dict[str, Dict[str, Path]] = {}
        for p in snapshots_dir.iterdir():
            if p.name.endswith(SNAPSHOT_SUFFIX):
                ts = p.name[: -len(SNAPSHOT_SUFFIX)]
                snapshot_map.setdefault(ts, {})["normalized"] = p
            elif p.name.endswith(".sha256"):
                ts = p.name[: -len(".sha256")]
                snapshot_map.setdefault(ts, {})["hash"] = p
        snapshots = [
            SnapshotInfo(timestamp=ts, normalized_path=parts["normalized"], hash_path=parts.get("hash"))
            for ts, parts in sorted(snapshot_map.items())
            if "normalized" in parts
        ]
        if not snapshots:
            continue
        service_name, env = parse_service_env_from_dirname(child.name)
        histories.append(
            ServiceEnvHistory(
                service_name=service_name,
                environment=env,
                directory_name=child.name,
                snapshots=snapshots,
            )
        )
    return histories


def compare_snapshots(left: SnapshotInfo, right: SnapshotInfo) -> Dict[str, List[str]]:
    left_spec = load_json(left.normalized_path)
    right_spec = load_json(right.normalized_path)
    return diff_specs(left_spec, right_spec)


def build_compare_markdown(service: str, env: str, left: SnapshotInfo, right: SnapshotInfo, diff: Dict[str, List[str]]) -> str:
    lines = [
        f"# Historical Swagger compare: {service} [{env}]",
        "",
        f"- From: `{left.timestamp}`",
        f"- To: `{right.timestamp}`",
        f"- From hash: `{sha_short(left.hash_path)}`",
        f"- To hash: `{sha_short(right.hash_path)}`",
        "",
        "## Summary",
        f"- Added operations: {len(diff['added'])}",
        f"- Removed operations: {len(diff['removed'])}",
        f"- Changed operations: {len(diff['changed'])}",
        "",
    ]
    for section in ["added", "removed", "changed"]:
        lines.append(f"## {section.capitalize()}")
        items = diff[section]
        lines.extend([f"- {item}" for item in items] if items else ["- None"])
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def write_compare_report(state_dir: Path, history: ServiceEnvHistory, left: SnapshotInfo, right: SnapshotInfo) -> Tuple[Path, Dict[str, List[str]]]:
    diff = compare_snapshots(left, right)
    reports_dir = state_dir / "history_reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    base = f"{safe_name(history.service_name)}_{history.environment.lower()}_{left.timestamp}_vs_{right.timestamp}"
    md_path = reports_dir / f"{base}.md"
    json_path = reports_dir / f"{base}.json"

    markdown = build_compare_markdown(history.service_name, history.environment, left, right, diff)
    payload = {
        "service_name": history.service_name,
        "environment": history.environment,
        "from": left.timestamp,
        "to": right.timestamp,
        "diff": diff,
    }
    write_text(md_path, markdown)
    write_text(json_path, json.dumps(payload, ensure_ascii=False, indent=2))
    return md_path, diff


def render_diff_preview(diff: Dict[str, List[str]]) -> str:
    def block(title: str, items: List[str]) -> str:
        if not items:
            return f"<div class=\"mini-block\"><h5>{esc(title)}</h5><div class=\"muted\">None</div></div>"
        preview = items[:5]
        lis = "".join(f"<li><code>{esc(x)}</code></li>" for x in preview)
        more = "" if len(items) <= 5 else f"<div class=\"muted\">+ {len(items) - 5} more</div>"
        return f"<div class=\"mini-block\"><h5>{esc(title)}</h5><ul>{lis}</ul>{more}</div>"
    return block("Added", diff["added"]) + block("Removed", diff["removed"]) + block("Changed", diff["changed"])


def build_history_page(state_dir: Path) -> Path:
    histories = collect_histories(state_dir)
    cards: List[str] = []

    for history in histories:
        snapshots = history.snapshots
        earliest = snapshots[0]
        latest = snapshots[-1]
        previous = snapshots[-2] if len(snapshots) >= 2 else None

        latest_compare_html = "<div class=\"muted\">Need at least 2 snapshots</div>"
        if previous is not None:
            latest_md, latest_diff = write_compare_report(state_dir, history, previous, latest)
            latest_compare_html = f"""
            <div class=\"compare-card\">
              <div class=\"compare-head\">
                <h4>Previous vs Latest</h4>
                <a href=\"{esc(latest_md.name)}\" target=\"_blank\" rel=\"noreferrer\">Open report</a>
              </div>
              <div class=\"muted\">{esc(previous.timestamp)} → {esc(latest.timestamp)}</div>
              <div class=\"mini-grid\">{render_diff_preview(latest_diff)}</div>
            </div>
            """

        earliest_compare_html = "<div class=\"muted\">Need at least 2 snapshots</div>"
        if len(snapshots) >= 2:
            earliest_md, earliest_diff = write_compare_report(state_dir, history, earliest, latest)
            earliest_compare_html = f"""
            <div class=\"compare-card\">
              <div class=\"compare-head\">
                <h4>Earliest vs Latest</h4>
                <a href=\"{esc(earliest_md.name)}\" target=\"_blank\" rel=\"noreferrer\">Open report</a>
              </div>
              <div class=\"muted\">{esc(earliest.timestamp)} → {esc(latest.timestamp)}</div>
              <div class=\"mini-grid\">{render_diff_preview(earliest_diff)}</div>
            </div>
            """

        snapshot_list = "".join(
            f"<li><code>{esc(s.timestamp)}</code> <span class=\"muted\">{esc(sha_short(s.hash_path))}</span></li>"
            for s in reversed(snapshots[-10:])
        )

        cards.append(
            f"""
            <article class=\"service-card\">
              <div class=\"service-head\">
                <h2>{esc(history.service_name)} [{esc(history.environment)}]</h2>
                <span class=\"badge\">{len(snapshots)} snapshots</span>
              </div>
              <div class=\"stats\">
                <div class=\"stat\"><span>Earliest</span><strong>{esc(earliest.timestamp)}</strong></div>
                <div class=\"stat\"><span>Latest</span><strong>{esc(latest.timestamp)}</strong></div>
                <div class=\"stat\"><span>Count</span><strong>{len(snapshots)}</strong></div>
              </div>
              <div class=\"grid\">
                {latest_compare_html}
                {earliest_compare_html}
              </div>
              <details>
                <summary>Recent snapshots</summary>
                <ul>{snapshot_list}</ul>
              </details>
            </article>
            """
        )

    page = f"""
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>EG Retail Swagger History</title>
  <style>
    :root {{
      --bg: #0b1020;
      --card: #121933;
      --muted: #9fb0d0;
      --text: #eef4ff;
      --border: #263052;
      --accent: #7cc4ff;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, Segoe UI, Arial, sans-serif; background: var(--bg); color: var(--text); }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .wrap {{ max-width: 1400px; margin: 0 auto; padding: 24px; }}
    .hero {{ display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 24px; }}
    .hero h1 {{ margin: 0 0 6px; font-size: 32px; }}
    .muted {{ color: var(--muted); }}
    .service-card, .compare-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.18); }}
    .service-card {{ padding: 18px; margin-bottom: 18px; }}
    .service-head {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; margin-bottom: 14px; }}
    .service-head h2 {{ margin: 0; font-size: 24px; }}
    .badge {{ display: inline-block; border-radius: 999px; padding: 6px 10px; font-size: 12px; background: rgba(255,255,255,.08); }}
    .stats {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin-bottom: 14px; }}
    .stat {{ background: rgba(255,255,255,.03); border: 1px solid var(--border); border-radius: 14px; padding: 12px; }}
    .stat span {{ display: block; color: var(--muted); font-size: 12px; margin-bottom: 6px; }}
    .stat strong {{ font-size: 18px; overflow-wrap: anywhere; }}
    .grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }}
    .compare-card {{ padding: 14px; }}
    .compare-head {{ display: flex; justify-content: space-between; gap: 12px; align-items: center; margin-bottom: 8px; }}
    .compare-head h4 {{ margin: 0; font-size: 18px; }}
    .mini-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin-top: 12px; }}
    .mini-block {{ background: rgba(255,255,255,.03); border: 1px solid var(--border); border-radius: 12px; padding: 10px; }}
    .mini-block h5 {{ margin: 0 0 8px; font-size: 13px; }}
    ul {{ margin: 8px 0 0 18px; padding: 0; }}
    li {{ margin: 6px 0; }}
    code {{ background: rgba(255,255,255,.04); border: 1px solid var(--border); border-radius: 8px; padding: 2px 6px; word-break: break-word; }}
    details {{ margin-top: 14px; }}
    summary {{ cursor: pointer; color: var(--accent); }}
    @media (max-width: 1100px) {{ .grid, .mini-grid, .stats {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <div class=\"wrap\">
    <section class=\"hero\">
      <div>
        <h1>EG Retail Swagger History</h1>
        <div class=\"muted\">Generated from saved snapshots under {esc(str(state_dir))}</div>
      </div>
      <div><a href=\"index.html\">Back to dashboard</a></div>
    </section>
    {''.join(cards) if cards else '<div class="muted">No saved snapshots found yet.</div>'}
  </div>
</body>
</html>
    """.strip()

    history_path = state_dir / "history.html"
    write_text(history_path, page + "\n")
    return history_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build history page from saved Swagger snapshots")
    parser.add_argument("--state-dir", default=".swagger_watch_state")
    args = parser.parse_args()
    history_path = build_history_page(Path(args.state_dir))
    print(f"History page written to: {history_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
