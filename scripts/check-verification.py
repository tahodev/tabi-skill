#!/usr/bin/env python3
"""Check the verification registry: status grades, freshness, and README matrix sync.

Policy: docs/verification.md. Set TABI_TODAY=YYYY-MM-DD to test a future date.
Set TABI_FRESHNESS=warn to report stale grades as WARN instead of FAIL
(used on push/PR so an expiring date does not block unrelated changes;
the scheduled run stays strict and opens an issue).
"""
from datetime import date
from pathlib import Path
import json, os, re, sys

root = Path(__file__).resolve().parents[1]
STATUSES = ('live-data-verified', 'endpoint-confirmed', 'experimental')
KINDS = ('api', 'static')
reg = json.loads((root / 'docs/verification.json').read_text(encoding='utf-8'))
policy = reg['policy']
entries = reg['skills']
soft_freshness = os.environ.get('TABI_FRESHNESS') == 'warn'
today = date.fromisoformat(os.environ.get('TABI_TODAY') or date.today().isoformat())
skills = sorted(p.parent.name for p in root.glob('*/SKILL.md'))
failed = False

def fail(msg):
    global failed
    failed = True
    print(f'FAIL  {msg}')

missing = sorted(set(skills) - set(entries))
extra = sorted(set(entries) - set(skills))
if missing or extra:
    fail(f'docs/verification.json drift: missing={missing} extra={extra}')
else:
    print(f'OK    registry covers all {len(skills)} skills')

for name, e in sorted(entries.items()):
    status, kind = e.get('status'), e.get('kind')
    if status not in STATUSES:
        fail(f'{name}: unknown status {status!r} (use one of {", ".join(STATUSES)})'); continue
    if kind not in KINDS:
        fail(f'{name}: unknown kind {kind!r} (use api or static)')
    if status == 'experimental':
        if not e.get('note'):
            fail(f'{name}: experimental skills need a note saying what is missing')
        continue
    raw = e.get('verified_on')
    try:
        verified = date.fromisoformat(raw)
    except (TypeError, ValueError):
        fail(f'{name}: {status} needs verified_on as YYYY-MM-DD (got {raw!r})'); continue
    if verified > today:
        fail(f'{name}: verified_on {raw} is in the future'); continue
    max_age = e.get('review_days') or policy['max_age_days'][status]
    age = (today - verified).days
    left = max_age - age
    if left < 0 and soft_freshness:
        print(f'WARN  {name}: {status} is stale ({age} days since {raw}, limit {max_age}); scheduled run will fail')
    elif left < 0:
        fail(f'{name}: {status} is stale ({age} days since {raw}, limit {max_age}). Re-verify and update verified_on, or downgrade the status')
    elif left <= policy['warn_before_days']:
        print(f'WARN  {name}: {status} expires in {left} days (verified {raw}, limit {max_age})')

# README matrix: one row per status, starting with | `status` |
readme = (root / 'README.md').read_text(encoding='utf-8')
names = sorted(skills, key=len, reverse=True)
token = re.compile(r'(?<![a-z0-9-])(' + '|'.join(map(re.escape, names)) + r')(?![a-z0-9-])')
for status in STATUSES:
    rows = [l for l in readme.splitlines() if l.startswith(f'| `{status}` |')]
    if len(rows) != 1:
        fail(f'README verification matrix needs exactly one row for `{status}` (found {len(rows)})'); continue
    listed = set(token.findall(rows[0].split('|', 3)[-1]))
    expected = {n for n, e in entries.items() if e.get('status') == status}
    if listed != expected:
        fail(f'README `{status}` row drift: missing={sorted(expected - listed)} extra={sorted(listed - expected)}')
    else:
        print(f'OK    README `{status}` row matches registry ({len(expected)} skills)')

counts = {s: sum(1 for e in entries.values() if e.get('status') == s) for s in STATUSES}
print('OK    status counts: ' + ', '.join(f'{k}={v}' for k, v in counts.items()) + f' (as of {today})')
sys.exit(1 if failed else 0)
