#!/usr/bin/env python3
"""
EG Retail Swagger Watch Agent + HTML Dashboard

What it does
- Fetches DEV, TEST, and PROD OpenAPI/Swagger specs from DIRECT_SPECS_JSON
- Detects changes over time for each service/environment
- Detects DEV-vs-TEST and TEST-vs-PROD drift for each service
- Writes Markdown reports and a browsable HTML dashboard
- Optionally posts compact Slack notifications

Environment variables
- DIRECT_SPECS_JSON='[
    {
      "service_name": "CustomerOrderV2",
      "dev":  "https://.../swagger/v1/swagger.json",
      "test": "https://.../swagger/v1/swagger.json",
      "prod": "https://.../swagger/v1/swagger.json"
    }
  ]'
- POLL_INTERVAL_SECONDS=3600
- STATE_DIR=.swagger_watch_state
- SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...   # optional
- AUTH_HEADER=Bearer ...                                   # optional
- EXTRA_HEADERS_JSON={"X-Api-Key":"..."}                # optional
- REQUEST_TIMEOUT_SECONDS=30

How to add more monitored EG Swagger specs
1. Open the DIRECT_SPECS_JSON secret or environment variable.
2. Add one more JSON object to the array.
3. Provide service_name and any of dev, test, prod URLs.
4. Save and rerun the workflow.

Example:
[
  {
    "service_name": "CustomerOrderV2",
    "dev":  "https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json",
    "test": "https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json",
    "prod": "https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json"
  },
  {
    "service_name": "NewService",
    "dev":  "https://newservice.egretail-dev.cloud/swagger/v1/swagger.json",
    "test": "https://newservice.egretail-test.cloud/swagger/v1/swagger.json",
    "prod": "https://newservice.egretail.cloud/swagger/v1/swagger.json"
  }
]

Outputs
- Per-endpoint snapshots and markdown reports under STATE_DIR
- HTML dashboard at STATE_DIR/dashboard.html

Run
    python eg_retail_swagger_watch_agent.py
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests
import yaml


HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
IGNORE_TOP_LEVEL_KEYS = {
    "x-generated-at",
    "x-build-time",
    "x-generated-by",
    "x-request-id",
}
ENV_ORDER = ["DEV", "TEST", "PROD"]
DRIFT_PAIRS = [("DEV", "TEST"), ("TEST", "PROD")]


@dataclass
class ResolvedService:
    service_name: str
    environment: str
    docs_url: str
    swagger_url: str

    @property
    def key(self) -> str:
        return f"{self.service_name} [{self.environment}]"


@dataclass
class EnvCheckResult:
    service_name: str
    environment: str
    swagger_url: str
    status: str
    summary: str
    report: str
    spec: Optional[Dict[str, Any]]
    spec_hash: str
    counts: Dict[str, int]
    changed_items: Dict[str, List[str]]
    error: str = ""


@dataclass
class DriftCheckResult:
    service_name: str
    pair_name: str
    left_env: str
    right_env: str
    status: str
    report: str
    counts: Dict[str, int]
    changed_items: Dict[str, List[str]]
    left_url: str
    right_url: str
    left_hash: str
    right_hash: str
    error: str = ""


@dataclass
class DashboardServiceRow:
    service_name: str
    env_results: Dict[str, Optional[EnvCheckResult]]
    drift_results: List[DriftCheckResult]


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_env_json(name: str) -> Dict[str, str]:
    raw = os.getenv(name, "").strip()
    if not raw:
        return {}
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise RuntimeError(f"{name} must be a JSON object")
    return {str(k): str(v) for k, v in data.items()}


def build_headers() -> Dict[str, str]:
    headers = {
        "Accept": "application/json, application/yaml, text/yaml, */*",
        "User-Agent": "eg-retail-swagger-watch-agent/5.0",
    }
    auth = os.getenv("AUTH_HEADER", "").strip()
    if auth:
        headers["Authorization"] = auth
    headers.update(load_env_json("EXTRA_HEADERS_JSON"))
    return headers


def request_timeout() -> int:
    return int(os.getenv("REQUEST_TIMEOUT_SECONDS", "30"))


def fetch_spec(url: str) -> Tuple[str, Any]:
    resp = requests.get(url, headers=build_headers(), timeout=request_timeout())
    resp.raise_for_status()
    text = resp.text
    content_type = (resp.headers.get("content-type") or "").lower()

    if "json" in content_type:
        return text, resp.json()

    try:
        return text, resp.json()
    except Exception:
        return text, yaml.safe_load(text)


def normalize(obj: Any) -> Any:
    if isinstance(obj, dict):
        out = {}
        for key in sorted(obj.keys(), key=str):
            if key in IGNORE_TOP_LEVEL_KEYS:
                continue
            if isinstance(key, str) and key.lower() in {"generatedat", "buildtime", "timestamp"}:
                continue
            out[str(key)] = normalize(obj[key])
        return out
    if isinstance(obj, list):
        return [normalize(x) for x in obj]
    return obj


def canonical_json(obj: Any) -> str:
    return json.dumps(normalize(obj), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


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


def schema_signature(schema: Any) -> str:
    if schema is None:
        return ""
    return sha256(canonical_json(schema))[:12]


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


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_").lower()


def endpoint_dir(state_dir: Path, endpoint_name: str) -> Path:
    path = state_dir / safe_name(endpoint_name)
    ensure_dir(path)
    return path


def service_dir(state_dir: Path, service_name: str) -> Path:
    path = state_dir / safe_name(service_name)
    ensure_dir(path)
    return path


def read_text(path: Path) -> Optional[str]:
    return path.read_text(encoding="utf-8") if path.exists() else None


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def load_previous_spec(ep_dir: Path) -> Optional[Dict[str, Any]]:
    path = ep_dir / "latest.normalized.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_current_spec(ep_dir: Path, raw_text: str, normalized_obj: Dict[str, Any], digest: str) -> None:
    ts = now_iso().replace(":", "").replace("-", "")
    snapshots = ep_dir / "snapshots"
    ensure_dir(snapshots)

    write_text(ep_dir / "latest.raw.txt", raw_text)
    write_json(ep_dir / "latest.normalized.json", normalized_obj)
    write_text(ep_dir / "latest.sha256", digest)

    write_text(snapshots / f"{ts}.raw.txt", raw_text)
    write_json(snapshots / f"{ts}.normalized.json", normalized_obj)
    write_text(snapshots / f"{ts}.sha256", digest)


def direct_specs_from_env() -> List[ResolvedService]:
    raw = os.getenv("DIRECT_SPECS_JSON", "").strip()
    if not raw:
        raise RuntimeError("DIRECT_SPECS_JSON must be set")

    data = json.loads(raw)
    if not isinstance(data, list):
        raise RuntimeError("DIRECT_SPECS_JSON must be a JSON array")

    out: List[ResolvedService] = []
    for item in data:
        if not isinstance(item, dict):
            raise RuntimeError("Each DIRECT_SPECS_JSON item must be an object")

        service_name = str(item.get("service_name", "")).strip()
        if not service_name:
            raise RuntimeError("Each DIRECT_SPECS_JSON item must include service_name")

        for env_key in ["dev", "test", "prod"]:
            url = str(item.get(env_key, "")).strip()
            if url:
                out.append(
                    ResolvedService(
                        service_name=service_name,
                        environment=env_key.upper(),
                        docs_url=url,
                        swagger_url=url,
                    )
                )

    return out


def build_change_report(svc: ResolvedService, diff: Dict[str, List[str]], old_hash: str, new_hash: str) -> str:
    lines = [
        f"# Swagger/OpenAPI change detected: {svc.key}",
        "",
        f"- Time: {now_iso()}",
        f"- Swagger URL: {svc.swagger_url}",
        f"- Previous hash: `{old_hash}`",
        f"- Current hash: `{new_hash}`",
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


def build_drift_report(
    service_name: str,
    left_env: str,
    right_env: str,
    left_url: str,
    right_url: str,
    diff: Dict[str, List[str]],
    left_hash: str,
    right_hash: str,
) -> str:
    lines = [
        f"# {left_env} vs {right_env} drift detected: {service_name}",
        "",
        f"- Time: {now_iso()}",
        f"- {left_env} Swagger URL: {left_url}",
        f"- {right_env} Swagger URL: {right_url}",
        f"- {left_env} hash: `{left_hash}`",
        f"- {right_env} hash: `{right_hash}`",
        "",
        "## Summary",
        f"- Only in {left_env}: {len(diff['added'])}",
        f"- Only in {right_env}: {len(diff['removed'])}",
        f"- Present in both but different: {len(diff['changed'])}",
        "",
        f"## Only in {left_env}",
    ]

    lines.extend([f"- {item}" for item in diff["added"]] if diff["added"] else ["- None"])
    lines.append("")
    lines.append(f"## Only in {right_env}")
    lines.extend([f"- {item}" for item in diff["removed"]] if diff["removed"] else ["- None"])
    lines.append("")
    lines.append(f"## Different in {left_env} and {right_env}")
    lines.extend([f"- {item}" for item in diff["changed"]] if diff["changed"] else ["- None"])
    lines.append("")

    return "\n".join(lines).strip() + "\n"


def send_slack(text: str) -> None:
    webhook = os.getenv("SLACK_WEBHOOK_URL", "").strip()
    if not webhook:
        return
    resp = requests.post(webhook, json={"text": text[:3500]}, timeout=request_timeout())
    resp.raise_for_status()


def summarize_change_for_slack(svc: ResolvedService, diff: Dict[str, List[str]]) -> str:
    summary = (
        f"Swagger change detected in *{svc.key}* | "
        f"added={len(diff['added'])} | removed={len(diff['removed'])} | changed={len(diff['changed'])}"
    )
    preview = []
    preview += [f"+ {x}" for x in diff["added"][:3]]
    preview += [f"- {x}" for x in diff["removed"][:3]]
    preview += [f"~ {x}" for x in diff["changed"][:3]]
    return summary + (("\n" + "\n".join(preview)) if preview else "")


def summarize_drift_for_slack(service_name: str, left_env: str, right_env: str, diff: Dict[str, List[str]]) -> str:
    summary = (
        f"{left_env} vs {right_env} drift in *{service_name}* | "
        f"only_{left_env.lower()}={len(diff['added'])} | only_{right_env.lower()}={len(diff['removed'])} | different={len(diff['changed'])}"
    )
    preview = []
    preview += [f"{left_env}-only: {x}" for x in diff["added"][:2]]
    preview += [f"{right_env}-only: {x}" for x in diff["removed"][:2]]
    preview += [f"DIFF: {x}" for x in diff["changed"][:2]]
    return summary + (("\n" + "\n".join(preview)) if preview else "")


def check_service_change(svc: ResolvedService, state_dir: Path) -> EnvCheckResult:
    ep_dir = endpoint_dir(state_dir, svc.key)
    raw_text, parsed = fetch_spec(svc.swagger_url)

    if not isinstance(parsed, dict):
        raise RuntimeError(f"Parsed spec for {svc.key} is not an object")

    normalized = normalize(parsed)
    new_hash = sha256(canonical_json(normalized))
    old_hash = (read_text(ep_dir / "latest.sha256") or "").strip()
    old_spec = load_previous_spec(ep_dir)

    save_current_spec(ep_dir, raw_text, normalized, new_hash)

    if not old_hash:
        report = (
            f"Initialized baseline for {svc.key} at {now_iso()}\n"
            f"Swagger URL: {svc.swagger_url}\n"
            f"Hash: {new_hash}\n"
        )
        write_text(ep_dir / "last_report.md", report)
        return EnvCheckResult(
            service_name=svc.service_name,
            environment=svc.environment,
            swagger_url=svc.swagger_url,
            status="baseline",
            summary=f"Initialized baseline ({new_hash[:12]})",
            report=report,
            spec=normalized,
            spec_hash=new_hash,
            counts={"added": 0, "removed": 0, "changed": 0},
            changed_items={"added": [], "removed": [], "changed": []},
        )

    if old_hash == new_hash:
        return EnvCheckResult(
            service_name=svc.service_name,
            environment=svc.environment,
            swagger_url=svc.swagger_url,
            status="no_change",
            summary=f"No change ({new_hash[:12]})",
            report=f"No change for {svc.key} ({new_hash[:12]})",
            spec=normalized,
            spec_hash=new_hash,
            counts={"added": 0, "removed": 0, "changed": 0},
            changed_items={"added": [], "removed": [], "changed": []},
        )

    diff = diff_specs(old_spec or {}, normalized)
    report = build_change_report(svc, diff, old_hash, new_hash)
    write_text(ep_dir / "last_report.md", report)
    send_slack(summarize_change_for_slack(svc, diff))
    return EnvCheckResult(
        service_name=svc.service_name,
        environment=svc.environment,
        swagger_url=svc.swagger_url,
        status="changed",
        summary=f"Changed: +{len(diff['added'])} / -{len(diff['removed'])} / ~{len(diff['changed'])}",
        report=report,
        spec=normalized,
        spec_hash=new_hash,
        counts={
            "added": len(diff["added"]),
            "removed": len(diff["removed"]),
            "changed": len(diff["changed"]),
        },
        changed_items=diff,
    )


def failed_env_result(svc: ResolvedService, error: Exception) -> EnvCheckResult:
    return EnvCheckResult(
        service_name=svc.service_name,
        environment=svc.environment,
        swagger_url=svc.swagger_url,
        status="error",
        summary=str(error),
        report=str(error),
        spec=None,
        spec_hash="",
        counts={"added": 0, "removed": 0, "changed": 0},
        changed_items={"added": [], "removed": [], "changed": []},
        error=str(error),
    )


def check_env_pair_drift(
    service_name: str,
    left_env: str,
    right_env: str,
    left_svc: ResolvedService,
    right_svc: ResolvedService,
    left_spec: Dict[str, Any],
    right_spec: Dict[str, Any],
    left_hash: str,
    right_hash: str,
    state_dir: Path,
) -> DriftCheckResult:
    svc_dir = service_dir(state_dir, f"{service_name}_{left_env.lower()}_vs_{right_env.lower()}")
    latest_drift_hash_path = svc_dir / "latest_drift.sha256"

    diff = diff_specs(right_spec, left_spec)
    drift_payload = {
        f"only_in_{left_env.lower()}": diff["added"],
        f"only_in_{right_env.lower()}": diff["removed"],
        "different": diff["changed"],
        f"{left_env.lower()}_hash": left_hash,
        f"{right_env.lower()}_hash": right_hash,
    }
    drift_hash = sha256(json.dumps(drift_payload, sort_keys=True, ensure_ascii=False))

    has_drift = bool(diff["added"] or diff["removed"] or diff["changed"])
    previous_drift_hash = (read_text(latest_drift_hash_path) or "").strip()
    pair_name = f"{left_env} vs {right_env}"

    if not has_drift:
        write_text(latest_drift_hash_path, drift_hash)
        report = f"No {pair_name} drift for {service_name}"
        write_text(svc_dir / "last_drift_report.md", report)
        return DriftCheckResult(
            service_name=service_name,
            pair_name=pair_name,
            left_env=left_env,
            right_env=right_env,
            status="aligned",
            report=report,
            counts={f"only_in_{left_env.lower()}": 0, f"only_in_{right_env.lower()}": 0, "different": 0},
            changed_items={f"only_in_{left_env.lower()}": [], f"only_in_{right_env.lower()}": [], "different": []},
            left_url=left_svc.swagger_url,
            right_url=right_svc.swagger_url,
            left_hash=left_hash,
            right_hash=right_hash,
        )

    report = build_drift_report(
        service_name=service_name,
        left_env=left_env,
        right_env=right_env,
        left_url=left_svc.swagger_url,
        right_url=right_svc.swagger_url,
        diff=diff,
        left_hash=left_hash,
        right_hash=right_hash,
    )
    write_text(svc_dir / "last_drift_report.md", report)
    write_text(latest_drift_hash_path, drift_hash)

    if previous_drift_hash != drift_hash:
        send_slack(summarize_drift_for_slack(service_name, left_env, right_env, diff))

    return DriftCheckResult(
        service_name=service_name,
        pair_name=pair_name,
        left_env=left_env,
        right_env=right_env,
        status="drift" if previous_drift_hash == drift_hash else "drift_changed",
        report=report,
        counts={
            f"only_in_{left_env.lower()}": len(diff["added"]),
            f"only_in_{right_env.lower()}": len(diff["removed"]),
            "different": len(diff["changed"]),
        },
        changed_items={
            f"only_in_{left_env.lower()}": diff["added"],
            f"only_in_{right_env.lower()}": diff["removed"],
            "different": diff["changed"],
        },
        left_url=left_svc.swagger_url,
        right_url=right_svc.swagger_url,
        left_hash=left_hash,
        right_hash=right_hash,
    )


def failed_drift_result(service_name: str, left_env: str, right_env: str, left_url: str, right_url: str, error: Exception) -> DriftCheckResult:
    pair_name = f"{left_env} vs {right_env}"
    return DriftCheckResult(
        service_name=service_name,
        pair_name=pair_name,
        left_env=left_env,
        right_env=right_env,
        status="error",
        report=str(error),
        counts={f"only_in_{left_env.lower()}": 0, f"only_in_{right_env.lower()}": 0, "different": 0},
        changed_items={f"only_in_{left_env.lower()}": [], f"only_in_{right_env.lower()}": [], "different": []},
        left_url=left_url,
        right_url=right_url,
        left_hash="",
        right_hash="",
        error=str(error),
    )


def status_badge_class(status: str) -> str:
    return {
        "changed": "warn",
        "baseline": "info",
        "no_change": "ok",
        "aligned": "ok",
        "drift": "warn",
        "drift_changed": "warn",
        "error": "bad",
    }.get(status, "info")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def list_to_html(items: List[str], empty_label: str = "None") -> str:
    if not items:
        return f"<div class=\"muted\">{esc(empty_label)}</div>"
    lis = "".join(f"<li><code>{esc(item)}</code></li>" for item in items)
    return f"<ul>{lis}</ul>"


def render_env_panel(result: Optional[EnvCheckResult], title: str) -> str:
    if result is None:
        return f"<section class=\"panel\"><h3>{esc(title)}</h3><div class=\"muted\">Not configured</div></section>"

    counts = result.counts
    added_html = list_to_html(result.changed_items.get("added", []))
    removed_html = list_to_html(result.changed_items.get("removed", []))
    changed_html = list_to_html(result.changed_items.get("changed", []))

    return f"""
    <section class=\"panel\">
      <div class=\"panel-head\">
        <h3>{esc(title)}</h3>
        <span class=\"badge {status_badge_class(result.status)}\">{esc(result.status.replace('_', ' '))}</span>
      </div>
      <div class=\"kv\"><span>URL</span><a href=\"{esc(result.swagger_url)}\" target=\"_blank\" rel=\"noreferrer\">{esc(result.swagger_url)}</a></div>
      <div class=\"kv\"><span>Hash</span><code>{esc(result.spec_hash[:12] if result.spec_hash else '')}</code></div>
      <div class=\"kv\"><span>Summary</span><strong>{esc(result.summary)}</strong></div>
      <div class=\"stats\">
        <div class=\"stat\"><span>Added</span><strong>{counts.get('added', 0)}</strong></div>
        <div class=\"stat\"><span>Removed</span><strong>{counts.get('removed', 0)}</strong></div>
        <div class=\"stat\"><span>Changed</span><strong>{counts.get('changed', 0)}</strong></div>
      </div>
      <details>
        <summary>Details</summary>
        <h4>Added</h4>
        {added_html}
        <h4>Removed</h4>
        {removed_html}
        <h4>Changed</h4>
        {changed_html}
        {f'<pre>{esc(result.report)}</pre>' if result.report else ''}
      </details>
    </section>
    """


def render_drift_panel(result: DriftCheckResult) -> str:
    only_left_key = f"only_in_{result.left_env.lower()}"
    only_right_key = f"only_in_{result.right_env.lower()}"
    only_left_html = list_to_html(result.changed_items.get(only_left_key, []))
    only_right_html = list_to_html(result.changed_items.get(only_right_key, []))
    different_html = list_to_html(result.changed_items.get("different", []))

    return f"""
    <section class=\"panel drift\">
      <div class=\"panel-head\">
        <h3>{esc(result.pair_name)}</h3>
        <span class=\"badge {status_badge_class(result.status)}\">{esc(result.status.replace('_', ' '))}</span>
      </div>
      <div class=\"kv\"><span>{esc(result.left_env)}</span><a href=\"{esc(result.left_url)}\" target=\"_blank\" rel=\"noreferrer\">{esc(result.left_url)}</a></div>
      <div class=\"kv\"><span>{esc(result.right_env)}</span><a href=\"{esc(result.right_url)}\" target=\"_blank\" rel=\"noreferrer\">{esc(result.right_url)}</a></div>
      <div class=\"stats\">
        <div class=\"stat\"><span>Only in {esc(result.left_env)}</span><strong>{result.counts.get(only_left_key, 0)}</strong></div>
        <div class=\"stat\"><span>Only in {esc(result.right_env)}</span><strong>{result.counts.get(only_right_key, 0)}</strong></div>
        <div class=\"stat\"><span>Different</span><strong>{result.counts.get('different', 0)}</strong></div>
      </div>
      <details>
        <summary>Details</summary>
        <h4>Only in {esc(result.left_env)}</h4>
        {only_left_html}
        <h4>Only in {esc(result.right_env)}</h4>
        {only_right_html}
        <h4>Different</h4>
        {different_html}
        {f'<pre>{esc(result.report)}</pre>' if result.report else ''}
      </details>
    </section>
    """


def build_dashboard(rows: List[DashboardServiceRow], output_path: Path) -> None:
    service_cards = []
    changed_count = 0
    drift_count = 0
    error_count = 0

    for row in rows:
        for env_name in ENV_ORDER:
            env_result = row.env_results.get(env_name)
            if env_result and env_result.status == "changed":
                changed_count += 1
            if env_result and env_result.status == "error":
                error_count += 1
        for drift in row.drift_results:
            if drift.status in {"drift", "drift_changed"}:
                drift_count += 1
            if drift.status == "error":
                error_count += 1

        env_panels = "".join(render_env_panel(row.env_results.get(env_name), env_name) for env_name in ENV_ORDER)
        drift_panels = "".join(render_drift_panel(drift) for drift in row.drift_results)

        service_cards.append(
            f"""
            <article class=\"service-card\">
              <div class=\"service-head\">
                <h2>{esc(row.service_name)}</h2>
              </div>
              <div class=\"grid env-grid\">{env_panels}</div>
              <div class=\"grid drift-grid\">{drift_panels}</div>
            </article>
            """
        )

    html_doc = f"""
<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>EG Retail Swagger Dashboard</title>
  <style>
    :root {{
      --bg: #0b1020;
      --card: #121933;
      --muted: #9fb0d0;
      --text: #eef4ff;
      --border: #263052;
      --ok: #153a2a;
      --warn: #4a3310;
      --bad: #4c1720;
      --info: #17324c;
      --accent: #7cc4ff;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Inter, Segoe UI, Arial, sans-serif; background: var(--bg); color: var(--text); }}
    a {{ color: var(--accent); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    .wrap {{ max-width: 1600px; margin: 0 auto; padding: 24px; }}
    .hero {{ display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 24px; }}
    .hero h1 {{ margin: 0 0 6px; font-size: 32px; }}
    .muted {{ color: var(--muted); }}
    .summary {{ display: grid; grid-template-columns: repeat(4, minmax(140px, 1fr)); gap: 12px; margin: 20px 0 28px; }}
    .summary .card, .panel, .service-card {{ background: var(--card); border: 1px solid var(--border); border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.18); }}
    .summary .card {{ padding: 16px; }}
    .summary .card span {{ display: block; color: var(--muted); font-size: 13px; margin-bottom: 6px; }}
    .summary .card strong {{ font-size: 28px; }}
    .service-card {{ padding: 18px; margin-bottom: 18px; }}
    .service-head {{ margin-bottom: 14px; }}
    .service-head h2 {{ margin: 0; font-size: 24px; }}
    .grid {{ display: grid; gap: 14px; }}
    .env-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); margin-bottom: 14px; }}
    .drift-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .panel {{ padding: 16px; min-width: 0; }}
    .panel-head {{ display: flex; justify-content: space-between; gap: 10px; align-items: center; margin-bottom: 12px; }}
    .panel h3 {{ margin: 0; font-size: 18px; }}
    .badge {{ display: inline-block; border-radius: 999px; padding: 6px 10px; font-size: 12px; text-transform: uppercase; letter-spacing: .04em; }}
    .badge.ok {{ background: var(--ok); }}
    .badge.warn {{ background: var(--warn); }}
    .badge.bad {{ background: var(--bad); }}
    .badge.info {{ background: var(--info); }}
    .kv {{ display: grid; grid-template-columns: 72px 1fr; gap: 10px; font-size: 14px; margin: 8px 0; align-items: start; }}
    .kv span {{ color: var(--muted); }}
    .stats {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; margin-top: 14px; }}
    .stat {{ background: rgba(255,255,255,.03); border: 1px solid var(--border); border-radius: 14px; padding: 12px; }}
    .stat span {{ display: block; color: var(--muted); font-size: 12px; margin-bottom: 6px; }}
    .stat strong {{ font-size: 22px; }}
    details {{ margin-top: 14px; }}
    summary {{ cursor: pointer; color: var(--accent); }}
    ul {{ margin: 8px 0 0 18px; padding: 0; }}
    li {{ margin: 6px 0; }}
    code, pre {{ background: rgba(255,255,255,.04); border: 1px solid var(--border); border-radius: 8px; }}
    code {{ padding: 2px 6px; word-break: break-word; }}
    pre {{ white-space: pre-wrap; overflow-wrap: anywhere; padding: 12px; font-size: 12px; margin-top: 12px; }}
    @media (max-width: 1300px) {{ .env-grid, .drift-grid {{ grid-template-columns: 1fr; }} .summary {{ grid-template-columns: repeat(2, minmax(140px, 1fr)); }} }}
    @media (max-width: 640px) {{ .hero {{ display: block; }} .summary {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
  <div class=\"wrap\">
    <section class=\"hero\">
      <div>
        <h1>EG Retail Swagger Dashboard</h1>
        <div class=\"muted\">Generated at {esc(now_iso())}</div>
      </div>
      <div class=\"muted\">Output: {esc(str(output_path))}</div>
    </section>

    <section class=\"summary\">
      <div class=\"card\"><span>Services</span><strong>{len(rows)}</strong></div>
      <div class=\"card\"><span>Env changes</span><strong>{changed_count}</strong></div>
      <div class=\"card\"><span>Drifts</span><strong>{drift_count}</strong></div>
      <div class=\"card\"><span>Errors</span><strong>{error_count}</strong></div>
    </section>

    {''.join(service_cards)}
  </div>
</body>
</html>
    """.strip()

    write_text(output_path, html_doc + "\n")


def run_once() -> int:
    state_dir = Path(os.getenv("STATE_DIR", ".swagger_watch_state"))
    ensure_dir(state_dir)

    try:
        resolved = direct_specs_from_env()
    except Exception as exc:
        print(f"ERROR while loading DIRECT_SPECS_JSON: {exc}", file=sys.stderr)
        return 2

    if not resolved:
        print("No services configured.", file=sys.stderr)
        return 2

    grouped: Dict[str, Dict[str, ResolvedService]] = {}
    for svc in resolved:
        grouped.setdefault(svc.service_name, {})[svc.environment] = svc

    exit_code = 0
    dashboard_rows: List[DashboardServiceRow] = []
    print(f"Loaded {len(resolved)} service-environment specs from DIRECT_SPECS_JSON")

    for service_name in sorted(grouped):
        envs = grouped[service_name]
        env_results: Dict[str, Optional[EnvCheckResult]] = {env: None for env in ENV_ORDER}
        drift_results: List[DriftCheckResult] = []

        for env_name in ENV_ORDER:
            svc = envs.get(env_name)
            if svc is None:
                continue
            try:
                result = check_service_change(svc, state_dir)
                env_results[env_name] = result
                print(result.report.strip())
                print("-" * 80)
            except Exception as exc:
                exit_code = 1
                env_results[env_name] = failed_env_result(svc, exc)
                print(f"ERROR while checking {svc.key}: {exc}", file=sys.stderr)

        for left_env, right_env in DRIFT_PAIRS:
            left_svc = envs.get(left_env)
            right_svc = envs.get(right_env)
            left_result = env_results.get(left_env)
            right_result = env_results.get(right_env)

            if left_svc is None or right_svc is None:
                continue

            if left_result and right_result and left_result.spec is not None and right_result.spec is not None:
                try:
                    drift = check_env_pair_drift(
                        service_name=service_name,
                        left_env=left_env,
                        right_env=right_env,
                        left_svc=left_svc,
                        right_svc=right_svc,
                        left_spec=left_result.spec,
                        right_spec=right_result.spec,
                        left_hash=left_result.spec_hash,
                        right_hash=right_result.spec_hash,
                        state_dir=state_dir,
                    )
                    drift_results.append(drift)
                    print(drift.report.strip())
                    print("=" * 80)
                except Exception as exc:
                    exit_code = 1
                    drift = failed_drift_result(service_name, left_env, right_env, left_svc.swagger_url, right_svc.swagger_url, exc)
                    drift_results.append(drift)
                    print(f"ERROR while checking {left_env} vs {right_env} drift for {service_name}: {exc}", file=sys.stderr)
            else:
                drift_results.append(
                    failed_drift_result(
                        service_name,
                        left_env,
                        right_env,
                        left_svc.swagger_url,
                        right_svc.swagger_url,
                        RuntimeError(f"{left_env} vs {right_env} drift check skipped because one env fetch failed"),
                    )
                )

        dashboard_rows.append(DashboardServiceRow(service_name=service_name, env_results=env_results, drift_results=drift_results))

    dashboard_path = state_dir / "dashboard.html"
    build_dashboard(dashboard_rows, dashboard_path)
    print(f"HTML dashboard written to: {dashboard_path}")
    return exit_code


def main() -> int:
    interval = int(os.getenv("POLL_INTERVAL_SECONDS", "0") or "0")
    if interval <= 0:
        return run_once()

    print(f"Starting EG Retail Swagger Watch Agent with interval={interval}s")
    while True:
        code = run_once()
        if code != 0:
            print(f"Completed cycle with errors at {now_iso()}", file=sys.stderr)
        time.sleep(interval)


if __name__ == "__main__":
    raise SystemExit(main())
