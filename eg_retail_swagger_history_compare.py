#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options", "trace"}
IGNORED_KEYS = {"description", "summary", "externalDocs", "example", "examples", "title", "servers", "operationId", "tags"}


@dataclass
class SnapshotInfo:
    timestamp: str
    normalized_path: Path
    hash_path: Path


def safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_").lower()


def endpoint_dir(state_dir: Path, service_name: str, environment: str) -> Path:
    return state_dir / safe_name(f"{service_name} [{environment}]")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize(obj: Any) -> Any:
    if isinstance(obj, dict):
        out = {}
        for k, v in sorted(obj.items(), key=lambda kv: str(kv[0])):
            if str(k) in IGNORED_KEYS:
                continue
            out[str(k)] = normalize(v)
        return out
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    return obj


def canonical_json(obj: Any) -> str:
    return json.dumps(normalize(obj), ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def schema_signature(schema: Any) -> str:
    return sha256(canonical_json(schema))[:12] if schema is not None else ""


def flatten_paths(spec: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    out: Dict[str, Dict[str, Any]] = {}
    for path, methods in (spec.get("paths") or {}).items():
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
        if isinstance(p, dict):
            parameters.append({
                "name": p.get("name"),
                "in": p.get("in"),
                "required": p.get("required"),
                "schema": schema_signature(p.get("schema")),
            })

    request_content = {
        ct: schema_signature((desc or {}).get("schema"))
        for ct, desc in sorted(((op.get("requestBody") or {}).get("content") or {}).items())
    }

    responses = {}
    for status, resp in sorted((op.get("responses") or {}).items(), key=lambda x: str(x[0])):
        responses[str(status)] = {
            ct: schema_signature((desc or {}).get("schema"))
            for ct, desc in sorted(((resp or {}).get("content") or {}).items())
        }

    return {
        "parameters": sorted(parameters, key=lambda x: (str(x.get("in")), str(x.get("name")))),
        "requestBody": request_content,
        "responses": responses,
        "security": normalize(op.get("security") or []),
        "deprecated": bool(op.get("deprecated", False)),
    }


def diff_specs(old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, List[str]]:
    old_ops = flatten_paths(old)
    new_ops = flatten_paths(new)
    old_keys = set(old_ops)
    new_keys = set(new_ops)
    return {
        "added": sorted(new_keys - old_keys),
        "removed": sorted(old_keys - new_keys),
        "changed": [k for k in sorted(old_keys & new_keys) if operation_signature(old_ops[k]) != operation_signature(new_ops[k])],
    }


def classify_diff(diff: Dict[str, List[str]]) -> str:
    if not diff["added"] and not diff["removed"] and not diff["changed"]:
        return "no_change"
    if diff["removed"]:
        return "breaking"
    return "non_breaking"


def load_snapshots(state_dir: Path, service_name: str, environment: str) -> List[SnapshotInfo]:
    snapshots_dir = endpoint_dir(state_dir, service_name, environment) / "snapshots"
    if not snapshots_dir.exists():
        raise FileNotFoundError(f"No snapshots directory found: {snapshots_dir}")

    found: Dict[str, Dict[str, Path]] = {}
    for p in snapshots_dir.iterdir():
        if p.name.endswith(".normalized.json"):
            found.setdefault(p.name[:-16], {})["normalized"] = p
        elif p.name.endswith(".sha256"):
            found.setdefault(p.name[:-7], {})["hash"] = p

    snapshots = [
        SnapshotInfo(timestamp=ts, normalized_path=parts["normalized"], hash_path=parts["hash"])
        for ts, parts in sorted(found.items())
        if "normalized" in parts and "hash" in parts
    ]
    if not snapshots:
        raise FileNotFoundError(f"No usable snapshots found in {snapshots_dir}")
    return snapshots


def resolve_snapshot(snapshots: List[SnapshotInfo], selector: str) -> SnapshotInfo:
    if selector == "earliest":
        return snapshots[0]
    if selector == "latest":
        return snapshots[-1]
    matches = [s for s in snapshots if s.timestamp.startswith(selector)]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        raise ValueError(f"No snapshot matched selector: {selector}")
    raise ValueError(f"Ambiguous selector {selector}; matches: {', '.join(s.timestamp for s in matches)}")


def build_report(service: str, env: str, left: SnapshotInfo, right: SnapshotInfo, diff: Dict[str, List[str]]) -> str:
    classification = classify_diff(diff)
    lines = [
        f"# Historical Swagger compare: {service} [{env}]",
        "",
        f"- From: `{left.timestamp}`",
        f"- To: `{right.timestamp}`",
        f"- Classification: `{classification}`",
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


def cmd_list(args: argparse.Namespace) -> int:
    for s in load_snapshots(Path(args.state_dir), args.service, args.env.upper()):
        print(s.timestamp)
    return 0


def cmd_compare(args: argparse.Namespace) -> int:
    state_dir = Path(args.state_dir)
    env = args.env.upper()
    snapshots = load_snapshots(state_dir, args.service, env)
    left = resolve_snapshot(snapshots, args.from_selector)
    right = resolve_snapshot(snapshots, args.to_selector)

    left_spec = json.loads(left.normalized_path.read_text(encoding="utf-8"))
    right_spec = json.loads(right.normalized_path.read_text(encoding="utf-8"))
    diff = diff_specs(left_spec, right_spec)
    report = build_report(args.service, env, left, right, diff)

    reports_dir = state_dir / "history_reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    base = f"{safe_name(args.service)}_{env.lower()}_{left.timestamp}_vs_{right.timestamp}"
    (reports_dir / f"{base}.md").write_text(report, encoding="utf-8")
    (reports_dir / f"{base}.json").write_text(json.dumps({
        "service_name": args.service,
        "environment": env,
        "from": left.timestamp,
        "to": right.timestamp,
        "classification": classify_diff(diff),
        "diff": diff,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(report)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Compare EG Retail Swagger snapshots from history")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List available snapshots for one service/env")
    p_list.add_argument("--state-dir", default=".swagger_watch_state")
    p_list.add_argument("--service", required=True)
    p_list.add_argument("--env", required=True)
    p_list.set_defaults(func=cmd_list)

    p_compare = sub.add_parser("compare", help="Compare two snapshots for one service/env")
    p_compare.add_argument("--state-dir", default=".swagger_watch_state")
    p_compare.add_argument("--service", required=True)
    p_compare.add_argument("--env", required=True)
    p_compare.add_argument("--from", dest="from_selector", required=True)
    p_compare.add_argument("--to", dest="to_selector", required=True)
    p_compare.set_defaults(func=cmd_compare)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
