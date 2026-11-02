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
命名约定：公共规则 `服务名 / Domain`（或 `/ IP`）→ `mrs/`（anchor `*domain` / `*ip`，format mrs）；仅自定义条目 `服务名_zdy / Domain` → `zdy/*.list`（anchor `*class`）。`_zdy` 在 rule-providers 和 rules 中都排在对应 mrs 之前（如 `Apple_zdy` → `Apple`，`Crypto_zdy` → `Crypto`，`Globe_zdy`/`Proxy_zdy` → `Globe`）。公共规则不得写成 list，也不再使用 `clash/` 目录。

## Provider 映射
| rule-provider | 文件 |
|---|---|
| `ChatGPT / Domain` | `mrs/geosite_openai.mrs` |
| `Claude / Domain` | `mrs/geosite_anthropic.mrs` |
| `Perplexity / Domain` | `mrs/geosite_perplexity.mrs` |
| `Gemini / Domain` | `mrs/geosite_google-gemini.mrs` |
| `Grok / Domain` | `mrs/geosite_xai.mrs` |
| `Groq / Domain` | `mrs/geosite_groq.mrs` |
| `Cursor / Domain` | `mrs/geosite_cursor.mrs` |
| `Telegram / Domain` | `mrs/geosite_telegram.mrs` |
| `Telegram / IP` | `mrs/geoip_telegram.mrs` |
| `Twitter / Domain` | `mrs/geosite_x.mrs` |
| `WhatsApp / Domain` | `mrs/geosite_whatsapp.mrs` |
| `Facebook / Domain` | `mrs/geosite_facebook.mrs` |
| `Instagram / Domain` | `mrs/geosite_instagram.mrs` |
| `Reddit / Domain` | `mrs/geosite_reddit.mrs` |
| `Amazon / Domain` | `mrs/geosite_amazon.mrs` |
| `Apple-CN / Domain` | `mrs/geosite_apple-cn.mrs` |
| `Apple / Domain` | `mrs/geosite_apple.mrs` |
| `Microsoft / Domain` | `mrs/geosite_microsoft.mrs` |
| `TikTok / Domain` | `mrs/geosite_tiktok.mrs` |
| `Netflix / Domain` | `mrs/geosite_netflix.mrs` |
| `Netflix / IP` | `mrs/geoip_netflix.mrs` |
| `Disney / Domain` | `mrs/geosite_disney.mrs` |
| `HBO / Domain` | `mrs/geosite_hbo.mrs` |
| `Spotify / Domain` | `mrs/geosite_spotify.mrs` |
| `Youtube / Domain` | `mrs/geosite_youtube.mrs` |
| `BiliBili / Domain` | `mrs/geosite_bilibili.mrs` |
| `Steam / Domain` | `mrs/geosite_steam.mrs` |
| `Epic / Domain` | `mrs/geosite_epicgames.mrs` |
| `EA / Domain` | `mrs/geosite_ea.mrs` |
| `Blizzard / Domain` | `mrs/geosite_blizzard.mrs` |
| `UBI / Domain` | `mrs/geosite_ubisoft.mrs` |
| `PlayStation / Domain` | `mrs/geosite_playstation.mrs` |
| `Nintend / Domain` | `mrs/geosite_nintendo.mrs` |
| `Adobe / Domain` | `mrs/geosite_adobe.mrs` |
| `Nvidia / Domain` | `mrs/geosite_nvidia.mrs` |
| `PayPal / Domain` | `mrs/geosite_paypal.mrs` |
| `eBay / Domain` | `mrs/geosite_ebay.mrs` |
| `Wise / Domain` | `mrs/geosite_wise.mrs` |
| `Synology / Domain` | `mrs/geosite_synology.mrs` |
| `Crypto / Domain` | `mrs/geosite_category-cryptocurrency.mrs` |
| `PT-Tracker / Domain` | `mrs/geosite_category-pt.mrs` |
| `Google / Domain` | `mrs/geosite_google.mrs` |
| `Google / IP` | `mrs/geoip_google.mrs` |
| `Private / Domain` | `mrs/geosite_private.mrs` |
| `China / Domain` | `mrs/geosite_cn.mrs` |
| `China / IP` | `mrs/geoip_cn.mrs` |
| `Globe / Domain` | `mrs/geosite_geolocation-not-cn.mrs` |
| `Globe_zdy / Domain` | `zdy/Globe2.list` |
| `Dev-GitHub_zdy / Domain` | `zdy/dev.list` |
| `UltraMobile_zdy / Domain` | `zdy/ultramobile.list` |
| `Crypto_zdy / Domain` | `zdy/crypto.list` |
| `TEST_zdy / Domain` | `zdy/Check.list` |
| `Meta AI_zdy / Domain` | `zdy/MetaAi.list` |
| `Copilot_zdy / Domain` | `zdy/Copilot.list` |
| `Apple_zdy / Domain` | `zdy/Apple.list` |
| `Crunchyroll_zdy / Domain` | `zdy/Crunchyroll.list` |
| `Popcorn_zdy / Domain` | `zdy/Popcorn.list` |
| `Direct_zdy / Domain` | `zdy/Direct.list` |
| `Proxy_zdy / Domain` | `zdy/Proxy.list` |
