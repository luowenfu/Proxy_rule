# Proxy_rule

OpenClash / Mihomo 自用规则集合（扁平存放于 `clash/`）。

- `.list`：classical text 规则（`behavior: classical`, `format: text`）
- 仅 `China_Domain.mrs` / `China_IP.mrs` 保留 mrs（来自 MetaCubeX/meta-rules-dat cn）
- `zdy_*.list`：自用规则
- `convert-*`：由 meta-rules-dat 的 geosite/geoip 文本转换为 classical 规则

## 自动同步
`.github/workflows/sync-upstream.yml` 每 3 天运行一次（也可手动 workflow_dispatch），按 `upstream.json` 拉取上游。
冲突以本地为准：若 `clash/<文件>` 与 `upstream-snapshots/<文件>` 不同（即手动改过），该文件不会被覆盖。
若想恢复跟随上游，把 `clash/<文件>` 改回与快照一致或删除快照文件。

## 引用示例
```yaml
url: https://gh-proxy.com/raw.githubusercontent.com/luowenfu/Proxy_rule/refs/heads/main/clash/Google.list
```

## 文件与上游
| 文件 | 方式 | 上游 |
|---|---|---|
| `clash/zdy_Globe2.list` | raw | https://raw.githubusercontent.com/luowenfu/ios_rule_script/refs/heads/master/lwf_zdy/rules/Globe2.list |
| `clash/zdy_dev.list` | raw | https://raw.githubusercontent.com/luowenfu/ios_rule_script/refs/heads/master/lwf_zdy/rules/dev.list |
| `clash/zdy_ultramobile.list` | raw | https://raw.githubusercontent.com/luowenfu/ios_rule_script/refs/heads/master/lwf_zdy/rules/ultramobile.list |
| `clash/Crypto.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Crypto/Crypto.list |
| `clash/zdy_crypto.list` | raw | https://raw.githubusercontent.com/luowenfu/ios_rule_script/refs/heads/master/lwf_zdy/rules/crypto.list |
| `clash/PrivateTracker.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PrivateTracker/PrivateTracker.list |
| `clash/Check.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Check.list |
| `clash/ChatGPT.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.list |
| `clash/Claude.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Claude/Claude.list |
| `clash/MetaAi.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/MetaAi.list |
| `clash/Perplexity.list` | convert-geosite | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/perplexity.list |
| `clash/Copilot.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Copilot.list |
| `clash/Gemini.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Gemini.list |
| `clash/Telegram.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.list |
| `clash/Telegram_IP.list` | convert-geoip | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/telegram.list |
| `clash/Twitter.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.list |
| `clash/Whatsapp.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Whatsapp/Whatsapp.list |
| `clash/Facebook.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.list |
| `clash/Instagram.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Instagram/Instagram.list |
| `clash/Amazon.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Amazon/Amazon.list |
| `clash/Apple_CN.list` | convert-geosite | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/apple-cn.list |
| `clash/Apple.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Apple/Apple.list |
| `clash/list_Apple.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Apple.list |
| `clash/Microsoft.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.list |
| `clash/TikTok.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok.list |
| `clash/Netflix.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.list |
| `clash/Netflix_IP.list` | convert-geoip | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/netflix.list |
| `clash/Disney.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disney/Disney.list |
| `clash/HBO.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/HBO/HBO.list |
| `clash/Spotify.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Spotify/Spotify.list |
| `clash/Steam.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Steam/Steam.list |
| `clash/Epic.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Epic/Epic.list |
| `clash/EA.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/EA/EA.list |
| `clash/Blizzard.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Blizzard/Blizzard.list |
| `clash/UBI.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/UBI/UBI.list |
| `clash/PlayStation.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/PlayStation/PlayStation.list |
| `clash/Nintendo.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Nintendo/Nintendo.list |
| `clash/Adobe.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Adobe/Adobe.list |
| `clash/Nvidia.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Nvidia/Nvidia.list |
| `clash/Crunchyroll.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Crunchyroll.list |
| `clash/Reddit.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Reddit/Reddit.list |
| `clash/Groq.list` | convert-geosite | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/groq.list |
| `clash/Grok.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Grok.list |
| `clash/Popcorn.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Popcorn.list |
| `clash/Direct.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Direct.list |
| `clash/PayPal.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/PayPal/PayPal.list |
| `clash/eBay.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/eBay/eBay.list |
| `clash/Private.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Lan/Lan.list |
| `clash/China_Domain.mrs` | raw | https://raw.githubusercontent.com/metacubex/meta-rules-dat/meta/geo/geosite/cn.mrs |
| `clash/China_IP.mrs` | raw | https://raw.githubusercontent.com/metacubex/meta-rules-dat/meta/geo/geoip/cn.mrs |
| `clash/YouTube.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/YouTube/YouTube.list |
| `clash/Google.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.list |
| `clash/Google_IP.list` | convert-geoip | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geoip/google.list |
| `clash/BiliBili.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/BiliBili/BiliBili.list |
| `clash/Synology.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Synology/Synology.list |
| `clash/Cursor.list` | convert-geosite | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/cursor.list |
| `clash/Wise.list` | convert-geosite | https://raw.githubusercontent.com/MetaCubeX/meta-rules-dat/meta/geo/geosite/wise.list |
| `clash/Proxy.list` | raw | https://raw.githubusercontent.com/liandu2024/clash/refs/heads/main/list/Proxy.list |
| `clash/Global.list` | raw | https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/refs/heads/master/rule/Clash/Global/Global.list |
