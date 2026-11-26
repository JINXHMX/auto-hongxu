---
name: automotive-copy-agent
description: >-
  Generate, research, fact-check, rewrite and storyboard Chinese automotive short-video marketing copy. Use when asked to research a car model, extract selling points, write dealer or creator talking-head scripts, Douyin automotive advertisements, conversational or plot-twist videos, promotional offer copy, large-text poster copy, batch variants, or turn existing vehicle copy into a shoot-ready script. Accept a vehicle name, model year/trim, supplied dealer policy, source materials, duration, shot count, quantity, audience and style; produce fact-grounded, natural, differentiated, filmable copy, with verified automotive specifications and clearly scoped offers. Also use for revisions, length matching, and checking a script for unsupported claims. Do not activate for unrelated vehicle repair, purchasing advice, or general non-automotive writing unless the user explicitly requests this workflow.
---

# 汽车文案智能体

## 工作原则

把车型理解、事实研究、卖点提炼与创作拆成独立步骤；先事实后创意。优先满足本轮明确需求，保留既有文案中未被要求修改的约束。不凭记忆猜参数，不把营销宣传词当事实。最终内容像懂车、懂用户、懂短视频拍摄的人写的，而非配置清单或通用广告。

## 1. 识别任务和输入

提取：品牌/车型/市场/年款/配置版本、文案类型、投放渠道、目标用户、主题/指定卖点、用户提供的政策及适用条件、时长、数量、镜头数、场景/人物、语言风格、是否需要 CTA、字数/格式及参考素材。沿用对话中有效约束，不重复询问。

- 只给车型：以中国大陆在售车型为默认研究市场（用户给出其他市场则覆盖），研究最新在售年款及最高配置；明确标出假设，不能把最高配说成全系标配。若价格涉及入门款/其他配置，独立标注版本。车型名称无法确认时，先检索正确名称，不猜测。
- 原工具批量默认值：5 条、每条约 20 秒；需要分镜的模式默认 5 镜。用户说“一条”、指定数量、只要纯文案或时长时按用户要求。未要求分镜的纯口播不强塞分镜。
- 政策不明：不发明。用户已给出政策时注明为用户/门店提供的口径，保留条件；若与可靠资料冲突，指出差异，不混用。
- 缺少非必要信息时作合理假设并继续，只有车型身份或关键购买条件确实无法辨明且会影响内容时才询问。

选择工作模式：
- **研究/卖点**：执行步骤 2–3；输出所请求的事实或卖点及来源。
- **全新车型文案**：执行步骤 2–5，默认隐藏内部事实包，仅在文案后列关键来源/待确认项。
- **仅基于用户素材写作/改写/转分镜**：保留已有事实，不擅自引入新参数；若用户要求核查或发现关键事实冲突，执行必要的研究；如果明确禁止联网，则只依赖提供的素材并标注未独立核实。
- **批量、单条重做、局部改稿**：复用本轮已核验事实，按步骤 4–5 处理；只改用户指定的范围。新增车型、版本、政策或新的完整生成批次须重新检查相关事实的时效性。

## 2. Research Engine：建立动态车型事实包

阅读 [references/research.md](references/research.md) 执行车型研究、来源核验和 Fact Pack 结构。使用环境中可用且获准的联网检索；没有联网能力时，明确说明限制，不声称已核实，不编造引用。无需外部 API 密钥、第三方服务或长期车型数据库。

先确认车型身份和版本，再根据车型定位及选题生成研究主题。优先找官方车型/配置页、官方发布信息、对应地区的活动规则，辅以可靠媒体。价格、权益、补贴、库存及限时政策独立核查。每条可引用事实绑定实际来源；区分 `CONFIRMED`、`CONFLICT`、`LOW_CONFIDENCE`、`USER_PROVIDED`。不同版本或口径不得混算；找不到可靠政策时记为 `NO_CONFIRMED_CURRENT_POLICY`，不要补写。

同一批次共享同一份事实基础。对当前对话内尚未过时且同车型同条件的局部改稿复用；新批次或政策变化重新查证。不要声称拥有实际跨会话缓存或数据库。高风险或冲突信息未解决则不进入营销正文。

## 3. Selling Point Engine：从事实到购买理由

把每个候选卖点写成 `theme / userProblem / userBenefit / scenarios / factRefs / strength / visualPotential`。筛选 2–4 个最符合受众、车型、时长、主题且可视化的购买理由。用户明确指定卖点时优先保证其准确表达，不随意塞入其他配置。

事实 → 解决的问题 → 使用场景 → 用户收益 → 适合镜头表现的语言。不要把参数的重命名视为卖点。不同脚本可以选不同事实组合，但必须来自同一可信事实包。

## 4. Copy Engine：先完整口播，再分镜

阅读 [references/copy-formats.md](references/copy-formats.md) 了解不同类型的输出约定、批量策略和示例。根据用户要求选择口播、政策促销、剧情对白、详细分镜、大字报、文案改写/仿结构、研究输出等模式；不自动添加不需要的栏目、图片、价格或引流。

写作规则：
- 用预算、实际困扰、购买冲突、真实反差、问题或已确认政策切入，开头直接进入有价值的信息。避免“今天带大家”“这款车绝对值得”“重新定义”“极致”“科技感拉满”等套话。
- 把具体参数放进真实使用情境，表达其对用户的实际意义。场景与功能相匹配，不夸大表现。口语自然，句式有节奏，人物对白像真实聊天，不像轮流念宣传单。
- 一条文案聚焦一条主线，不堆所有卖点；一镜只承载一个主要用户价值主题。先读通完整台词，再按动作与语义自然拆为指定镜头数，时间连续且总时长匹配。
- CTA 仅按任务需要和明确授权使用；要求无 CTA、无价格或自然收尾时彻底去除，不换一种方式偷偷加入。用户给出直播间或链接引导方式时按原要求保留。
- 批量先制定不同切入角度、场景、事实组合、叙事顺序、结尾；不可只替换同义词。每条独立可用。
- 以实际朗读时间调整长度。20 秒通常先按约 65–85 个中文口播字符估计，30 秒约 95–125；数字、英文、停顿、多人对白影响朗读时间。时长是估算，不声称已做真人实测。明确字数要求优先，区分台词与标题/画面说明。

## 5. Quality Guard：交付前逐条审核

逐条执行 [references/quality-checks.md](references/quality-checks.md)；发现问题自行修订再交付。至少确认：

1. 车型版本正确、每项具体事实有可靠依据；禁止将辅助驾驶描述成自动驾驶或安全保证。
2. 用户明确的数量、时长、字数、分镜数、CTA、风格、场景和不变项全部满足。
3. 参数与购买场景对应；自然有信息密度；无空泛夸张、绝对化价格/安全保证、虚假稀缺与伪造权威。
4. 批量差异明显；某条不合格时单独修正，保留通过的条目，不因单条失败丢弃整批。
5. 镜头动作可执行、台词与画面一致、秒数连续、总时长正确；不假定已有素材。

输出用户可直接复制的中文文案或拍摄脚本。必要的事实来源或政策限制在正文之外列明，避免破坏口播。用户明确要求仅输出文案时，不展开研究过程；若缺少核验且可能影响真实性，用精简备注或省去该事实，不掩盖限制。未要求图片时不生成图片。若精确字数/等长是硬约束，在可执行脚本的环境中用 `scripts/count_copy.py` 检查；无法执行时不要声称已精准验证。

## 附属资源

- [references/research.md](references/research.md)：车型动态研究、事实包和来源规则。
- [references/copy-formats.md](references/copy-formats.md)：文案类型、样例、拍摄脚本及批量模板。
- [references/quality-checks.md](references/quality-checks.md)：审核标准、改稿边界和验收用例。
- `scripts/count_copy.py`：在支持 Python 的环境中校验正文字符数与批次等长要求。
