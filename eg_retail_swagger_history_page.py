#!/usr/bin/env python3
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


def build_history_index(histories: List[ServiceEnvHistory]) -> Dict[str, Any]:
    items = []
    for history in histories:
        items.append(
            {
                "id": f"{history.service_name} [{history.environment}]",
                "service_name": history.service_name,
                "environment": history.environment,
                "snapshots": [
                    {
                        "timestamp": s.timestamp,
                        "hash": sha_short(s.hash_path),
                        "file": s.normalized_path.name,
                    }
                    for s in history.snapshots
                ],
            }
        )
    return {"services": items}


def build_history_page(state_dir: Path) -> Path:
    histories = collect_histories(state_dir)
    history_index = build_history_index(histories)
    history_index_path = state_dir / "history_index.json"
    write_text(history_index_path, json.dumps(history_index, ensure_ascii=False, indent=2))

    page = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
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
    .topnav {{ display: flex; gap: 12px; margin-bottom: 18px; }}
    .topnav a {{ background: rgba(255,255,255,.05); border: 1px solid var(--border); border-radius: 10px; padding: 8px 12px; }}
    .hero {{ display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 24px; }}
    .hero h1 {{ margin: 0 0 6px; font-size: 32px; }}
    .muted {{ color: var(--muted); }}
    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: 0 10px 30px rgba(0,0,0,.18);
      padding: 18px;
      margin-bottom: 18px;
    }}
    .selectors {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr auto;
      gap: 12px;
      align-items: end;
    }}
    label {{ display: block; margin-bottom: 6px; color: var(--muted); font-size: 13px; }}
    select, button {{
      width: 100%;
      background: rgba(255,255,255,.04);
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 12px;
    }}
    button {{
      cursor: pointer;
      background: rgba(124,196,255,.14);
    }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin-top: 16px;
    }}
    .stat {{
      background: rgba(255,255,255,.03);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 12px;
    }}
    .stat span {{ display: block; color: var(--muted); font-size: 12px; margin-bottom: 6px; }}
    .stat strong {{ font-size: 18px; overflow-wrap: anywhere; }}
    .section-title {{ margin: 18px 0 8px; font-size: 18px; }}
    ul {{ margin: 8px 0 0 18px; padding: 0; }}
    li {{ margin: 6px 0; }}
    code {{
      background: rgba(255,255,255,.04);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 2px 6px;
      word-break: break-word;
    }}
    @media (max-width: 900px) {{
      .selectors, .stats {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <nav class="topnav">
      <a href="index.html">Dashboard</a>
      <a href="history.html">History</a>
    </nav>

    <section class="hero">
      <div>
        <h1>EG Retail Swagger History</h1>
        <div class="muted">Choose any two saved snapshots and compare them.</div>
      </div>
    </section>

    <section class="card">
      <div class="selectors">
        <div>
          <label for="serviceSelect">Service / env</label>
          <select id="serviceSelect"></select>
        </div>
        <div>
          <label for="fromSelect">From</label>
          <select id="fromSelect"></select>
        </div>
        <div>
          <label for="toSelect">To</label>
          <select id="toSelect"></select>
        </div>
        <div>
          <label>&nbsp;</label>
          <button id="compareBtn" type="button">Compare</button>
        </div>
      </div>

      <div class="stats">
        <div class="stat"><span>Snapshot count</span><strong id="countValue">-</strong></div>
        <div class="stat"><span>Earliest</span><strong id="earliestValue">-</strong></div>
        <div class="stat"><span>Latest</span><strong id="latestValue">-</strong></div>
      </div>

      <h3 class="section-title">Compare result</h3>
      <div id="result" class="muted">Pick a service and two snapshots, then click Compare.</div>
    </section>
  </div>

  <script>
    async function loadIndex() {{
      const res = await fetch('history_index.json', {{ cache: 'no-store' }});
      if (!res.ok) throw new Error('Could not load history_index.json');
      return res.json();
    }}

    function fillSelect(select, values) {{
      select.innerHTML = '';
      for (const value of values) {{
        const opt = document.createElement('option');
        opt.value = value;
        opt.textContent = value;
        select.appendChild(opt);
      }}
    }}

    function renderDiff(diff) {{
      const section = (title, items) => {{
        const list = items.length
          ? `<ul>${{items.map(x => `<li><code>${{x}}</code></li>`).join('')}}</ul>`
          : `<div class="muted">None</div>`;
        return `<h4>${{title}}</h4>${{list}}`;
      }};
      return `
        <div class="stats">
          <div class="stat"><span>Added</span><strong>${{diff.added.length}}</strong></div>
          <div class="stat"><span>Removed</span><strong>${{diff.removed.length}}</strong></div>
          <div class="stat"><span>Changed</span><strong>${{diff.changed.length}}</strong></div>
        </div>
        ${{section('Added', diff.added)}}
        ${{section('Removed', diff.removed)}}
        ${{section('Changed', diff.changed)}}
      `;
    }}

    function compareSpecs(oldSpec, newSpec) {{
      const flattenPaths = (spec) => {{
        const paths = spec.paths || {{}};
        const out = {{}};
        for (const [path, methods] of Object.entries(paths)) {{
          if (!methods || typeof methods !== 'object') continue;
          for (const [method, op] of Object.entries(methods)) {{
            const m = String(method).toLowerCase();
            if (!['get','post','put','patch','delete','head','options','trace'].includes(m)) continue;
            out[`${{method.toUpperCase()}} ${{path}}`] = op || {{}};
          }}
        }}
        return out;
      }};

      const opSig = (op) => JSON.stringify(op);
      const a = flattenPaths(oldSpec);
      const b = flattenPaths(newSpec);
      const aKeys = new Set(Object.keys(a));
      const bKeys = new Set(Object.keys(b));

      const added = [...bKeys].filter(x => !aKeys.has(x)).sort();
      const removed = [...aKeys].filter(x => !bKeys.has(x)).sort();
      const changed = [...aKeys].filter(x => bKeys.has(x) && opSig(a[x]) !== opSig(b[x])).sort();

      return {{ added, removed, changed }};
    }}

    async function main() {{
      const data = await loadIndex();
      const services = data.services || [];

      const serviceSelect = document.getElementById('serviceSelect');
      const fromSelect = document.getElementById('fromSelect');
      const toSelect = document.getElementById('toSelect');
      const compareBtn = document.getElementById('compareBtn');
      const result = document.getElementById('result');

      const countValue = document.getElementById('countValue');
      const earliestValue = document.getElementById('earliestValue');
      const latestValue = document.getElementById('latestValue');

      const map = new Map(services.map(s => [s.id, s]));
      fillSelect(serviceSelect, services.map(s => s.id));

      function refreshSnapshotSelectors() {{
        const current = map.get(serviceSelect.value);
        const snaps = (current?.snapshots || []).map(s => s.timestamp);

        fillSelect(fromSelect, snaps);
        fillSelect(toSelect, snaps);

        if (snaps.length > 0) {{
          fromSelect.value = snaps[0];
          toSelect.value = snaps[snaps.length - 1];
          countValue.textContent = String(snaps.length);
          earliestValue.textContent = snaps[0];
          latestValue.textContent = snaps[snaps.length - 1];
        }} else {{
          countValue.textContent = '-';
          earliestValue.textContent = '-';
          latestValue.textContent = '-';
        }}
      }}

      serviceSelect.addEventListener('change', refreshSnapshotSelectors);
      refreshSnapshotSelectors();

      compareBtn.addEventListener('click', async () => {{
        const current = map.get(serviceSelect.value);
        if (!current) return;

        const fromTs = fromSelect.value;
        const toTs = toSelect.value;
        const fromSnap = current.snapshots.find(s => s.timestamp === fromTs);
        const toSnap = current.snapshots.find(s => s.timestamp === toTs);

        if (!fromSnap || !toSnap) {{
          result.innerHTML = '<div class="muted">Invalid snapshot selection.</div>';
          return;
        }}

        if (fromTs === toTs) {{
          result.innerHTML = '<div class="muted">Choose two different snapshots.</div>';
          return;
        }}

        const dirName = `${{current.service_name}} [${{current.environment}}]`
          .replace(/[^a-zA-Z0-9._-]+/g, '_')
          .replace(/^_+|_+$/g, '')
          .toLowerCase();

        const fromUrl = `${{dirName}}/snapshots/${{fromTs}}.normalized.json`;
        const toUrl = `${{dirName}}/snapshots/${{toTs}}.normalized.json`;

        try {{
          const [aRes, bRes] = await Promise.all([
            fetch(fromUrl, {{ cache: 'no-store' }}),
            fetch(toUrl, {{ cache: 'no-store' }}),
          ]);

          if (!aRes.ok || !bRes.ok) {{
            result.innerHTML = '<div class="muted">Could not load one of the selected snapshots.</div>';
            return;
          }}

          const [aSpec, bSpec] = await Promise.all([aRes.json(), bRes.json()]);
          const diff = compareSpecs(aSpec, bSpec);

          result.innerHTML = `
            <div class="muted">${{fromTs}} → ${{toTs}}</div>
            ${{renderDiff(diff)}}
          `;
        }} catch (err) {{
          result.innerHTML = `<div class="muted">Compare failed: ${{err.message}}</div>`;
        }}
      }});
    }}

    main().catch(err => {{
      document.getElementById('result').innerHTML = `<div class="muted">Initialization failed: ${{err.message}}</div>`;
    }});
  </script>
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