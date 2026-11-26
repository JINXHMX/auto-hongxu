# Auto Hongxu | 汽车文案智能体

**V1.3.0** · [![skills.sh](https://skills.sh/b/JINXHMX/automotive-copy-agent)](https://skills.sh/JINXHMX/automotive-copy-agent)

一套面向中国汽车短视频创作者与经销商的可复用 Agent Skill：动态车型研究 → 事实核验 → 卖点提炼 → 文案创作 → 质量审核。

## 一键安装

技能名称已统一为 `auto-hongxu`。仓库名称正在迁移：当前仍可从原仓库安装；仓库正式改名为 `auto-hongxu` 后，可改用 `npx skills add JINXHMX/auto-hongxu`。现有旧名技能建议先移除再安装新名称，以免重复。

在支持 Node.js（当前 Skills CLI 要求 22.20+）的终端中执行：

```bash
npx skills add JINXHMX/automotive-copy-agent
```

选择需要安装的 AI 客户端，如 Codex、Claude Code、Cursor。默认安装到当前项目；需要全局安装时追加 `-g`。安装前可使用 `--list` 查看技能，并审阅仓库内容。

安装后，在支持 `$` 调用语法的客户端输入：

```text
$auto-hongxu 生成10条华境S的30秒综合营销口播，配置与适用优惠结合，末镜引流。
```

也可直接说“使用汽车文案智能体，生成5条20秒汽车营销文案”。客户端支持自动匹配时，无需显式指定技能名称。不同客户端的触发语法可能不同。

## 免安装使用

支持 Skills CLI 的环境可生成一次性使用提示词（不安装 Skill）：

```bash
npx skills use JINXHMX/automotive-copy-agent@auto-hongxu
```

普通联网聊天 AI 可尝试输入：

```text
加载 GitHub: JINXHMX/automotive-copy-agent 的 ONLINE.md
```

若 AI 无法定位，直接提供 [ONLINE.md 原始文件](https://raw.githubusercontent.com/JINXHMX/automotive-copy-agent/main/ONLINE.md) 并要求读取完整内容后执行任务。无法读取时应说明，不能假装加载成功。网页读取并不等于原生 Skill 安装。

## 更新与校验

```bash
npx skills check
npx skills update auto-hongxu
npx skills add JINXHMX/automotive-copy-agent --list
```

使用者可在 [Skills.sh](https://skills.sh/) 搜索技能；排行榜及收录由平台根据安装活动等因素管理，并非提交仓库后立即保证可搜索。

## ChatGPT 原生导入

[下载 skill.zip](./skill.zip)，在支持自定义 Skills 的客户端中按照平台的导入流程安装。ChatGPT 的技能入口及可用性取决于账户和工作空间。

## V1.3.0 综合营销默认规则

- 默认5篇、每篇20秒、5镜；按实际AI配音反馈校准115–130正文字符，优先120–125，不计标点与空白，包含CTA。
- 每篇一个独立纯文本代码块，每镜一行、无空行、无标题/序号/分镜标签或表格，一键复制。
- 每条优先融合3–4个不同配置/价值维度及可靠适用的价格权益；不按单卖点拆批，不用废话凑字数。
- 最后一镜固定引流；默认批次至少覆盖3类渠道（直播间、头像私信、左下角链接、到店等），用户指定渠道优先。
- 不在台词中插入“部分门店”“以门店为准”等防御性语句。事实和来源内部核验，必要条件保持真实，人工负责最终发布审核。
- 新增字数范围和非空镜段行数校验：`python scripts/count_copy.py copies.json --min-chars 115 --max-chars 130 --lines 5`。

## 车系级价格与配置

默认独立核验车系入门起售价和最高在售配置的卖点，二者可在同篇文案中组合。以“XX万元起”“顶配搭载”“最高可达”等短语保持真实范围，不暗示入门价即可购买顶配配置。明确指定车型版本时按该版本生成。

## 交互式需求设置

- 只输入车型：先选择“默认生成”或“自定义生成”。
- `$auto-hongxu 华境S 默认生成`：直接按5条、20秒、5镜及原营销规则执行。
- `$auto-hongxu 华境S 自定义生成`：按问卷配置数量、时长、镜数、文案类型、价格/配置、引流渠道、风格等。
- 已明确给出生成设置的指令直接执行，后续改稿不重复询问。
- WorkBuddy 优先使用实际可用的原生问答选择器；其企业版 SDK 文档提供 AskUserQuestion。Codex 优先使用允许的 request_user_input。其他客户端没有原生工具时使用简短文字问答。Skill 不能强制客户端显示特定弹窗。
- WorkBuddy 可从技能页面导入本仓库的 `skill.zip`；选择器能否触发仍需实际客户端验证。

官方参考：[WorkBuddy 更新日志](https://www.codebuddy.cn/docs/workbuddy/Changelog) · [WorkBuddy Enterprise SDK 问答工具](https://cloud.tencent.cn/document/product/1831/137037)。

## 功能

| 模块 | 能力 |
|---|---|
| Research Engine | 联网研究车型年款、版本、参数及价格政策 |
| Fact Pack | 来源绑定、事实冲突处理、参数去重 |
| Selling Point Engine | 参数 → 用户痛点 → 价值 → 使用场景 |
| Copy Engine | 口播、营销、剧情对白、拍摄分镜、大字报、批量差异化 |
| Quality Guard | 事实准确性、口语化、字数、广告风险及改稿边界 |

## 文件结构

```text
SKILL.md                     标准技能入口
ONLINE.md                    单文件联网入口
agents/openai.yaml           技能界面元数据
references/                  研究、文案模板及质量审核
scripts/count_copy.py        本地字数校验脚本
skill.zip                    原生 Skill 安装包
VERSION / CHANGELOG.md       版本记录
```

## 边界与维护

本仓库仅提供工作规范，不提供远程模型 API、授权计费或车型数据库。研究和推理由使用者 AI 客户端执行，无需配置发布者的 API Key；联网、工具权限及模型用量由使用者环境决定。生成的车型事实和实时优惠应在发布前复核。公开文件可被阅读；安装前请审阅内容，不运行未经确认的远程脚本。更新 Skill 时应同步更新 ONLINE.md、skill.zip 和版本记录。

CLI 文档：[vercel-labs/skills](https://github.com/vercel-labs/skills) · [Skills.sh 文档](https://skills.sh/docs)
