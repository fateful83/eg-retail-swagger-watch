#!/usr/bin/env python3
"""
EG Retail Swagger Watch Agent V4

What it does
- Fetches DEV / TEST / PROD OpenAPI/Swagger specs from DIRECT_SPECS_JSON
- Detects changes over time for each service/environment
- Distinguishes:
    - no_change
    - docs_only
    - non_breaking
    - breaking
- Detects DEV-vs-TEST and TEST-vs-PROD drift
- Distinguishes drift as:
    - aligned
    - non_breaking
    - breaking
- Persists snapshots and reports under STATE_DIR
- Writes a browsable HTML dashboard
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
- STATE_DIR=.swagger_watch_state
- POLL_INTERVAL_SECONDS=0
- RETENTION_DAYS=180
- SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...   # optional
- AUTH_HEADER=Bearer ...                                   # optional
- EXTRA_HEADERS_JSON={"X-Api-Key":"..."}                   # optional
- REQUEST_TIMEOUT_SECONDS=60
- FAIL_ON_SERVICE_ERRORS=false
"""

from __future__ import annotations

import copy
import hashlib
import html
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
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
    file_changed: bool = False
    api_changed: bool = False
    breaking_changed: bool = False
    fetched_at: str = ""
    duration_ms: int = 0
    error: str = ""


@dataclass
class DriftCheckResult:
    service_name: str
    pair_name: str
    left_env: str
    right_env: str
    status: str
    severity: str
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


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def now_iso() -> str:
    return now_utc().strftime("%Y-%m-%dT%H:%M:%SZ")


def bool_env(name: str, default: bool) -> bool:
    raw = os.getenv(name, str(default)).strip().lower()
    return raw in {"1", "true", "yes", "y", "on"}


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
        "User-Agent": "eg-retail-swagger-watch-agent/7.0",
    }
    auth = os.getenv("AUTH_HEADER", "").strip()
    if auth:
        headers["Authorization"] = auth
    headers.update(load_env_json("EXTRA_HEADERS_JSON"))
    return headers


def request_timeout() -> int:
    return int(os.getenv("REQUEST_TIMEOUT_SECONDS", "60"))


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


def _drop_non_contract_metadata(node: Any) -> Any:
    """
    Deeply removes documentation-only and presentation-oriented fields so that
    comparisons focus on contract shape instead of text metadata.
    """
    if isinstance(node, dict):
        cleaned: Dict[str, Any] = {}
        for key, value in node.items():
            k = str(key)

            if k in {
                "description",
                "summary",
                "externalDocs",
                "example",
                "examples",
                "title",
                "contact",
                "license",
                "termsOfService",
                "x-generated-at",
                "x-build-time",
                "x-generated-by",
                "x-request-id",
            }:
                continue

            # Ignore top-level cosmetic structures later as well
            cleaned[k] = _drop_non_contract_metadata(value)

        return {k: cleaned[k] for k in sorted(cleaned.keys(), key=str)}

    if isinstance(node, list):
        return [_drop_non_contract_metadata(x) for x in node]

    return node


def normalize_contract_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Produces a metadata-light, contract-focused normalized spec for use in
    docs_only detection and drift reduction.
    """
    if not isinstance(spec, dict):
        return {}

    spec = copy.deepcopy(spec)
    spec = normalize(spec)
    spec = _drop_non_contract_metadata(spec)

    for top_key in ["servers", "externalDocs"]:
        spec.pop(top_key, None)

    # info.version often changes for docs/build reasons and can inflate noise
    info = spec.get("info")
    if isinstance(info, dict):
        info.pop("version", None)
        if not info:
            spec.pop("info", None)

    # Trim tag descriptions to avoid docs-only drift
    tags = spec.get("tags")
    if isinstance(tags, list):
        cleaned_tags = []
        for tag in tags:
            if isinstance(tag, dict):
                t = dict(tag)
                t.pop("description", None)
                t.pop("externalDocs", None)
                cleaned_tags.append({k: t[k] for k in sorted(t.keys(), key=str)})
            else:
                cleaned_tags.append(tag)
        spec["tags"] = cleaned_tags

    return spec


def canonical_json(obj: Any) -> str:
    return json.dumps(normalize(obj), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_contract_json(obj: Any) -> str:
    return json.dumps(normalize_contract_spec(obj if isinstance(obj, dict) else {}), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


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
    normalized_schema = _drop_non_contract_metadata(normalize(schema))
    return sha256(json.dumps(normalized_schema, ensure_ascii=False, sort_keys=True, separators=(",", ":")))[:12]


def operation_signature(op: Dict[str, Any]) -> Dict[str, Any]:
    parameters = []
    for p in op.get("parameters", []) or []:
        if not isinstance(p, dict):
            continue
        parameters.append(
            {
                "name": p.get("name"),
                "in": p.get("in"),
                "required": bool(p.get("required", False)),
                "schema": schema_signature(p.get("schema")),
            }
        )
    parameters.sort(key=lambda x: (str(x.get("in")), str(x.get("name"))))

    request_body = op.get("requestBody") or {}
    request_required = bool(request_body.get("required", False)) if isinstance(request_body, dict) else False
    request_content = {}
    for content_type, body_desc in sorted((request_body.get("content") or {}).items()):
        request_content[str(content_type)] = schema_signature((body_desc or {}).get("schema"))

    responses = {}
    for status, resp in sorted((op.get("responses") or {}).items(), key=lambda x: str(x[0])):
        content = {}
        for content_type, body_desc in sorted(((resp or {}).get("content") or {}).items()):
            content[str(content_type)] = schema_signature((body_desc or {}).get("schema"))
        responses[str(status)] = content

    security = op.get("security") or []
    security_norm = normalize(security)

    return {
        "parameters": parameters,
        "requestBodyRequired": request_required,
        "requestBody": request_content,
        "responses": responses,
        "security": security_norm,
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


def _param_key(p: Dict[str, Any]) -> tuple:
    return (p.get("name"), p.get("in"))


def _extract_parameters(op: Dict[str, Any]) -> Dict[tuple, Dict[str, Any]]:
    out = {}
    for p in op.get("parameters", []) or []:
        if isinstance(p, dict):
            out[_param_key(p)] = p
    return out


def _extract_request_content(op: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    rb = op.get("requestBody") or {}
    return rb.get("content") or {}


def _extract_response_content(op: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out = {}
    for status, resp in (op.get("responses") or {}).items():
        out[str(status)] = (resp or {}).get("content") or {}
    return out


def _schema_hash(schema: Any) -> str:
    if schema is None:
        return ""
    return schema_signature(schema)


def operation_breaking_change(old_op: Dict[str, Any], new_op: Dict[str, Any]) -> bool:
    old_params = _extract_parameters(old_op)
    new_params = _extract_parameters(new_op)

    # New required parameter is breaking
    for key, new_p in new_params.items():
        old_p = old_params.get(key)
        if old_p is None and bool(new_p.get("required", False)):
            return True

    # Existing optional -> required is breaking
    for key, old_p in old_params.items():
        new_p = new_params.get(key)
        if new_p is None:
            continue
        if not bool(old_p.get("required", False)) and bool(new_p.get("required", False)):
            return True

    # Request body becoming required is breaking
    old_rb = old_op.get("requestBody") or {}
    new_rb = new_op.get("requestBody") or {}
    if not bool(old_rb.get("required", False)) and bool(new_rb.get("required", False)):
        return True

    # Request content removed or request schema changed: conservatively breaking
    old_req = _extract_request_content(old_op)
    new_req = _extract_request_content(new_op)

    for ct in old_req:
        if ct not in new_req:
            return True

    for ct, old_desc in old_req.items():
        if ct in new_req:
            old_schema = _schema_hash((old_desc or {}).get("schema"))
            new_schema = _schema_hash((new_req[ct] or {}).get("schema"))
            if old_schema != new_schema:
                return True

    # Response status/media type removed or response schema changed: conservatively breaking
    old_resp = _extract_response_content(old_op)
    new_resp = _extract_response_content(new_op)

    for status, old_content in old_resp.items():
        if status not in new_resp:
            return True
        for ct in old_content:
            if ct not in new_resp[status]:
                return True
            old_schema = _schema_hash((old_content[ct] or {}).get("schema"))
            new_schema = _schema_hash((new_resp[status][ct] or {}).get("schema"))
            if old_schema != new_schema:
                return True

    # Security requirement change is conservatively breaking
    if normalize(old_op.get("security") or []) != normalize(new_op.get("security") or []):
        return True

    return False


def breaking_summary(old_spec: Dict[str, Any], new_spec: Dict[str, Any], diff: Dict[str, List[str]]) -> Dict[str, List[str]]:
    old_ops = flatten_paths(old_spec)
    new_ops = flatten_paths(new_spec)

    breaking = {
        "removed_operations": sorted(diff["removed"]),
        "breaking_changed_operations": [],
        "non_breaking_changed_operations": [],
        "added_operations": sorted(diff["added"]),
    }

    for op_key in diff["changed"]:
        if operation_breaking_change(old_ops.get(op_key, {}), new_ops.get(op_key, {})):
            breaking["breaking_changed_operations"].append(op_key)
        else:
            breaking["non_breaking_changed_operations"].append(op_key)

    return breaking


def classify_change(
    old_spec: Dict[str, Any],
    new_spec: Dict[str, Any],
    old_hash: str,
    new_hash: str,
) -> Tuple[str, Dict[str, Any]]:
    if old_hash == new_hash:
        return "no_change", {
            "file_changed": False,
            "api_changed": False,
            "breaking_changed": False,
            "diff": {"added": [], "removed": [], "changed": []},
            "breaking": {
                "removed_operations": [],
                "breaking_changed_operations": [],
                "non_breaking_changed_operations": [],
                "added_operations": [],
            },
        }

    old_contract_hash = sha256(canonical_contract_json(old_spec or {}))
    new_contract_hash = sha256(canonical_contract_json(new_spec or {}))

    diff = diff_specs(old_spec or {}, new_spec or {})
    api_changed = old_contract_hash != new_contract_hash and bool(diff["added"] or diff["removed"] or diff["changed"])

    if old_contract_hash == new_contract_hash or not api_changed:
        return "docs_only", {
            "file_changed": True,
            "api_changed": False,
            "breaking_changed": False,
            "diff": {"added": [], "removed": [], "changed": []},
            "breaking": {
                "removed_operations": [],
                "breaking_changed_operations": [],
                "non_breaking_changed_operations": [],
                "added_operations": [],
            },
        }

    breaking = breaking_summary(old_spec or {}, new_spec or {}, diff)
    breaking_changed = bool(
        breaking["removed_operations"] or breaking["breaking_changed_operations"]
    )

    return (
        "breaking" if breaking_changed else "non_breaking",
        {
            "file_changed": True,
            "api_changed": True,
            "breaking_changed": breaking_changed,
            "diff": diff,
            "breaking": breaking,
        },
    )


def classify_drift(left_spec: Dict[str, Any], right_spec: Dict[str, Any], diff: Dict[str, List[str]]) -> str:
    if not (diff["added"] or diff["removed"] or diff["changed"]):
        return "aligned"

    breaking = breaking_summary(left_spec or {}, right_spec or {}, diff)
    is_breaking = bool(breaking["removed_operations"] or breaking["breaking_changed_operations"])
    return "breaking" if is_breaking else "non_breaking"


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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, obj: Any) -> None:
    write_text(path, json.dumps(obj, ensure_ascii=False, indent=2))


def load_previous_spec(ep_dir: Path) -> Optional[Dict[str, Any]]:
    path = ep_dir / "latest.normalized.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def save_current_spec(ep_dir: Path, raw_text: str, normalized_obj: Dict[str, Any], digest: str, svc: ResolvedService) -> str:
    ts = now_utc().strftime("%Y%m%dT%H%M%SZ")
    snapshots = ep_dir / "snapshots"
    ensure_dir(snapshots)

    write_text(ep_dir / "latest.raw.txt", raw_text)
    write_json(ep_dir / "latest.normalized.json", normalized_obj)
    write_text(ep_dir / "latest.sha256", digest)
    write_json(
        ep_dir / "meta.json",
        {
            "service_name": svc.service_name,
            "environment": svc.environment,
            "swagger_url": svc.swagger_url,
            "docs_url": svc.docs_url,
        },
    )

    write_text(snapshots / f"{ts}.raw.txt", raw_text)
    write_json(snapshots / f"{ts}.normalized.json", normalized_obj)
    write_text(snapshots / f"{ts}.sha256", digest)
    return ts


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


def build_change_report(
    svc: ResolvedService,
    diff: Dict[str, List[str]],
    old_hash: str,
    new_hash: str,
    status: str,
    breaking: Dict[str, List[str]],
    fetched_at: str,
    duration_ms: int,
) -> str:
    lines = [
        f"# Swagger/OpenAPI change detected: {svc.key}",
        "",
        f"- Time: {now_iso()}",
        f"- Fetch completed at: {fetched_at}",
        f"- Fetch duration ms: {duration_ms}",
        f"- Swagger URL: {svc.swagger_url}",
        f"- Previous hash: `{old_hash}`",
        f"- Current hash: `{new_hash}`",
        "",
        "## Summary",
        f"- Status: {status}",
        f"- Added operations: {len(diff['added'])}",
        f"- Removed operations: {len(diff['removed'])}",
        f"- Changed operations: {len(diff['changed'])}",
        f"- Breaking removed operations: {len(breaking['removed_operations'])}",
        f"- Breaking changed operations: {len(breaking['breaking_changed_operations'])}",
        f"- Non-breaking changed operations: {len(breaking['non_breaking_changed_operations'])}",
        "",
    ]

    for section in ["added", "removed", "changed"]:
        lines.append(f"## {section.capitalize()}")
        items = diff[section]
        lines.extend([f"- {item}" for item in items] if items else ["- None"])
        lines.append("")

    lines.append("## Breaking classification")
    lines.append(f"- Removed operations: {len(breaking['removed_operations'])}")
    lines.extend([f"  - {x}" for x in breaking["removed_operations"]] if breaking["removed_operations"] else ["- None"])
    lines.append("")
    lines.append(f"- Breaking changed operations: {len(breaking['breaking_changed_operations'])}")
    lines.extend(
        [f"  - {x}" for x in breaking["breaking_changed_operations"]]
        if breaking["breaking_changed_operations"]
        else ["- None"]
    )
    lines.append("")
    lines.append(f"- Non-breaking changed operations: {len(breaking['non_breaking_changed_operations'])}")
    lines.extend(
        [f"  - {x}" for x in breaking["non_breaking_changed_operations"]]
        if breaking["non_breaking_changed_operations"]
        else ["- None"]
    )
    lines.append("")

    return "\n".join(lines).strip() + "\n"


def build_docs_only_report(svc: ResolvedService, old_hash: str, new_hash: str, fetched_at: str, duration_ms: int) -> str:
    return (
        f"# Documentation-only change detected: {svc.key}\n\n"
        f"- Time: {now_iso()}\n"
        f"- Fetch completed at: {fetched_at}\n"
        f"- Fetch duration ms: {duration_ms}\n"
        f"- Swagger URL: {svc.swagger_url}\n"
        f"- Previous hash: `{old_hash}`\n"
        f"- Current hash: `{new_hash}`\n\n"
        f"No contract-level API changes were detected.\n"
    )


def build_drift_report(
    service_name: str,
    left_env: str,
    right_env: str,
    left_url: str,
    right_url: str,
    diff: Dict[str, List[str]],
    left_hash: str,
    right_hash: str,
    severity: str,
) -> str:
    lines = [
        f"# {left_env} vs {right_env} drift detected: {service_name}",
        "",
        f"- Time: {now_iso()}",
        f"- Severity: {severity}",
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


def summarize_change_for_slack(
    svc: ResolvedService,
    diff: Dict[str, List[str]],
    status: str,
    breaking: Dict[str, List[str]],
) -> str:
    summary = (
        f"Swagger update in *{svc.key}* | "
        f"status={status} | "
        f"added={len(diff['added'])} | removed={len(diff['removed'])} | changed={len(diff['changed'])}"
    )
    preview = []
    preview += [f"+ {x}" for x in diff["added"][:3]]
    preview += [f"- {x}" for x in diff["removed"][:3]]
    preview += [f"~ {x}" for x in diff["changed"][:3]]

    if breaking["removed_operations"]:
        preview += [f"BREAK removed: {x}" for x in breaking["removed_operations"][:2]]
    if breaking["breaking_changed_operations"]:
        preview += [f"BREAK changed: {x}" for x in breaking["breaking_changed_operations"][:2]]

    return summary + (("\n" + "\n".join(preview)) if preview else "")


def summarize_drift_for_slack(service_name: str, left_env: str, right_env: str, diff: Dict[str, List[str]], severity: str) -> str:
    summary = (
        f"{left_env} vs {right_env} drift in *{service_name}* | "
        f"severity={severity} | "
        f"only_{left_env.lower()}={len(diff['added'])} | only_{right_env.lower()}={len(diff['removed'])} | different={len(diff['changed'])}"
    )
    preview = []
    preview += [f"{left_env}-only: {x}" for x in diff["added"][:2]]
    preview += [f"{right_env}-only: {x}" for x in diff["removed"][:2]]
    preview += [f"DIFF: {x}" for x in diff["changed"][:2]]
    return summary + (("\n" + "\n".join(preview)) if preview else "")


def should_alert_change(status: str) -> bool:
    return status == "breaking"


def should_alert_drift(status: str) -> bool:
    return status in {"drift_changed"}


def check_service_change(svc: ResolvedService, state_dir: Path) -> EnvCheckResult:
    ep_dir = endpoint_dir(state_dir, svc.key)

    started = time.perf_counter()
    raw_text, parsed = fetch_spec(svc.swagger_url)
    fetched_at = now_iso()
    duration_ms = int((time.perf_counter() - started) * 1000)

    if not isinstance(parsed, dict):
        raise RuntimeError(f"Parsed spec for {svc.key} is not an object")

    normalized = normalize(parsed)
    new_hash = sha256(canonical_json(normalized))
    old_hash = (read_text(ep_dir / "latest.sha256") or "").strip()
    old_spec = load_previous_spec(ep_dir)

    save_current_spec(ep_dir, raw_text, normalized, new_hash, svc)

    if not old_hash:
        report = (
            f"Initialized baseline for {svc.key} at {now_iso()}\n"
            f"Fetch completed at: {fetched_at}\n"
            f"Fetch duration ms: {duration_ms}\n"
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
            fetched_at=fetched_at,
            duration_ms=duration_ms,
        )

    status, meta = classify_change(old_spec or {}, normalized, old_hash, new_hash)

    if status == "no_change":
        report = f"No change for {svc.key} ({new_hash[:12]})\nFetch completed at: {fetched_at}\nFetch duration ms: {duration_ms}\n"
        write_text(ep_dir / "last_report.md", report)
        return EnvCheckResult(
            service_name=svc.service_name,
            environment=svc.environment,
            swagger_url=svc.swagger_url,
            status="no_change",
            summary=f"No change ({new_hash[:12]})",
            report=report,
            spec=normalized,
            spec_hash=new_hash,
            counts={"added": 0, "removed": 0, "changed": 0},
            changed_items={"added": [], "removed": [], "changed": []},
            file_changed=False,
            api_changed=False,
            breaking_changed=False,
            fetched_at=fetched_at,
            duration_ms=duration_ms,
        )

    if status == "docs_only":
        report = build_docs_only_report(svc, old_hash, new_hash, fetched_at, duration_ms)
        write_text(ep_dir / "last_report.md", report)
        return EnvCheckResult(
            service_name=svc.service_name,
            environment=svc.environment,
            swagger_url=svc.swagger_url,
            status="docs_only",
            summary="File changed, API unchanged",
            report=report,
            spec=normalized,
            spec_hash=new_hash,
            counts={"added": 0, "removed": 0, "changed": 0},
            changed_items={"added": [], "removed": [], "changed": []},
            file_changed=True,
            api_changed=False,
            breaking_changed=False,
            fetched_at=fetched_at,
            duration_ms=duration_ms,
        )

    diff = meta["diff"]
    breaking = meta["breaking"]

    report = build_change_report(svc, diff, old_hash, new_hash, status, breaking, fetched_at, duration_ms)
    write_text(ep_dir / "last_report.md", report)

    if should_alert_change(status):
        send_slack(summarize_change_for_slack(svc, diff, status, breaking))

    return EnvCheckResult(
        service_name=svc.service_name,
        environment=svc.environment,
        swagger_url=svc.swagger_url,
        status=status,
        summary=(
            f"{status.replace('_', ' ').title()}: "
            f"+{len(diff['added'])} / -{len(diff['removed'])} / ~{len(diff['changed'])}"
        ),
        report=report,
        spec=normalized,
        spec_hash=new_hash,
        counts={
            "added": len(diff["added"]),
            "removed": len(diff["removed"]),
            "changed": len(diff["changed"]),
        },
        changed_items=diff,
        file_changed=True,
        api_changed=True,
        breaking_changed=bool(breaking["removed_operations"] or breaking["breaking_changed_operations"]),
        fetched_at=fetched_at,
        duration_ms=duration_ms,
    )


def failed_env_result(svc: ResolvedService, error: Exception, duration_ms: int = 0) -> EnvCheckResult:
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
        fetched_at=now_iso(),
        duration_ms=duration_ms,
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
    severity = classify_drift(right_spec, left_spec, diff)

    drift_payload = {
        f"only_in_{left_env.lower()}": diff["added"],
        f"only_in_{right_env.lower()}": diff["removed"],
        "different": diff["changed"],
        "severity": severity,
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
            severity="aligned",
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
        severity=severity,
    )
    write_text(svc_dir / "last_drift_report.md", report)
    write_text(latest_drift_hash_path, drift_hash)

    status = "drift" if previous_drift_hash == drift_hash else "drift_changed"

    if should_alert_drift(status):
        send_slack(summarize_drift_for_slack(service_name, left_env, right_env, diff, severity))

    return DriftCheckResult(
        service_name=service_name,
        pair_name=pair_name,
        left_env=left_env,
        right_env=right_env,
        status=status,
        severity=severity,
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
        severity="error",
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
        "breaking": "bad",
        "non_breaking": "warn",
        "docs_only": "info",
        "baseline": "info",
        "no_change": "ok",
        "aligned": "ok",
        "drift": "warn",
        "drift_changed": "warn",
        "error": "bad",
    }.get(status, "info")


def severity_badge_class(severity: str) -> str:
    return {
        "aligned": "ok",
        "non_breaking": "warn",
        "breaking": "bad",
        "error": "bad",
    }.get(severity, "info")


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def list_to_html(items: List[str], empty_label: str = "None") -> str:
    if not items:
        return f"<div class=\"muted\">{esc(empty_label)}</div>"
    lis = "".join(f"<li><code>{esc(item)}</code></li>" for item in items)
    return f"<ul>{lis}</ul>"


def render_env_panel(result: Optional[EnvCheckResult], title: str) -> str:
    if result is None:
        return (
            f'<section class="panel env-panel" data-status="not_configured" data-env="{esc(title)}">'
            f'<h3>{esc(title)}</h3><div class="muted">Not configured</div></section>'
        )

    counts = result.counts
    added_html = list_to_html(result.changed_items.get("added", []))
    removed_html = list_to_html(result.changed_items.get("removed", []))
    changed_html = list_to_html(result.changed_items.get("changed", []))

    return f"""
    <section class="panel env-panel" data-status="{esc(result.status)}" data-env="{esc(result.environment)}">
      <div class="panel-head">
        <h3>{esc(title)}</h3>
        <span class="badge {status_badge_class(result.status)}">{esc(result.status.replace('_', ' '))}</span>
      </div>
      <div class="kv"><span>URL</span><a href="{esc(result.swagger_url)}" target="_blank" rel="noreferrer">{esc(result.swagger_url)}</a></div>
      <div class="kv"><span>Hash</span><code>{esc(result.spec_hash[:12] if result.spec_hash else '')}</code></div>
      <div class="kv"><span>Summary</span><strong>{esc(result.summary)}</strong></div>
      <div class="kv"><span>Fetched</span><span>{esc(result.fetched_at or '-')}</span></div>
      <div class="kv"><span>Duration</span><span>{result.duration_ms} ms</span></div>
      <div class="stats">
        <div class="stat"><span>Added</span><strong>{counts.get('added', 0)}</strong></div>
        <div class="stat"><span>Removed</span><strong>{counts.get('removed', 0)}</strong></div>
        <div class="stat"><span>Changed</span><strong>{counts.get('changed', 0)}</strong></div>
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
    <section class="panel drift drift-panel" data-status="{esc(result.status)}" data-severity="{esc(result.severity)}">
      <div class="panel-head">
        <h3>{esc(result.pair_name)}</h3>
        <div class="badge-row">
          <span class="badge {status_badge_class(result.status)}">{esc(result.status.replace('_', ' '))}</span>
          <span class="badge {severity_badge_class(result.severity)}">{esc(result.severity.replace('_', ' '))}</span>
        </div>
      </div>
      <div class="kv"><span>{esc(result.left_env)}</span><a href="{esc(result.left_url)}" target="_blank" rel="noreferrer">{esc(result.left_url)}</a></div>
      <div class="kv"><span>{esc(result.right_env)}</span><a href="{esc(result.right_url)}" target="_blank" rel="noreferrer">{esc(result.right_url)}</a></div>
      <div class="stats">
        <div class="stat"><span>Only in {esc(result.left_env)}</span><strong>{result.counts.get(only_left_key, 0)}</strong></div>
        <div class="stat"><span>Only in {esc(result.right_env)}</span><strong>{result.counts.get(only_right_key, 0)}</strong></div>
        <div class="stat"><span>Different</span><strong>{result.counts.get('different', 0)}</strong></div>
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
    partial_failure_count = 0

    for row in rows:
        row_has_error = False

        for env_name in ENV_ORDER:
            env_result = row.env_results.get(env_name)
            if env_result and env_result.status in {"breaking", "non_breaking", "docs_only"}:
                changed_count += 1
            if env_result and env_result.status == "error":
                error_count += 1
                row_has_error = True

        for drift in row.drift_results:
            if drift.status in {"drift", "drift_changed"}:
                drift_count += 1
            if drift.status == "error":
                error_count += 1
                row_has_error = True

        if row_has_error:
            partial_failure_count += 1

        env_panels = "".join(render_env_panel(row.env_results.get(env_name), env_name) for env_name in ENV_ORDER)
        drift_panels = "".join(render_drift_panel(drift) for drift in row.drift_results)

        statuses = []
        for env_name in ENV_ORDER:
            env_result = row.env_results.get(env_name)
            if env_result:
                statuses.append(env_result.status)
        data_statuses = ",".join(statuses)

        service_cards.append(
            f"""
            <article class="service-card service-item" data-service="{esc(row.service_name.lower())}" data-statuses="{esc(data_statuses)}">
              <div class="service-head">
                <h2>{esc(row.service_name)}</h2>
              </div>
              <div class="grid env-grid">{env_panels}</div>
              <div class="grid drift-grid">{drift_panels}</div>
            </article>
            """
        )

    git_sha = os.getenv("GITHUB_SHA", "").strip()
    git_repo = os.getenv("GITHUB_REPOSITORY", "").strip()
    git_run_id = os.getenv("GITHUB_RUN_ID", "").strip()
    git_server = os.getenv("GITHUB_SERVER_URL", "https://github.com").strip()
    retention = retention_days()
    timeout = request_timeout()
    fail_on_errors = bool_env("FAIL_ON_SERVICE_ERRORS", False)
    run_url = f"{git_server}/{git_repo}/actions/runs/{git_run_id}" if git_repo and git_run_id else ""

    html_doc = f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
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
    .topnav {{ display: flex; gap: 12px; margin-bottom: 18px; flex-wrap: wrap; }}
    .topnav a {{ background: rgba(255,255,255,.05); border: 1px solid var(--border); border-radius: 10px; padding: 8px 12px; text-decoration: none; }}
    .hero {{ display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 24px; }}
    .hero h1 {{ margin: 0 0 6px; font-size: 32px; }}
    .muted {{ color: var(--muted); }}
    .summary {{ display: grid; grid-template-columns: repeat(5, minmax(140px, 1fr)); gap: 12px; margin: 20px 0 20px; }}
    .summary .card, .panel, .service-card, .legend, .filters {{ background: var(--card); border: 1px solid var(--border); border-radius: 18px; box-shadow: 0 10px 30px rgba(0,0,0,.18); }}
    .summary .card {{ padding: 16px; }}
    .summary .card span {{ display: block; color: var(--muted); font-size: 13px; margin-bottom: 6px; }}
    .summary .card strong {{ font-size: 28px; }}
    .legend, .filters {{ padding: 16px; margin-bottom: 18px; }}
    .legend h3, .filters h3 {{ margin: 0 0 10px; font-size: 18px; }}
    .legend-grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(280px, 1fr));
      gap: 10px 16px;
    }}
    .legend-item {{
      background: rgba(255,255,255,.03);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 12px;
    }}
    .legend-item p {{ margin: 8px 0 0; color: var(--muted); font-size: 14px; line-height: 1.45; }}
    .filter-row {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 12px;
    }}
    .filter-row input, .filter-row select {{
      width: 100%;
      background: rgba(255,255,255,.04);
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 12px;
    }}
    .service-card {{ padding: 18px; margin-bottom: 18px; }}
    .service-head {{ margin-bottom: 14px; }}
    .service-head h2 {{ margin: 0; font-size: 24px; }}
    .grid {{ display: grid; gap: 14px; }}
    .env-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); margin-bottom: 14px; }}
    .drift-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .panel {{ padding: 16px; min-width: 0; }}
    .panel-head {{ display: flex; justify-content: space-between; gap: 10px; align-items: center; margin-bottom: 12px; }}
    .panel h3 {{ margin: 0; font-size: 18px; }}
    .badge-row {{ display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }}
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
    .hidden {{ display: none !important; }}
    @media (max-width: 1300px) {{
      .env-grid, .drift-grid, .filter-row {{ grid-template-columns: 1fr; }}
      .summary {{ grid-template-columns: repeat(2, minmax(140px, 1fr)); }}
      .legend-grid {{ grid-template-columns: 1fr; }}
    }}
    @media (max-width: 640px) {{
      .hero {{ display: block; }}
      .summary {{ grid-template-columns: 1fr; }}
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
        <h1>EG Retail Swagger Dashboard</h1>
        <div class="muted">Generated at {esc(now_iso())}</div>
      </div>
      <div class="muted">Output: {esc(str(output_path))}</div>
    </section>

    <section class="summary">
      <div class="card"><span>Services</span><strong>{len(rows)}</strong></div>
      <div class="card"><span>Env updates</span><strong>{changed_count}</strong></div>
      <div class="card"><span>Drifts</span><strong>{drift_count}</strong></div>
      <div class="card"><span>Errors</span><strong>{error_count}</strong></div>
      <div class="card"><span>Partial failures</span><strong>{partial_failure_count}</strong></div>
    </section>

    <section class="legend">
      <h3>Classification guide</h3>
      <div class="legend-grid">
        <div class="legend-item">
          <span class="badge ok">no change</span>
          <p>The fetched spec matched the previous snapshot exactly after normalization.</p>
        </div>
        <div class="legend-item">
          <span class="badge info">docs only</span>
          <p>The file changed, but only documentation or metadata changed. No contract-level API change was detected.</p>
        </div>
        <div class="legend-item">
          <span class="badge warn">non breaking</span>
          <p>The API contract changed, but the change appears additive or otherwise backward compatible.</p>
        </div>
        <div class="legend-item">
          <span class="badge bad">breaking</span>
          <p>The API contract changed in a way that may break existing consumers, such as removed operations, removed response shapes, stricter input requirements, or incompatible schema changes.</p>
        </div>
        <div class="legend-item">
          <span class="badge ok">aligned</span>
          <p>Compared environments are contract-aligned after metadata-light normalization.</p>
        </div>
        <div class="legend-item">
          <span class="badge warn">drift severity</span>
          <p>Cross-environment drift is labeled as non-breaking or breaking using the same contract-focused comparison model.</p>
        </div>
      </div>
      <p class="muted" style="margin-top: 12px;">
        Metadata such as descriptions, summaries, examples, tag descriptions, external docs, and similar non-contract fields are intentionally de-emphasized to reduce false positives.
      </p>
    </section>

    <section class="filters">
      <h3>Filters</h3>
      <div class="filter-row">
        <input id="serviceFilter" type="text" placeholder="Filter by service name..." />
        <select id="envStatusFilter">
          <option value="">All env statuses</option>
          <option value="breaking">breaking</option>
          <option value="non_breaking">non_breaking</option>
          <option value="docs_only">docs_only</option>
          <option value="no_change">no_change</option>
          <option value="baseline">baseline</option>
          <option value="error">error</option>
        </select>
        <select id="driftSeverityFilter">
          <option value="">All drift severities</option>
          <option value="breaking">breaking</option>
          <option value="non_breaking">non_breaking</option>
          <option value="aligned">aligned</option>
          <option value="error">error</option>
        </select>
      </div>
      <p class="muted" style="margin-top: 10px;">
        Commit: {esc(git_sha[:12] if git_sha else '-')} |
        Retention: {retention} days |
        Timeout: {timeout}s |
        Fail on service errors: {str(fail_on_errors).lower()} |
        Run: {f'<a href="{esc(run_url)}" target="_blank" rel="noreferrer">{esc(git_run_id)}</a>' if run_url else '-'}
      </p>
    </section>

    <div id="services">
      {''.join(service_cards)}
    </div>
  </div>

  <script>
    (function() {{
      const serviceFilter = document.getElementById('serviceFilter');
      const envStatusFilter = document.getElementById('envStatusFilter');
      const driftSeverityFilter = document.getElementById('driftSeverityFilter');
      const cards = Array.from(document.querySelectorAll('.service-item'));

      function applyFilters() {{
        const serviceNeedle = (serviceFilter.value || '').trim().toLowerCase();
        const envNeedle = envStatusFilter.value || '';
        const driftNeedle = driftSeverityFilter.value || '';

        cards.forEach(card => {{
          const serviceName = card.dataset.service || '';
          const envPanels = Array.from(card.querySelectorAll('.env-panel'));
          const driftPanels = Array.from(card.querySelectorAll('.drift-panel'));

          const matchesService = !serviceNeedle || serviceName.includes(serviceNeedle);
          const matchesEnv = !envNeedle || envPanels.some(p => (p.dataset.status || '') === envNeedle);
          const matchesDrift = !driftNeedle || driftPanels.some(p => (p.dataset.severity || '') === driftNeedle);

          card.classList.toggle('hidden', !(matchesService && matchesEnv && matchesDrift));
        }});
      }}

      serviceFilter.addEventListener('input', applyFilters);
      envStatusFilter.addEventListener('change', applyFilters);
      driftSeverityFilter.addEventListener('change', applyFilters);
      applyFilters();
    }})();
  </script>
</body>
</html>
    """.strip()

    write_text(output_path, html_doc + "\n")


def parse_snapshot_timestamp(ts: str) -> Optional[datetime]:
    for fmt in ("%Y%m%dT%H%M%SZ", "%Y%m%dT%H%M%S", "%Y-%m-%dT%H:%M:%SZ"):
        try:
            return datetime.strptime(ts, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    return None


def retention_days() -> int:
    return int(os.getenv("RETENTION_DAYS", "180"))


def prune_old_snapshots(state_dir: Path) -> List[str]:
    cutoff = now_utc() - timedelta(days=retention_days())
    removed: List[str] = []

    for child in state_dir.iterdir() if state_dir.exists() else []:
        if not child.is_dir():
            continue

        snapshots_dir = child / "snapshots"
        if not snapshots_dir.exists():
            continue

        grouped: Dict[str, List[Path]] = {}
        for p in snapshots_dir.iterdir():
            name = p.name
            ts = None
            for suffix in [".raw.txt", ".normalized.json", ".sha256"]:
                if name.endswith(suffix):
                    ts = name[: -len(suffix)]
                    break
            if ts:
                grouped.setdefault(ts, []).append(p)

        for ts, files in grouped.items():
            dt = parse_snapshot_timestamp(ts)
            if dt is None:
                continue
            if dt < cutoff:
                for f in files:
                    if f.exists():
                        f.unlink()
                removed.append(f"{child.name}/{ts}")

    history_reports_dir = state_dir / "history_reports"
    if history_reports_dir.exists():
        for p in history_reports_dir.iterdir():
            if not p.is_file():
                continue
            m = re.search(r"_(\d{8}T\d{6}Z)_vs_(\d{8}T\d{6}Z)\.", p.name)
            if not m:
                continue
            right_dt = parse_snapshot_timestamp(m.group(2))
            if right_dt and right_dt < cutoff:
                p.unlink()
                removed.append(f"history_reports/{p.name}")

    return removed


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
    fail_on_service_errors = bool_env("FAIL_ON_SERVICE_ERRORS", False)
    dashboard_rows: List[DashboardServiceRow] = []
    print(f"Loaded {len(resolved)} service-environment specs from DIRECT_SPECS_JSON")

    for service_name in sorted(grouped):
        envs = grouped[service_name]
        env_results: Dict[str, Optional[EnvCheckResult]] = {env: None for env in ENV_ORDER}
        drift_results: List[DriftCheckResult] = []

        futures = {}
        max_workers = max(1, min(3, sum(1 for env in ENV_ORDER if envs.get(env) is not None)))

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for env_name in ENV_ORDER:
                svc = envs.get(env_name)
                if svc is None:
                    continue
                futures[executor.submit(check_service_change, svc, state_dir)] = (env_name, svc)

            for future in as_completed(futures):
                env_name, svc = futures[future]
                try:
                    result = future.result()
                    env_results[env_name] = result
                    print(result.report.strip())
                    print("-" * 80)
                except Exception as exc:
                    if fail_on_service_errors:
                        exit_code = 1
                    env_results[env_name] = failed_env_result(svc, exc)
                    print(f"ERROR while checking {svc.key}: {exc}", file=sys.stderr)
                    if os.getenv("SLACK_WEBHOOK_URL", "").strip():
                        try:
                            send_slack(f"Swagger fetch failed in *{svc.key}*: {exc}")
                        except Exception as slack_exc:
                            print(f"ERROR while sending Slack failure notification for {svc.key}: {slack_exc}", file=sys.stderr)

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
                    if fail_on_service_errors:
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

    removed_items = prune_old_snapshots(state_dir)
    if removed_items:
        print(f"Pruned {len(removed_items)} old snapshot items")

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