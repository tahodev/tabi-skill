#!/usr/bin/env python3
"""Smoke-test response fixtures in */examples/.

Each fixture must be registered in docs/verification.json, parse cleanly,
carry a success status, contain at least one record, and be labeled in its
SKILL.md the same way the registry labels it (captured vs illustrative).
"""
from pathlib import Path
import json, re, sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
ILLUSTRATIVE_MARK = '構造を再現した記述例'
OK_CODES = {'00', '0000', 'INFO-000'}
reg = json.loads((root / 'docs/verification.json').read_text(encoding='utf-8'))['skills']
registered = {}
for name, e in reg.items():
    for fx in e.get('fixtures', []):
        registered[fx['path']] = (name, fx.get('origin'))
on_disk = sorted(str(p.relative_to(root)) for p in root.glob('*/examples/*') if p.is_file())
failed = False

def fail(msg):
    global failed
    failed = True
    print(f'FAIL  {msg}')

for path in sorted(set(on_disk) - set(registered)):
    fail(f'{path}: not registered in docs/verification.json fixtures')
for path in sorted(set(registered) - set(on_disk)):
    fail(f'{path}: registered but missing on disk')

def json_status(obj):
    """Return (ok, detail) for the first status field found."""
    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            for key in ('resultCode', 'code'):
                if key in cur and isinstance(cur[key], (str, int)):
                    val = str(cur[key])
                    return val in OK_CODES, f'{key}={val}'
            if 'result' in cur and isinstance(cur['result'], int):
                return cur['result'] == 1, f'result={cur["result"]}'
            if 'RESULT' in cur and isinstance(cur['RESULT'], dict):
                return False, f'RESULT={cur["RESULT"]}'
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
    return True, 'no status field (record check only)'

def json_records(obj):
    if isinstance(obj, list):
        if obj and all(isinstance(x, dict) for x in obj):
            return len(obj)
        return max((json_records(x) for x in obj), default=0)
    if isinstance(obj, dict):
        return max((json_records(v) for v in obj.values()), default=0)
    return 0

for path in on_disk:
    if path not in registered:
        continue
    skill, origin = registered[path]
    text = (root / path).read_text(encoding='utf-8')
    try:
        if path.endswith('.json'):
            data = json.loads(text)
            ok, detail = json_status(data)
            records = json_records(data)
        elif path.endswith('.xml'):
            tree = ET.fromstring(text)
            code = tree.findtext('.//resultCode')
            ok, detail = (code in OK_CODES, f'resultCode={code}') if code is not None else (True, 'no resultCode')
            records = len(tree.findall('.//item'))
        else:
            fail(f'{path}: unsupported fixture type (use .json or .xml)'); continue
    except (json.JSONDecodeError, ET.ParseError) as err:
        fail(f'{path}: does not parse ({err})'); continue
    if not ok:
        fail(f'{path}: non-success status ({detail})'); continue
    if records < 1:
        fail(f'{path}: no records found'); continue
    if origin not in ('captured', 'illustrative'):
        fail(f'{path}: origin must be captured or illustrative (got {origin!r})'); continue
    lines = [l for l in (root / skill / 'SKILL.md').read_text(encoding='utf-8').splitlines() if Path(path).name in l]
    if not lines:
        fail(f'{path}: not referenced from {skill}/SKILL.md'); continue
    near = ' '.join(lines)
    # A line can mention several fixtures; look at the text right after this file name.
    after = near.split(Path(path).name, 1)[1][:80]
    labeled_illustrative = ILLUSTRATIVE_MARK in after
    if origin == 'illustrative' and not labeled_illustrative:
        fail(f'{path}: registry says illustrative but SKILL.md does not say {ILLUSTRATIVE_MARK}')
    elif origin == 'captured' and labeled_illustrative:
        fail(f'{path}: registry says captured but SKILL.md calls it {ILLUSTRATIVE_MARK}')
    else:
        print(f'OK    {path}: {detail}, {records} record(s), {origin}')

print(f'Checked {len(on_disk)} fixtures')
sys.exit(1 if failed else 0)
