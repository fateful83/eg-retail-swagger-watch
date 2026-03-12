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

        meta_path = child / "meta.json"
        if meta_path.exists():
            meta = load_json(meta_path)
            service_name = str(meta.get("service_name", child.name))
            env = str(meta.get("environment", ""))
        else:
            service_name, env = parse_service_env_from_dirname(child.name)

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


def safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", name).strip("_").lower()


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


def build_history_index(histories: List[ServiceEnvHistory]) -> Dict[str, Any]:
    items = []
    for history in histories:
        items.append(
            {
                "id": f"{history.service_name} [{history.environment}]",
                "service_name": history.service_name,
                "environment": history.environment,
                "directory_name": history.directory_name,
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

    for history in histories:
        snaps = history.snapshots
        if len(snaps) >= 2:
            write_compare_report(state_dir, history, snaps[0], snaps[-1])
            write_compare_report(state_dir, history, snaps[-2], snaps[-1])

    page = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>EG Retail Swagger History</title>
  <style>
    :root {
      --bg: #0b1020;
      --card: #121933;
      --muted: #9fb0d0;
      --text: #eef4ff;
      --border: #263052;
      --accent: #7cc4ff;
      --good: #153a2a;
      --warn: #4a3310;
      --bad: #4c1720;
      --info: #17324c;
    }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: Inter, Segoe UI, Arial, sans-serif; background: var(--bg); color: var(--text); }
    a { color: var(--accent); text-decoration: none; }
    a:hover { text-decoration: underline; }
    .wrap { max-width: 1500px; margin: 0 auto; padding: 24px; }
    .topnav { display: flex; gap: 12px; margin-bottom: 18px; }
    .topnav a { background: rgba(255,255,255,.05); border: 1px solid var(--border); border-radius: 10px; padding: 8px 12px; }
    .hero { display: flex; justify-content: space-between; gap: 16px; align-items: end; margin-bottom: 24px; }
    .hero h1 { margin: 0 0 6px; font-size: 32px; }
    .muted { color: var(--muted); }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 18px;
      box-shadow: 0 10px 30px rgba(0,0,0,.18);
      padding: 18px;
      margin-bottom: 18px;
    }
    .selectors {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr auto auto;
      gap: 12px;
      align-items: end;
    }
    label { display: block; margin-bottom: 6px; color: var(--muted); font-size: 13px; }
    select, button {
      width: 100%;
      background: rgba(255,255,255,.04);
      color: var(--text);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 12px;
    }
    button {
      cursor: pointer;
      background: rgba(124,196,255,.14);
    }
    .stats {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin-top: 16px;
    }
    .stat {
      background: rgba(255,255,255,.03);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 12px;
    }
    .stat span { display: block; color: var(--muted); font-size: 12px; margin-bottom: 6px; }
    .stat strong { font-size: 18px; overflow-wrap: anywhere; }
    .section-title { margin: 18px 0 8px; font-size: 18px; }
    ul { margin: 8px 0 0 18px; padding: 0; }
    li { margin: 6px 0; }
    code {
      background: rgba(255,255,255,.04);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 2px 6px;
      word-break: break-word;
    }
    .result-block { margin-top: 16px; }
    .timeline-day {
      margin-top: 18px;
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      background: rgba(255,255,255,.02);
    }
    .timeline-day summary {
      cursor: pointer;
      list-style: none;
      padding: 14px 16px;
      background: rgba(255,255,255,.03);
      border-bottom: 1px solid var(--border);
    }
    .timeline-day summary::-webkit-details-marker { display: none; }
    .day-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }
    .day-title {
      font-weight: 700;
      font-size: 16px;
    }
    .day-meta {
      color: var(--muted);
      font-size: 13px;
    }
    .day-body {
      padding: 16px;
    }
    .timeline-entry {
      background: rgba(255,255,255,.025);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 14px;
      margin-top: 14px;
    }
    .timeline-entry:first-child {
      margin-top: 0;
    }
    .timeline-head {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: center;
      margin-bottom: 10px;
      flex-wrap: wrap;
    }
    .timeline-title {
      font-weight: 700;
    }
    .badge {
      display: inline-block;
      border-radius: 999px;
      padding: 6px 10px;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .04em;
    }
    .badge.good { background: var(--good); }
    .badge.warn { background: var(--warn); }
    .badge.bad { background: var(--bad); }
    .badge.info { background: var(--info); }
    .mini-stats {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin: 10px 0 12px;
    }
    .mini-stat {
      background: rgba(255,255,255,.03);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px;
    }
    .mini-stat span { display: block; color: var(--muted); font-size: 12px; margin-bottom: 4px; }
    .mini-stat strong { font-size: 18px; }
    .columns {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
    }
    .column {
      background: rgba(255,255,255,.02);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 12px;
      min-width: 0;
    }
    .column h4 { margin: 0 0 10px; font-size: 14px; }
    .summary-note {
      margin-top: 12px;
      color: var(--muted);
      font-size: 13px;
    }
    @media (max-width: 1100px) {
      .selectors { grid-template-columns: 1fr; }
      .stats, .mini-stats, .columns { grid-template-columns: 1fr; }
    }
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
        <div class="muted">Compare two snapshots or view the full change timeline across a selected range.</div>
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
          <button id="compareBtn" type="button">Net diff</button>
        </div>
        <div>
          <label>&nbsp;</label>
          <button id="timelineBtn" type="button">Change timeline</button>
        </div>
      </div>

      <div class="stats">
        <div class="stat"><span>Snapshot count</span><strong id="countValue">-</strong></div>
        <div class="stat"><span>Earliest</span><strong id="earliestValue">-</strong></div>
        <div class="stat"><span>Latest</span><strong id="latestValue">-</strong></div>
      </div>

      <h3 class="section-title">Result</h3>
      <div id="result" class="muted">Pick a service and snapshot range, then choose Net diff or Change timeline.</div>
    </section>
  </div>

  <script>
    async function loadIndex() {
      const res = await fetch('history_index.json', { cache: 'no-store' });
      if (!res.ok) throw new Error('Could not load history_index.json');
      return res.json();
    }

    function fillSelect(select, values) {
      select.innerHTML = '';
      for (const value of values) {
        const opt = document.createElement('option');
        opt.value = value;
        opt.textContent = value;
        select.appendChild(opt);
      }
    }

    function escapeHtml(value) {
      return String(value)
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;')
        .replaceAll("'", '&#39;');
    }

    function renderList(items) {
      if (!items.length) return '<div class="muted">None</div>';
      return `<ul>${items.map(x => `<li><code>${escapeHtml(x)}</code></li>`).join('')}</ul>`;
    }

    function renderNetDiff(diff, title) {
      return `
        <div class="result-block">
          <div class="muted">${escapeHtml(title)}</div>
          <div class="stats">
            <div class="stat"><span>Added</span><strong>${diff.added.length}</strong></div>
            <div class="stat"><span>Removed</span><strong>${diff.removed.length}</strong></div>
            <div class="stat"><span>Changed</span><strong>${diff.changed.length}</strong></div>
          </div>
          <h4 class="section-title">Added</h4>
          ${renderList(diff.added)}
          <h4 class="section-title">Removed</h4>
          ${renderList(diff.removed)}
          <h4 class="section-title">Changed</h4>
          ${renderList(diff.changed)}
        </div>
      `;
    }

    function classifyDiff(diff) {
      if (!diff.added.length && !diff.removed.length && !diff.changed.length) {
        return { name: 'no change', cls: 'good' };
      }
      if (diff.removed.length > 0) {
        return { name: 'breaking', cls: 'bad' };
      }
      return { name: 'changed', cls: 'warn' };
    }

    function compareSpecs(oldSpec, newSpec) {
      const flattenPaths = (spec) => {
        const paths = spec.paths || {};
        const out = {};
        for (const [path, methods] of Object.entries(paths)) {
          if (!methods || typeof methods !== 'object') continue;
          for (const [method, op] of Object.entries(methods)) {
            const m = String(method).toLowerCase();
            if (!['get','post','put','patch','delete','head','options','trace'].includes(m)) continue;
            out[`${method.toUpperCase()} ${path}`] = op || {};
          }
        }
        return out;
      };

      const opSig = (op) => JSON.stringify(op);
      const a = flattenPaths(oldSpec);
      const b = flattenPaths(newSpec);
      const aKeys = new Set(Object.keys(a));
      const bKeys = new Set(Object.keys(b));

      const added = [...bKeys].filter(x => !aKeys.has(x)).sort();
      const removed = [...aKeys].filter(x => !bKeys.has(x)).sort();
      const changed = [...aKeys].filter(x => bKeys.has(x) && opSig(a[x]) !== opSig(b[x])).sort();

      return { added, removed, changed };
    }

    async function loadSnapshot(directoryName, timestamp) {
      const url = `${directoryName}/snapshots/${timestamp}.normalized.json`;
      const res = await fetch(url, { cache: 'no-store' });
      if (!res.ok) throw new Error(`Could not load snapshot ${timestamp}`);
      return res.json();
    }

    function makeTimelineEntry(fromTs, toTs, diff) {
      const klass = classifyDiff(diff);
      return `
        <div class="timeline-entry">
          <div class="timeline-head">
            <div class="timeline-title">${escapeHtml(fromTs)} → ${escapeHtml(toTs)}</div>
            <span class="badge ${klass.cls}">${escapeHtml(klass.name)}</span>
          </div>
          <div class="mini-stats">
            <div class="mini-stat"><span>Added</span><strong>${diff.added.length}</strong></div>
            <div class="mini-stat"><span>Removed</span><strong>${diff.removed.length}</strong></div>
            <div class="mini-stat"><span>Changed</span><strong>${diff.changed.length}</strong></div>
          </div>
          <div class="columns">
            <div class="column">
              <h4>Added</h4>
              ${renderList(diff.added)}
            </div>
            <div class="column">
              <h4>Removed</h4>
              ${renderList(diff.removed)}
            </div>
            <div class="column">
              <h4>Changed</h4>
              ${renderList(diff.changed)}
            </div>
          </div>
        </div>
      `;
    }

    function groupTimelineEntries(entries) {
      const groups = new Map();

      for (const entry of entries) {
        const day = entry.from.slice(0, 10);
        if (!groups.has(day)) {
          groups.set(day, {
            day,
            entries: [],
            totalAdded: 0,
            totalRemoved: 0,
            totalChanged: 0,
          });
        }
        const group = groups.get(day);
        group.entries.push(entry);
        group.totalAdded += entry.diff.added.length;
        group.totalRemoved += entry.diff.removed.length;
        group.totalChanged += entry.diff.changed.length;
      }

      return [...groups.values()];
    }

    function renderGroupedTimeline(groups) {
      return groups.map(group => `
        <details class="timeline-day" open>
          <summary>
            <div class="day-head">
              <div class="day-title">${escapeHtml(group.day)}</div>
              <div class="day-meta">
                ${group.entries.length} step(s) · +${group.totalAdded} / -${group.totalRemoved} / ~${group.totalChanged}
              </div>
            </div>
          </summary>
          <div class="day-body">
            ${group.entries.map(entry => makeTimelineEntry(entry.from, entry.to, entry.diff)).join('')}
          </div>
        </details>
      `).join('');
    }

    async function main() {
      const data = await loadIndex();
      const services = data.services || [];

      const serviceSelect = document.getElementById('serviceSelect');
      const fromSelect = document.getElementById('fromSelect');
      const toSelect = document.getElementById('toSelect');
      const compareBtn = document.getElementById('compareBtn');
      const timelineBtn = document.getElementById('timelineBtn');
      const result = document.getElementById('result');

      const countValue = document.getElementById('countValue');
      const earliestValue = document.getElementById('earliestValue');
      const latestValue = document.getElementById('latestValue');

      const map = new Map(services.map(s => [s.id, s]));
      fillSelect(serviceSelect, services.map(s => s.id));

      function currentService() {
        return map.get(serviceSelect.value);
      }

      function currentSnapshots() {
        return currentService()?.snapshots || [];
      }

      function refreshSnapshotSelectors() {
        const snaps = currentSnapshots().map(s => s.timestamp);

        fillSelect(fromSelect, snaps);
        fillSelect(toSelect, snaps);

        if (snaps.length > 0) {
          fromSelect.value = snaps[0];
          toSelect.value = snaps[snaps.length - 1];
          countValue.textContent = String(snaps.length);
          earliestValue.textContent = snaps[0];
          latestValue.textContent = snaps[snaps.length - 1];
        } else {
          countValue.textContent = '-';
          earliestValue.textContent = '-';
          latestValue.textContent = '-';
        }
      }

      function selectedRangeIndices() {
        const snaps = currentSnapshots();
        const fromTs = fromSelect.value;
        const toTs = toSelect.value;
        const fromIdx = snaps.findIndex(s => s.timestamp === fromTs);
        const toIdx = snaps.findIndex(s => s.timestamp === toTs);
        return { snaps, fromIdx, toIdx };
      }

      async function runNetDiff() {
        const current = currentService();
        if (!current) return;

        const { snaps, fromIdx, toIdx } = selectedRangeIndices();

        if (fromIdx < 0 || toIdx < 0) {
          result.innerHTML = '<div class="muted">Invalid snapshot selection.</div>';
          return;
        }
        if (fromIdx === toIdx) {
          result.innerHTML = '<div class="muted">Choose two different snapshots.</div>';
          return;
        }
        if (fromIdx > toIdx) {
          result.innerHTML = '<div class="muted">From must be earlier than To.</div>';
          return;
        }

        const fromTs = snaps[fromIdx].timestamp;
        const toTs = snaps[toIdx].timestamp;

        try {
          const [aSpec, bSpec] = await Promise.all([
            loadSnapshot(current.directory_name, fromTs),
            loadSnapshot(current.directory_name, toTs),
          ]);
          const diff = compareSpecs(aSpec, bSpec);
          result.innerHTML = renderNetDiff(diff, `${fromTs} → ${toTs}`);
        } catch (err) {
          result.innerHTML = `<div class="muted">Net diff failed: ${escapeHtml(err.message)}</div>`;
        }
      }

      async function runTimeline() {
        const current = currentService();
        if (!current) return;

        const { snaps, fromIdx, toIdx } = selectedRangeIndices();

        if (fromIdx < 0 || toIdx < 0) {
          result.innerHTML = '<div class="muted">Invalid snapshot selection.</div>';
          return;
        }
        if (fromIdx === toIdx) {
          result.innerHTML = '<div class="muted">Choose two different snapshots.</div>';
          return;
        }
        if (fromIdx > toIdx) {
          result.innerHTML = '<div class="muted">From must be earlier than To.</div>';
          return;
        }

        const selected = snaps.slice(fromIdx, toIdx + 1);

        try {
          const specs = await Promise.all(
            selected.map(s => loadSnapshot(current.directory_name, s.timestamp))
          );

          const entries = [];
          let totalAdded = 0;
          let totalRemoved = 0;
          let totalChanged = 0;

          for (let i = 0; i < selected.length - 1; i++) {
            const left = selected[i];
            const right = selected[i + 1];
            const diff = compareSpecs(specs[i], specs[i + 1]);

            totalAdded += diff.added.length;
            totalRemoved += diff.removed.length;
            totalChanged += diff.changed.length;

            if (diff.added.length || diff.removed.length || diff.changed.length) {
              entries.push({
                from: left.timestamp,
                to: right.timestamp,
                diff,
              });
            }
          }

          const header = `
            <div class="result-block">
              <div class="muted">${escapeHtml(selected[0].timestamp)} → ${escapeHtml(selected[selected.length - 1].timestamp)}</div>
              <div class="stats">
                <div class="stat"><span>Total added events</span><strong>${totalAdded}</strong></div>
                <div class="stat"><span>Total removed events</span><strong>${totalRemoved}</strong></div>
                <div class="stat"><span>Total changed events</span><strong>${totalChanged}</strong></div>
              </div>
              <div class="summary-note">
                This timeline shows every intermediate snapshot-to-snapshot change in the selected range, grouped by day.
              </div>
            </div>
          `;

          if (!entries.length) {
            result.innerHTML = header + '<div class="muted">No step-by-step changes were detected across the selected range.</div>';
            return;
          }

          const groups = groupTimelineEntries(entries);
          result.innerHTML = header + renderGroupedTimeline(groups);
        } catch (err) {
          result.innerHTML = `<div class="muted">Timeline failed: ${escapeHtml(err.message)}</div>`;
        }
      }

      serviceSelect.addEventListener('change', refreshSnapshotSelectors);
      refreshSnapshotSelectors();

      compareBtn.addEventListener('click', runNetDiff);
      timelineBtn.addEventListener('click', runTimeline);
    }

    main().catch(err => {
      document.getElementById('result').innerHTML = `<div class="muted">Initialization failed: ${escapeHtml(err.message)}</div>`;
    });
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