#!/usr/bin/env python3
import json
import re
from collections import defaultdict

path = 'works.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])
authors = defaultdict(lambda: {'count':0, 'titles':[]})
key_re = re.compile(r"/authors/OL\d+A")

for e in entries:
    title = e.get('title') or e.get('subtitle') or '<no title>'
    for a in e.get('authors', []) or []:
        # Try common shapes
        k = None
        if isinstance(a, dict):
            # direct author.key
            auth = a.get('author')
            if isinstance(auth, dict):
                k = auth.get('key')
            # sometimes the author object itself may contain the key
            if not k:
                for v in a.values():
                    if isinstance(v, str) and key_re.search(v):
                        k = v
                    elif isinstance(v, dict):
                        # nested
                        for vv in v.values():
                            if isinstance(vv, str) and key_re.search(vv):
                                k = vv
        # fallback: search the serialized author entry
        if not k:
            s = json.dumps(a)
            m = key_re.search(s)
            if m:
                k = m.group(0)
        if k:
            authors[k]['count'] += 1
            if len(authors[k]['titles']) < 10:
                authors[k]['titles'].append(title)

# Print results
items = sorted(authors.items(), key=lambda x: (-x[1]['count'], x[0]))
print(f"Found {len(items)} unique author keys\n")
for key, info in items:
    print(f"{key}: {info['count']} appearances")
    for t in info['titles'][:5]:
        print(f"  - {t}")
    if info['count'] > len(info['titles']):
        print(f"  ... ({info['count'] - len(info['titles'])} more titles)")
    print()
