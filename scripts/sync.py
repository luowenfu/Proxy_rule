#!/usr/bin/env python3
"""按 upstream.json 同步上游；clash/ 与 upstream-snapshots/ 不一致（用户改过）的文件跳过，以本地为准。"""
import json, os, sys, urllib.request
up = json.load(open('upstream.json', encoding='utf-8'))
def get(u):
    req = urllib.request.Request(u, headers={'User-Agent': 'sync'})
    return urllib.request.urlopen(req, timeout=60).read()
def conv(raw, kind):
    out = []
    for l in raw.decode().splitlines():
        l = l.strip()
        if not l or l.startswith('#'): continue
        if kind == 'geoip': out.append(('IP-CIDR6,' if ':' in l else 'IP-CIDR,') + l + ',no-resolve')
        elif l.startswith('+.'): out.append('DOMAIN-SUFFIX,' + l[2:])
        elif l.startswith('.'): out.append('DOMAIN-SUFFIX,' + l[1:])
        else: out.append('DOMAIN,' + l)
    return ('# converted from %s\n' % u + '\n'.join(out) + '\n').encode()
for fn, i in up.items():
    u = i['url']; cf = 'clash/' + fn; sf = 'upstream-snapshots/' + fn
    try:
        data = get(u)
        if i['mode'].startswith('convert-'): data = conv(data, i['mode'][8:])
    except Exception as e:
        print('FETCH FAIL', fn, e); continue
    local = open(cf, 'rb').read() if os.path.exists(cf) else None
    snap = open(sf, 'rb').read() if os.path.exists(sf) else None
    if local is not None and snap is not None and local != snap:
        print('SKIP (本地已修改)', fn)
        open(sf, 'wb').write(data) if False else None
        continue
    open(cf, 'wb').write(data); open(sf, 'wb').write(data)
    print('OK', fn)
