#!/usr/bin/env python3
"""每 3 天同步上游规则（upstream.json 声明 path -> 来源）。
- 值为字符串：原样拉取字节写入（mrs/，来自 MetaCubeX/meta-rules-dat meta 分支）。
- 值为对象 {"url", "geosite": [...], "geoip": [...]}（zdy/）：下载上游 classical list，
  减去 meta geosite/geoip 已覆盖条目（geosite 为空则全量），生成 zdy 文本。
冲突策略（KEEP-LOCAL）：本地文件与 upstream-snapshots/ 中上次计算结果不同（本地改过）则保留本地；
快照总是更新为本次计算结果。zdy 无快照但本地已存在且内容不同，也视为本地修改而保留。
来自已停用的 luowenfu/ios_rule_script 的 zdy 为纯本地自定义，不在 upstream.json 中，不同步。"""
import json, os, re, sys, ipaddress, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
up = json.load(open(os.path.join(ROOT, "upstream.json"), encoding="utf-8"))
snapdir = os.path.join(ROOT, "upstream-snapshots")
META = "https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/%s/%s.list"
_cache = {}

def fetch(url):
    if url not in _cache:
        req = urllib.request.Request(url, headers={"User-Agent": "Proxy_rule-sync"})
        _cache[url] = urllib.request.urlopen(req, timeout=60).read()
    return _cache[url]

def lines(text):
    for l in text.splitlines():
        l = l.strip()
        if l and not l.startswith(("#", "//", ";", "payload:")):
            yield l[2:].strip().strip("'\"") if l.startswith("- ") else l

def norm(l):
    p = [x.strip() for x in l.split(",")]
    if len(p) == 1:
        d = p[0].lower()
        return ("DOMAIN-SUFFIX", d[2:]) if d.startswith("+.") else ("DOMAIN", d)
    t = p[0].upper()
    if t in ("DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"):
        return (t, p[1].lower())
    return (t, ",".join(p[1:]))

def parents(d):
    parts = d.split(".")
    return {".".join(parts[i:]) for i in range(len(parts))}

def build(rel, spec):
    src = fetch(spec["url"]).decode("utf-8", "replace")
    gs, gi = spec.get("geosite") or [], spec.get("geoip") or []
    full, suf, nets = set(), set(), []
    for n in gs:
        for l in lines(fetch(META % ("geosite", n)).decode("utf-8", "replace")):
            t, v = norm(l)
            (suf if t == "DOMAIN-SUFFIX" else full).add(v)
    for n in gi:
        for l in lines(fetch(META % ("geoip", n)).decode("utf-8", "replace")):
            try: nets.append(ipaddress.ip_network(l.split(",")[-1].strip() if "," in l else l, strict=False))
            except ValueError: pass
    out, seen = [], set()
    for l in lines(src):
        t, v = norm(l)
        key = (t, v)
        if key in seen: continue
        seen.add(key)
        if t == "DOMAIN-SUFFIX" and parents(v) & suf: continue
        if t == "DOMAIN" and (v in full or parents(v) & suf): continue
        if t in ("IP-CIDR", "IP-CIDR6") and nets:
            try:
                n = ipaddress.ip_network(v.split(",")[0], strict=False)
                if any(n.version == m.version and n.subnet_of(m) for m in nets): continue
            except ValueError: pass
        out.append(l)
    name = os.path.basename(rel).rsplit(".", 1)[0]
    head = ["# %s: 上游规则 − meta %s" % (name, ("geosite/" + ",".join(gs)) if gs else "geosite(无对应，全量)")]
    if "luowenfu/ios_rule_script" not in spec["url"]:
        head.append("# 来源: " + spec["url"])
    if gs: head.append("# geosite差集: " + ",".join(gs))
    if gi: head.append("# geoip差集: " + ",".join(gi))
    return ("\n".join(head + out) + "\n").encode("utf-8")

fail = 0
for rel, spec in up.items():
    dst = os.path.join(ROOT, rel); snap = os.path.join(snapdir, rel)
    try:
        if isinstance(spec, str): data = fetch(spec)
        elif rel.startswith("zdy/"): data = build(rel, spec)
        else: data = fetch(spec["url"])
    except Exception as e:
        print("FAIL", rel, e); fail += 1; continue
    if not data:
        print("EMPTY", rel); fail += 1; continue
    local = open(dst, "rb").read() if os.path.exists(dst) else None
    old = open(snap, "rb").read() if os.path.exists(snap) else None
    if local is not None and local != data and (old is not None and local != old or old is None and rel.startswith("zdy/")):
        print("KEEP-LOCAL", rel)
    elif local != data:
        os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, "wb").write(data); print("UPDATE", rel)
    os.makedirs(os.path.dirname(snap), exist_ok=True); open(snap, "wb").write(data)
sys.exit(1 if fail == len(up) else 0)