# Proxy_rule

OpenClash / Mihomo 用的规则仓库（公开）。

## 目录

| 路径 | 说明 |
|------|------|
| `mrs/` | 来自 [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) **meta** 分支的 `.mrs`。命名：`geosite_<分类>.mrs` / `geoip_<分类>.mrs`（`geolocation-!cn` → `geolocation-not-cn`，`category-ai-chat-!cn` → `category-ai-chat-not-cn`）。 |
| `zdy/blackmatrix7/` | 有上游 [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script) 的自定义 `.list`（可与 meta 做差集后同步）。 |
| `zdy/liandu2024/` | 有上游 [liandu2024/clash](https://github.com/liandu2024/clash) 的自定义 `.list`。 |
| `zdy/zdy/` | **纯本地自定义**，无上游、不进 `upstream.json`（Crypto、Dev-GitHub、Globe、PT-Tracker、UltraMobile）。 |
| `upstream.json` | 声明 `mrs/` 与可同步 `zdy/` 的来源。 |
| `upstream-snapshots/` | 上次同步的上游快照（用于对比 / 合并）。 |
| `scripts/sync.py` | 同步脚本；GitHub Actions 约每 3 天跑一次（也可手动 workflow_dispatch）。 |

## 同步规则

- **mrs**：按 `upstream.json` 拉取；若本地文件与快照不同（说明改过），**整文件保留本地**，仍更新快照。
- **zdy（blackmatrix7 / liandu2024）**：
  - 声明了 `geosite`：用上游 list 对 meta 同名 geosite 做**差集**后再写入；
  - `geosite` 为空：上游 **全量**写入；
  - 与本地 **按条合并**：上游新增并入；本地多出来的保留；同一条冲突以**本地为准**。
- **zdy/zdy/**：不同步，只手改。

## 在 YAML 里怎么引用

```
# 公共规则 → mrs（behavior: domain / ipcidr，format: mrs）
https://gh-proxy.com/raw.githubusercontent.com/luowenfu/Proxy_rule/refs/heads/main/mrs/geosite_openai.mrs

# 自定义 → zdy（behavior: classical，format: text）
https://gh-proxy.com/raw.githubusercontent.com/luowenfu/Proxy_rule/refs/heads/main/zdy/blackmatrix7/Youtube_zdy.list
https://gh-proxy.com/raw.githubusercontent.com/luowenfu/Proxy_rule/refs/heads/main/zdy/zdy/Globe_zdy.list
```

命名约定：

- 公共：`服务名 / Domain`（或 `/ IP`）→ `mrs/`，锚点 `*domain` / `*ip`
- 自定义：`服务名_zdy / Domain` → 对应 `zdy/.../服务名_zdy.list`，锚点 `*class`
- 同一服务时，`_zdy` 必须排在同名 mrs **前面**
- 公共规则不要写成 list，也不要再用 `clash/` 目录

## zdy 与 meta 的关系

- meta 有对应分类：配置里保留 mrs；多出来的域名进 `*_zdy.list`（差集）。
- meta 无对应：整段只进 zdy（如 Copilot、Direct、Proxy、Crunchyroll 等，现位于 `zdy/liandu2024/` 或 `zdy/zdy/`）。
- **Globe**：主体用 meta `geolocation-!cn` → `mrs/geosite_geolocation-not-cn.mrs`；额外自定义用 `Globe_zdy` → `zdy/zdy/Globe_zdy.list`，排在 Globe mrs 前。
- **AI 兜底**：`Ai-Catchall / Domain` → `mrs/geosite_category-ai-chat-not-cn.mrs`（meta `category-ai-chat-!cn`），策略组「兜底漏网 AI」，排在各精细 AI 规则之后。

## 当前 zdy 文件一览

**blackmatrix7（差集同步）**  
Adobe、Blizzard、Claude、EA、Epic、Instagram、Nintend、Nvidia、PayPal、UBI、WhatsApp、Youtube、eBay

**liandu2024**  
差集：Apple、Gemini  
全量：Copilot、Crunchyroll、Direct、MetaAI、Popcorn、Proxy、TEST

**纯本地 `zdy/zdy/`**  
Crypto、Dev-GitHub、Globe、PT-Tracker、UltraMobile
