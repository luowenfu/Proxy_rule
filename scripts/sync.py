#!/usr/bin/env python3
"""每 3 天同步上游规则（upstream.json 声明 path -> 来源）。
- 值为字符串：原样拉取字节写入（mrs/，来自 MetaCubeX/meta-rules-dat meta 分支）。
- 值为对象 {"url", "geosite": [...], "geoip": [...]}（zdy/）：下载上游 classical list，
  减去 meta geosite/geoip 已覆盖条目（geosite 为空则全量），生成 zdy 文本。
zdy 按条合并：以规则键（类型|主参数小写，去 no-resolve）合并本地与上游结果——
上游新增并入；本地独有保留；两边都有用本地行（冲突以本地为准）。顺序：本地原顺序在前，再补上游新键。
mrs：每次同步直接覆盖为上游（不手改 mrs）。
来自已停用的 luowenfu/ios_rule_script 的 zdy 为纯本地自定义，不在 upstream.json 中，不同步。"""
import json, os, sys, ipaddress, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
up = json.load(open(os.path.join(ROOT, "upstream.json"), encoding="utf-8"))
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

def rkey(l):
    t, v = norm(l)
    v = ",".join(x for x in v.split(",") if x.strip().lower() != "no-resolve")
    return t + "|" + v.lower()

def merge(local, up):
    ul = up.decode("utf-8").splitlines()
    head = [l for l in ul if l.startswith("#")]
    urules = [l for l in ul if l.strip() and not l.startswith("#")]
    out, seen = [], set()
    for l in lines(local.decode("utf-8", "replace")) if local else []:
        k = rkey(l)
        if k not in seen: seen.add(k); out.append(l)
    nl = len(out)
    for l in urules:
        k = rkey(l)
        if k not in seen: seen.add(k); out.append(l)
    return ("\n".join(head + out) + "\n").encode("utf-8"), len(out) - nl

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
    dst = os.path.join(ROOT, rel)
    try:
        if isinstance(spec, str): data = fetch(spec)
        elif rel.startswith("zdy/"): data = build(rel, spec)
        else: data = fetch(spec["url"])
    except Exception as e:
        print("FAIL", rel, e); fail += 1; continue
    if not data:
        print("EMPTY", rel); fail += 1; continue
    local = open(dst, "rb").read() if os.path.exists(dst) else None
    if rel.startswith("zdy/") and not isinstance(spec, str):
        merged, added = merge(local, data)
        if merged != local:
            os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, "wb").write(merged); print("MERGE", rel, "+%d" % added)
        else: print("SAME", rel)
    elif local != data:
        os.makedirs(os.path.dirname(dst), exist_ok=True); open(dst, "wb").write(data); print("UPDATE", rel)
    else:
        print("SAME", rel)
sys.exit(1 if fail == len(up) else 0)
