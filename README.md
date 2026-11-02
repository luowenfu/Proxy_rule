# Proxy_rule

OpenClash / Mihomo 规则仓库。

## 目录如何区分
- `mrs/`：**全部来自 [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) `meta` 分支**的二进制规则，命名 `geosite_<分类>.mrs` / `geoip_<分类>.mrs`（`geolocation-!cn` 写成 `geolocation-not-cn`）。由 `upstream.json` 声明来源，GitHub Actions 每 3 天自动同步。
- `zdy/`：**自定义**的 classical `.list`（meta 无对应分类或为自用规则），本地手工维护，不参与同步。
- `upstream-snapshots/`：上次同步时的上游原样快照。若 `mrs/` 中某文件与快照不同（本地改过），同步时保留本地版本。

## 在 YAML 中引用
```
https://gh-proxy.com/raw.githubusercontent.com/luowenfu/Proxy_rule/refs/heads/main/mrs/geosite_openai.mrs   # behavior: domain, format: mrs
https://gh-proxy.com/raw.githubusercontent.com/luowenfu/Proxy_rule/refs/heads/main/zdy/Globe2.list          # behavior: classical, format: text
```
命名约定：公共规则 服务名 / Domain（或 / IP）→ mrs/（anchor *domain / *ip，format mrs）；自定义 服务名_zdy / Domain → zdy/服务名_zdy.list（anchor *class）。同一服务 _zdy 在 rule-providers 和 rules 中都紧挨着排在 mrs 之前。公共规则不得写成 list，也不使用 clash/ 目录。

## zdy 如何生成（差集）
按旧配置的每个分流服务：下载旧 rule-provider URL 的实际内容（blackmatrix7 / liandu2024 / luowenfu 自建 list），与 meta 分支同名 geosite（及 geoip）的可读 .list 做差集：
- zdy = 旧规则条目 − geosite 已覆盖条目；差集为空则不建 zdy，只用 mrs。
- 规范化：域名小写；裸域名视为 DOMAIN，+.x 视为 DOMAIN-SUFFIX；旧 DOMAIN-SUFFIX,x 若 geosite 有 x 或其任一父域的 suffix 即视为已覆盖；旧 DOMAIN,x 若 geosite 有 full x 或其父域 suffix 即覆盖；IP-CIDR 仅当服务有 geoip 且为其子网才覆盖；DOMAIN-KEYWORD、PROCESS-NAME 等 mrs 无法表达，一律保留在 zdy。
- meta 无对应 geosite 的服务（TEST、Meta AI、Copilot、Crunchyroll、Popcorn、UltraMobile、Direct、Proxy、Globe2）：旧内容全量进 zdy，不建 mrs。
- Globe：直接使用 meta `geolocation-!cn`（本仓 `mrs/geosite_geolocation-not-cn.mrs`），不再使用 Globe_zdy。

## 服务处理表（条数 = 旧规则去重后 / 差集）
| 服务 | 处理 | meta 来源 | 旧条数 | zdy 条数 |
|---|---|---|---|---|
| TEST | 仅zdy | — | 60 | 60 |
| ChatGPT | 仅mrs | geosite:openai | 0 | 0 |
| Claude | mrs+zdy | geosite:anthropic | 3 | 1 |
| Cursor | 仅mrs | geosite:cursor | 0 | 0 |
| Meta AI | 仅zdy | — | 5 | 5 |
| Perplexity | 仅mrs | geosite:perplexity | 0 | 0 |
| Copilot | 仅zdy | — | 2 | 2 |
| Gemini | mrs+zdy | geosite:google-gemini | 11 | 4 |
| Groq | 仅mrs | geosite:groq | 0 | 0 |
| Grok | 仅mrs | geosite:xai | 1 | 0 |
| Reddit | 仅mrs | geosite:reddit | 0 | 0 |
| PT-Tracker | mrs+zdy | geosite:category-pt | 266 | 202 |
| Dev-GitHub | mrs+zdy | geosite:github | 546 | 514 |
| Synology | 仅mrs | geosite:synology | 0 | 0 |
| Telegram | 仅mrs | geosite:telegram, geoip:telegram | 0 | 0 |
| Twitter | 仅mrs | geosite:x | 0 | 0 |
| WhatsApp | mrs+zdy | geosite:whatsapp | 17 | 15 |
| Facebook | 仅mrs | geosite:facebook | 0 | 0 |
| Instagram | mrs+zdy | geosite:instagram | 4 | 2 |
| Apple | mrs+zdy | geosite:apple, geosite:apple-cn | 11 | 4 |
| Microsoft | 仅mrs | geosite:microsoft | 0 | 0 |
| Crypto | mrs+zdy | geosite:category-cryptocurrency | 341 | 155 |
| PayPal | mrs+zdy | geosite:paypal | 247 | 3 |
| Wise | 仅mrs | geosite:wise | 0 | 0 |
| BiliBili | 仅mrs | geosite:bilibili | 0 | 0 |
| Youtube | mrs+zdy | geosite:youtube | 183 | 7 |
| TikTok | 仅mrs | geosite:tiktok | 0 | 0 |
| Netflix | 仅mrs | geosite:netflix, geoip:netflix | 0 | 0 |
| Disney | 仅mrs | geosite:disney | 0 | 0 |
| Amazon | 仅mrs | geosite:amazon | 0 | 0 |
| eBay | mrs+zdy | geosite:ebay | 44 | 7 |
| Crunchyroll | 仅zdy | — | 3 | 3 |
| Popcorn | 仅zdy | — | 1 | 1 |
| HBO | 仅mrs | geosite:hbo | 0 | 0 |
| Spotify | 仅mrs | geosite:spotify | 0 | 0 |
| Steam | 仅mrs | geosite:steam | 0 | 0 |
| Epic | mrs+zdy | geosite:epicgames | 15 | 1 |
| EA | mrs+zdy | geosite:ea | 165 | 6 |
| Blizzard | mrs+zdy | geosite:blizzard | 62 | 48 |
| UBI | mrs+zdy | geosite:ubisoft | 5 | 2 |
| PlayStation | 仅mrs | geosite:playstation | 4 | 0 |
| Nintend | mrs+zdy | geosite:nintendo | 126 | 4 |
| Google | 仅mrs | geosite:google, geoip:google | 0 | 0 |
| Nvidia | mrs+zdy | geosite:nvidia | 62 | 2 |
| Adobe | mrs+zdy | geosite:adobe | 137 | 14 |
| UltraMobile | 仅zdy | — | 2 | 2 |
| Direct | 仅zdy | — | 577 | 577 |
| China | 仅mrs | geosite:cn, geoip:cn | 0 | 0 |
| Private | 仅mrs | geosite:private | 0 | 0 |
| Proxy | 仅zdy | — | 296 | 296 |
| Globe | 仅 mrs | geolocation-!cn | — | — |
| Globe2 | 仅zdy | — | 1 | 1 |

## Globe

Globe 现直接使用 meta `geolocation-!cn`（本仓 `mrs/geosite_geolocation-not-cn.mrs`），不再使用 Globe_zdy。
