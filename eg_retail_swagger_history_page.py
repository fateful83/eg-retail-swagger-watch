#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SNAPSHOT_SUFFIX = ".normalized.json"
CLASSIFICATION_DESCRIPTIONS = {
    "no_change": "No contract-relevant change was detected.",
    "docs_only": "Only documentation-style or metadata-style content changed.",
    "non_breaking": "A contract-relevant change was found without an obvious breaking signature.",
    "breaking": "A potentially consumer-impacting contract change was found.",
}


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
        if child.name in {"history_reports", "data", "reports"} or "_vs_" in child.name:
            continue
        snapshots_dir = child / "snapshots"
        if not snapshots_dir.exists():
            continue

        found: Dict[str, Dict[str, Path]] = {}
        for p in sorted(snapshots_dir.iterdir()):
            name = p.name
            if name.endswith(SNAPSHOT_SUFFIX):
                ts = name[: -len(SNAPSHOT_SUFFIX)]
                found.setdefault(ts, {})["normalized"] = p
            elif name.endswith(".sha256"):
                ts = name[: -len(".sha256")]
                found.setdefault(ts, {})["hash"] = p

        snapshots = [
            SnapshotInfo(timestamp=ts, normalized_path=parts["normalized"], hash_path=parts.get("hash"))
            for ts, parts in sorted(found.items())
            if "normalized" in parts
        ]
        if not snapshots:
            continue
        service_name, environment = parse_service_env_from_dirname(child.name)
        histories.append(ServiceEnvHistory(service_name=service_name, environment=environment, directory_name=child.name, snapshots=snapshots))
    return histories


def build_history_index(histories: List[ServiceEnvHistory]) -> Dict[str, Any]:
    services = []
    for item in histories:
        services.append({
            "id": f"{item.service_name} [{item.environment}]",
            "service_name": item.service_name,
            "environment": item.environment,
            "directory_name": item.directory_name,
            "snapshots": [
                {
                    "timestamp": snap.timestamp,
                    "normalized": snap.normalized_path.name,
                    "hash": snap.hash_path.name if snap.hash_path else "",
                }
                for snap in item.snapshots
            ],
        })
    return {"services": services}


def build_history_page(state_dir: Path) -> Path:
    histories = collect_histories(state_dir)
    history_index = build_history_index(histories)
    write_text(state_dir / "history_index.json", json.dumps(history_index, ensure_ascii=False, indent=2))

    legend_html = "".join(
        f'<div class="legend-item"><span class="badge {klass}">{esc(name.replace("_", " "))}</span><div class="legend-copy">{esc(text)}</div></div>'
        for name, text, klass in [
            ("no_change", CLASSIFICATION_DESCRIPTIONS["no_change"], "good"),
            ("docs_only", CLASSIFICATION_DESCRIPTIONS["docs_only"], "info"),
            ("non_breaking", CLASSIFICATION_DESCRIPTIONS["non_breaking"], "warn"),
            ("breaking", CLASSIFICATION_DESCRIPTIONS["breaking"], "bad"),
        ]
    )

    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>EG Retail Swagger History</title>
  <style>
    :root {{ --bg:#0b1020; --card:#121933; --muted:#9fb0d0; --text:#eef4ff; --border:#263052; --accent:#7cc4ff; --good:#153a2a; --warn:#4a3310; --bad:#4c1720; --info:#17324c; }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; font-family: Inter, Segoe UI, Arial, sans-serif; background:var(--bg); color:var(--text); }}
    .wrap {{ max-width: 1500px; margin:0 auto; padding:24px; }}
    .topnav, .toolbar {{ display:flex; gap:12px; flex-wrap:wrap; margin-bottom:18px; }}
    .topnav a, select, button {{ background:rgba(255,255,255,.05); color:var(--text); border:1px solid var(--border); border-radius:10px; padding:8px 12px; text-decoration:none; }}
    button {{ cursor:pointer; }}
    .hero {{ display:flex; justify-content:space-between; gap:16px; align-items:end; margin-bottom:18px; }}
    .hero h1 {{ margin:0 0 6px; }}
    .card, .result-block, .legend, .timeline-day, .info-grid > div {{ background:var(--card); border:1px solid var(--border); border-radius:18px; }}
    .legend, .result-block {{ padding:16px; }}
    .legend-grid, .info-grid, .stats, .columns {{ display:grid; gap:12px; }}
    .legend-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .info-grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); margin-bottom:18px; }}
    .info-grid > div {{ padding:14px; }}
    .muted {{ color:var(--muted); }}
    .stats {{ grid-template-columns: repeat(4, minmax(0, 1fr)); margin: 14px 0; }}
    .stat {{ background:rgba(255,255,255,.03); border:1px solid var(--border); border-radius:14px; padding:12px; }}
    .stat span {{ display:block; color:var(--muted); font-size:12px; margin-bottom:6px; }}
    .stat strong {{ font-size:22px; }}
    .columns {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
    .column {{ background: rgba(255,255,255,.02); border:1px solid var(--border); border-radius:14px; padding:12px; min-width:0; }}
    .badge {{ display:inline-block; border-radius:999px; padding:6px 10px; font-size:12px; text-transform:uppercase; letter-spacing:.04em; }}
    .badge.good {{ background:var(--good); }} .badge.warn {{ background:var(--warn); }} .badge.bad {{ background:var(--bad); }} .badge.info {{ background:var(--info); }}
    .timeline-day {{ margin-top:16px; }}
    .timeline-day summary {{ list-style:none; cursor:pointer; padding:16px; }}
    .day-body {{ padding:0 16px 16px; }}
    .timeline-entry {{ border-top:1px solid var(--border); padding:16px 0; }}
    .timeline-entry:first-child {{ border-top:none; padding-top:0; }}
    .timeline-head {{ display:flex; justify-content:space-between; gap:12px; align-items:center; margin-bottom:10px; }}
    .timeline-title {{ font-weight:600; }}
    .section-title {{ margin-top:18px; }}
    ul {{ margin:8px 0 0 18px; padding:0; }}
    code {{ background: rgba(255,255,255,.05); border:1px solid var(--border); border-radius:8px; padding:2px 6px; word-break:break-word; }}
    .mini-stats {{ display:flex; gap:8px; flex-wrap:wrap; margin-bottom:12px; }}
    .mini-stat {{ background:rgba(255,255,255,.03); border:1px solid var(--border); border-radius:12px; padding:8px 10px; }}
    @media (max-width: 1100px) {{ .legend-grid, .info-grid, .stats, .columns {{ grid-template-columns: 1fr; }} .hero {{ display:block; }} }}
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
        <div class="muted">Compare two snapshots or explore a grouped timeline across a range.</div>
      </div>
      <div class="muted">Source: history_index.json</div>
    </section>

    <section class="legend">
      <h2>Classification guide</h2>
      <div class="muted">These labels are a best-effort interpretation of contract impact after documentation-style metadata is normalized out.</div>
      <div class="legend-grid">{legend_html}</div>
    </section>

    <section class="toolbar">
      <label>Service / env <select id="serviceSelect"></select></label>
      <label>From <select id="fromSelect"></select></label>
      <label>To <select id="toSelect"></select></label>
      <label>Timeline filter <select id="classFilter">
        <option value="all">All entries</option>
        <option value="breaking">Breaking only</option>
        <option value="non_breaking">Non-breaking only</option>
        <option value="docs_only">Docs only</option>
      </select></label>
      <button id="compareBtn" type="button">Net diff</button>
      <button id="timelineBtn" type="button">Change timeline</button>
    </section>

    <section class="info-grid">
      <div><div class="muted">Snapshots</div><strong id="countValue">-</strong></div>
      <div><div class="muted">Earliest</div><strong id="earliestValue">-</strong></div>
      <div><div class="muted">Latest</div><strong id="latestValue">-</strong></div>
    </section>

    <div id="result" class="muted">Pick a service and snapshot range, then choose Net diff or Change timeline.</div>
  </div>
  <script>
    function escapeHtml(value) {{
      return String(value).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;');
    }}
    async function loadIndex() {{
      const res = await fetch('history_index.json', {{ cache: 'no-store' }});
      if (!res.ok) throw new Error('Could not load history_index.json');
      return res.json();
    }}
    function fillSelect(select, values) {{
      select.innerHTML = values.map(v => `<option value="${{escapeHtml(v)}}">${{escapeHtml(v)}}</option>`).join('');
    }}
    function renderList(items) {{
      if (!items.length) return '<div class="muted">None</div>';
      return `<ul>${{items.map(x => `<li><code>${{escapeHtml(x)}}</code></li>`).join('')}}</ul>`;
    }}
    function normalize(node) {{
      if (Array.isArray(node)) return node.map(normalize);
      if (!node || typeof node !== 'object') return node;
      const ignored = new Set(['description', 'summary', 'externalDocs', 'example', 'examples', 'title', 'servers', 'operationId', 'tags']);
      const out = {{}};
      for (const key of Object.keys(node).sort()) {{
        if (ignored.has(String(key))) continue;
        out[key] = normalize(node[key]);
      }}
      return out;
    }}
    function schemaSignature(schema) {{ return JSON.stringify(normalize(schema || null)); }}
    function flattenPaths(spec) {{
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
    }}
    function operationSignature(op) {{
      const parameters = (op.parameters || []).filter(p => p && typeof p === 'object').map(p => ({{ name: p.name || '', in: p.in || '', required: !!p.required, schema: schemaSignature(p.schema) }})).sort((a, b) => `${{a.in}}/${{a.name}}`.localeCompare(`${{b.in}}/${{b.name}}`));
      const requestBody = {{}};
      for (const [contentType, desc] of Object.entries((op.requestBody || {{}}).content || {{}})) requestBody[contentType] = schemaSignature((desc || {{}}).schema);
      const responses = {{}};
      for (const [status, resp] of Object.entries(op.responses || {{}}).sort((a, b) => String(a[0]).localeCompare(String(b[0])))) {{
        const content = {{}};
        for (const [contentType, desc] of Object.entries(((resp || {{}}).content || {{}}))) content[contentType] = schemaSignature((desc || {{}}).schema);
        responses[String(status)] = content;
      }}
      return JSON.stringify({{ parameters, requestBody, responses, security: normalize(op.security || []), deprecated: !!op.deprecated }});
    }}
    function compareSpecs(oldSpec, newSpec) {{
      const a = flattenPaths(oldSpec), b = flattenPaths(newSpec);
      const aKeys = new Set(Object.keys(a)), bKeys = new Set(Object.keys(b));
      return {{
        added: [...bKeys].filter(x => !aKeys.has(x)).sort(),
        removed: [...aKeys].filter(x => !bKeys.has(x)).sort(),
        changed: [...aKeys].filter(x => bKeys.has(x) && operationSignature(a[x]) !== operationSignature(b[x])).sort(),
      }};
    }}
    function classifyDiff(diff) {{
      if (!diff.added.length && !diff.removed.length && !diff.changed.length) return {{ name: 'no_change', label: 'no change', cls: 'good' }};
      if (diff.removed.length) return {{ name: 'breaking', label: 'breaking', cls: 'bad' }};
      return {{ name: 'non_breaking', label: 'non breaking', cls: 'warn' }};
    }}
    async function loadSnapshot(directoryName, timestamp) {{
      const res = await fetch(`${{directoryName}}/snapshots/${{timestamp}}.normalized.json`, {{ cache: 'no-store' }});
      if (!res.ok) throw new Error(`Could not load snapshot ${{timestamp}}`);
      return res.json();
    }}
    function renderNetDiff(diff, title) {{
      const klass = classifyDiff(diff);
      return `<div class="result-block"><div class="timeline-head"><div class="muted">${{escapeHtml(title)}}</div><span class="badge ${{klass.cls}}">${{escapeHtml(klass.label)}}</span></div><div class="stats"><div class="stat"><span>Added</span><strong>${{diff.added.length}}</strong></div><div class="stat"><span>Removed</span><strong>${{diff.removed.length}}</strong></div><div class="stat"><span>Changed</span><strong>${{diff.changed.length}}</strong></div><div class="stat"><span>Classification</span><strong>${{escapeHtml(klass.label)}}</strong></div></div><h4 class="section-title">Added</h4>${{renderList(diff.added)}}<h4 class="section-title">Removed</h4>${{renderList(diff.removed)}}<h4 class="section-title">Changed</h4>${{renderList(diff.changed)}}</div>`;
    }}
    function makeTimelineEntry(fromTs, toTs, diff) {{
      const klass = classifyDiff(diff);
      return {{ classification: klass.name, html: `<div class="timeline-entry" data-classification="${{klass.name}}"><div class="timeline-head"><div class="timeline-title">${{escapeHtml(fromTs)}} → ${{escapeHtml(toTs)}}</div><span class="badge ${{klass.cls}}">${{escapeHtml(klass.label)}}</span></div><div class="mini-stats"><div class="mini-stat">Added: <strong>${{diff.added.length}}</strong></div><div class="mini-stat">Removed: <strong>${{diff.removed.length}}</strong></div><div class="mini-stat">Changed: <strong>${{diff.changed.length}}</strong></div></div><div class="columns"><div class="column"><h4>Added</h4>${{renderList(diff.added)}}</div><div class="column"><h4>Removed</h4>${{renderList(diff.removed)}}</div><div class="column"><h4>Changed</h4>${{renderList(diff.changed)}}</div></div></div>` }};
    }}
    function groupTimelineEntries(entries) {{
      const groups = new Map();
      for (const entry of entries) {{
        const day = entry.from.slice(0, 10);
        if (!groups.has(day)) groups.set(day, {{ day, entries: [] }});
        groups.get(day).entries.push(entry);
      }}
      return [...groups.values()];
    }}
    function renderGroupedTimeline(groups, classFilter) {{
      return groups.map(group => {{
        const filtered = group.entries.filter(entry => classFilter === 'all' || entry.classification === classFilter);
        if (!filtered.length) return '';
        return `<details class="timeline-day" open><summary><strong>${{escapeHtml(group.day)}}</strong> <span class="muted">· ${{filtered.length}} visible step(s)</span></summary><div class="day-body">${{filtered.map(entry => entry.html).join('')}}</div></details>`;
      }}).join('');
    }}
    async function main() {{
      const data = await loadIndex();
      const services = data.services || [];
      const serviceSelect = document.getElementById('serviceSelect');
      const fromSelect = document.getElementById('fromSelect');
      const toSelect = document.getElementById('toSelect');
      const classFilter = document.getElementById('classFilter');
      const compareBtn = document.getElementById('compareBtn');
      const timelineBtn = document.getElementById('timelineBtn');
      const result = document.getElementById('result');
      const countValue = document.getElementById('countValue');
      const earliestValue = document.getElementById('earliestValue');
      const latestValue = document.getElementById('latestValue');
      const map = new Map(services.map(s => [s.id, s]));
      fillSelect(serviceSelect, services.map(s => s.id));
      function currentService() {{ return map.get(serviceSelect.value); }}
      function currentSnapshots() {{ return currentService()?.snapshots || []; }}
      function refreshSnapshotSelectors() {{
        const snaps = currentSnapshots().map(s => s.timestamp);
        fillSelect(fromSelect, snaps); fillSelect(toSelect, snaps);
        if (snaps.length) {{ fromSelect.value = snaps[0]; toSelect.value = snaps[snaps.length - 1]; countValue.textContent = String(snaps.length); earliestValue.textContent = snaps[0]; latestValue.textContent = snaps[snaps.length - 1]; }}
        else {{ countValue.textContent = earliestValue.textContent = latestValue.textContent = '-'; }}
      }}
      function selectedRangeIndices() {{ const snaps = currentSnapshots(); return {{ snaps, fromIdx: snaps.findIndex(s => s.timestamp === fromSelect.value), toIdx: snaps.findIndex(s => s.timestamp === toSelect.value) }}; }}
      async function runNetDiff() {{
        const current = currentService(); if (!current) return;
        const {{ snaps, fromIdx, toIdx }} = selectedRangeIndices();
        if (fromIdx < 0 || toIdx < 0) return result.innerHTML = '<div class="muted">Invalid snapshot selection.</div>';
        if (fromIdx === toIdx) return result.innerHTML = '<div class="muted">Choose two different snapshots.</div>';
        if (fromIdx > toIdx) return result.innerHTML = '<div class="muted">From must be earlier than To.</div>';
        try {{
          const [aSpec, bSpec] = await Promise.all([loadSnapshot(current.directory_name, snaps[fromIdx].timestamp), loadSnapshot(current.directory_name, snaps[toIdx].timestamp)]);
          result.innerHTML = renderNetDiff(compareSpecs(aSpec, bSpec), `${{snaps[fromIdx].timestamp}} → ${{snaps[toIdx].timestamp}}`);
        }} catch (err) {{ result.innerHTML = `<div class="muted">Net diff failed: ${{escapeHtml(err.message)}}</div>`; }}
      }}
      async function runTimeline() {{
        const current = currentService(); if (!current) return;
        const {{ snaps, fromIdx, toIdx }} = selectedRangeIndices();
        if (fromIdx < 0 || toIdx < 0) return result.innerHTML = '<div class="muted">Invalid snapshot selection.</div>';
        if (fromIdx === toIdx) return result.innerHTML = '<div class="muted">Choose two different snapshots.</div>';
        if (fromIdx > toIdx) return result.innerHTML = '<div class="muted">From must be earlier than To.</div>';
        const selected = snaps.slice(fromIdx, toIdx + 1);
        try {{
          const specs = await Promise.all(selected.map(s => loadSnapshot(current.directory_name, s.timestamp)));
          const entries = []; let totalAdded = 0, totalRemoved = 0, totalChanged = 0, breakingCount = 0;
          for (let i = 0; i < selected.length - 1; i++) {{
            const diff = compareSpecs(specs[i], specs[i + 1]);
            totalAdded += diff.added.length; totalRemoved += diff.removed.length; totalChanged += diff.changed.length;
            const entry = makeTimelineEntry(selected[i].timestamp, selected[i + 1].timestamp, diff);
            if (entry.classification === 'breaking') breakingCount += 1;
            if (diff.added.length || diff.removed.length || diff.changed.length) entries.push({{ from: selected[i].timestamp, classification: entry.classification, html: entry.html }});
          }}
          const header = `<div class="result-block"><div class="muted">${{escapeHtml(selected[0].timestamp)}} → ${{escapeHtml(selected[selected.length - 1].timestamp)}}</div><div class="stats"><div class="stat"><span>Total added events</span><strong>${{totalAdded}}</strong></div><div class="stat"><span>Total removed events</span><strong>${{totalRemoved}}</strong></div><div class="stat"><span>Total changed events</span><strong>${{totalChanged}}</strong></div><div class="stat"><span>Breaking steps</span><strong>${{breakingCount}}</strong></div></div><div class="muted">Timeline is grouped by day. Use the timeline filter to focus on breaking or non-breaking entries.</div></div>`;
          if (!entries.length) return result.innerHTML = header + '<div class="muted">No step-by-step changes were detected across the selected range.</div>';
          result.innerHTML = header + renderGroupedTimeline(groupTimelineEntries(entries), classFilter.value);
        }} catch (err) {{ result.innerHTML = `<div class="muted">Timeline failed: ${{escapeHtml(err.message)}}</div>`; }}
      }}
      serviceSelect.addEventListener('change', refreshSnapshotSelectors);
      classFilter.addEventListener('change', () => {{ if (result.innerHTML.includes('timeline-day')) runTimeline(); }});
      refreshSnapshotSelectors();
      compareBtn.addEventListener('click', runNetDiff);
      timelineBtn.addEventListener('click', runTimeline);
    }}
    main().catch(err => {{ document.getElementById('result').innerHTML = `<div class="muted">Initialization failed: ${{escapeHtml(err.message)}}</div>`; }});
  </script>
</body>
</html>'''

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
