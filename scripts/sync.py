#!/usr/bin/env python3
"""每 3 天从 MetaCubeX/meta-rules-dat (meta 分支) 同步 mrs/ 下的 .mrs。
冲突策略：若本地文件与 upstream-snapshots/ 中上次同步快照不同（说明本地改过），则保留本地、跳过。
zdy/ 为自定义 .list，不参与同步。"""
import json, os, urllib.request, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
up = json.load(open(os.path.join(ROOT, "upstream.json"), encoding="utf-8"))
snapdir = os.path.join(ROOT, "upstream-snapshots")
fail = 0
for rel, url in up.items():
    dst = os.path.join(ROOT, rel); snap = os.path.join(snapdir, rel)
    try:
        data = urllib.request.urlopen(url, timeout=60).read()
    except Exception as e:
        print("FAIL", rel, e); fail += 1; continue
    if not data:
        print("EMPTY", rel); fail += 1; continue
    local = open(dst, "rb").read() if os.path.exists(dst) else None
    old = open(snap, "rb").read() if os.path.exists(snap) else None
    if local is not None and old is not None and local != old:
        print("KEEP-LOCAL", rel)
    elif local != data:
        os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, "wb").write(data); print("UPDATE", rel)
    os.makedirs(os.path.dirname(snap), exist_ok=True); open(snap, "wb").write(data)
sys.exit(1 if fail == len(up) else 0)
