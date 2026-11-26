# 质量控制、修改边界与验收案例

## 交付检查

| 检查项 | 通过条件 | 不通过时处理 |
|---|---|---|
| 车型与来源 | 型号、年款、市场、配置和工况一致，关键技术有来源 | 查证、区分或删掉 |
| 流畅度与合规双重校验 | 检查配置展示与起售价之间是否连贯自然，是否成功使用了“本车系提供了……”、“你可以体验到……”等融合推介话术，且起步价保持唯一。 | 如有干瘪生硬的“仅限高配版”、“不包含在入门版内”、“具体配置以门店为准”的播报，必须退回重写，改用浑然一体的车系推介语境。 |
| Intake | Bare-model new request gets one mode selector; direct/default/fully specified requests skip; custom mode respects answered fields | Route correctly, do not repeatedly ask, and use text fallback if native question tools are unavailable |
| 政策 | 内部记录时间、地区、版本和来源；口播直接且不扩大优惠范围 | 精简必要真实条件或换掉不可靠优惠，不写防御性套话 |
| 具体性 | 关键卖点落到事实与场景 | 换成已确认的购买理由 |
| 综合营销 | 多个有购买价值的真实事实；通常3–4个价值维度，政策主导型可集中于购车权益和至少2个相关产品维度 | 重组事实，不按单卖点拆批、不硬塞非核心参数 |
| 动态排序 | 政策主导家庭车优先有效购车权益、舒适座舱及家庭空间；功率、扭矩、零百和悬架按需 | 删除非核心堆砌，补足已核验的权益及家庭价值，保持价格和配置范围清晰 |
| 表达 | 前3秒直接抛利益点；短、准、直的销售口语，删除虚构体验、铺垫长句和空话 | 逐句压缩，保留事实、条件与收益 |
| 安全与广告 | 不把辅助驾驶当无人驾驶；不承诺零风险、绝对性能或无根据最优/最低 | 删掉或改为有证据的限定表述 |
| CTA | 默认每条最后一镜/末句独立引流，只含明确行动；仅明确无CTA、自然收尾或非营销例外 | 补独立CTA；默认5条轮换至少3类引流渠道，指定渠道优先；不宣称实际直播或链接已验证 |
| 批次 | 数量正确，每条综合且完整，开头/事实组合/政策顺序实质不同 | 只修未通过条目 |
| 字数/时长 | 默认20秒115–130正文字符，目标120–125；按用户实测配音校准 | 增补真实卖点或删冗词，再检查，不把字符数当实测时长 |
| 分镜 | 秒数连续、镜头数准确、台词和动作匹配、可拍摄 | 调整台词/镜头而非硬切 |
| 输出格式 | 默认每篇独立纯文本代码块，5行台词无空行、无序号/标题/分镜标签/防御性语句 | 清除多余内容与标签，不在台词块内写审核备注 |

特别注意：不要凭车型宣传图推断未证实的功能；驾驶辅助识别、接管、泊车能力应保持真实操作前提，避免“兜底”“绝不会撞”“可以不用管”这种保证。法律和地方广告规范可能变化，不能宣称已完成法务审核；如涉具体合规要求，可依据有效官方规定核查。

## 精确字数

如有 Python 环境，将各条正文写入 JSON 数组（每项为字符串），运行：

```bash
python scripts/count_copy.py copies.json --min-chars 115 --max-chars 130 --lines 5
```

精确字数使用 `--target N --equal`。`--min-chars`/`--max-chars` 检查范围；`--lines` 检查非空行数并拒绝首尾或中间空白行。`--include-punctuation` 改为统计除空白外全部字符；`--equal` 检查条目等长。检查不通过时只改正文，再核验。字数统计是字符统计，不等同朗读速度，数字与英文字母逐字符计数。不要自动去掉正文标点或改动口语节奏，只在统计时排除标点。脚本未运行时不要宣称机械计数通过。

## 验收案例（用于使用后迭代；不是声称已实测）

1. 输入：“某品牌某车型，写5条20秒口播。”预期：先验证车型，5条不同综合角度，各115–130正文字符，每篇独立5行代码块；有可靠权益则融入；末行CTA至少轮换3类渠道，无依据不编价格。
2. 输入：“商用车，10条，每条80字，只给这些政策素材，不要任何引流。”预期：仅采用提供的优惠口径，10条无 CTA，正文严格等长；默认不附统计说明。
3. 输入：“把这段口播做成30秒、5个镜头，主播坐车内，给画面、机位、台词和字幕，不要图片。”预期：5镜时间连续到30秒，主播车内为主，少量合理B-roll，最后一镜为CTA，输出表格，不生成图像。
4. 输入：“改成妈妈和小孩的对话，自动泊车自然收尾。”预期：口语化对白、自然动作、真实功能限制，无硬促销及不安全演示。
5. 输入：“最新款最低价多少？写紧急清库文案。”预期：独立查价格、版本和活动；无可靠清库信息不编造，不写虚假稀缺；用户提供政策时标注来源和限制。
6. 输入：“其他文案不动，只把第二条换一种切入角度。”预期：保留已核验的事实基础和其他条目，返回修订的第二条，除非用户要整批。
7. 输入：“不要联网，按我发的文案改。”预期：不检索、不增加未提供参数，保留原约束，必要时提示事实未独立核验。

8. 输入：“默认营销，已提供六座、座椅通风加热、CLTC纯电续航、置换政策，生成5条20秒。”预期：每篇融合不同维度和适用权益，直接短句，末镜CTA；禁止一篇只讲座椅或续航。
9. 输入：“只介绍座椅，不要CTA。”预期：尊重单点与无引流例外，不强制综合。
10. 输入：“生成3条口播，只要纯文字，最后点击左下角链接。”预期：不加镜头号或画面说明，每条最后一句是指定引流，不在其后补卖点。

11. 输入：“只给车型，按默认生成。”预期：没有文案标题、分镜号、空白行、表格或防御性话术；默认5个代码块分别5行；每篇115–130字符，末行轮换直播间、头像私信、左下角链接和到店等。
12. 输入：只查到地区性促销且受众不明确。预期：不出现“部分门店”等话术，不把局部优惠写成普惠；用其他确认配置补足字数。
13. Fresh request: "$auto-hongxu <model>" without settings. Expected: one default/custom selector before research; native question tool only if actually exposed and allowed, otherwise concise text choices. No generated scripts until mode selected.
14. "$auto-hongxu <model> 默认生成". Expected: skip all optional questions; generate 5 x 20 seconds x 5 lines under the existing defaults.
15. Explicit custom mode: choose 10 copies, 30 seconds, 6 lines, live-room CTA, no price. Expected: do not re-ask known fields; fill skipped options with defaults; output 10 six-line blocks, each about 170-195 characters, all ending in the chosen CTA, no price.
16. Fictional line has a 149,800 yuan entry trim and flagship-only rear entertainment. Expected: starting-price hook and naturally worded version choice can coexist without 高配/顶配 labels; reject both explicit and implied claims that the entry trim has that screen. A requested entry-trim-only script omits the flagship-only feature.
16a. User dislikes 高配搭载/顶配配备 wording. Expected: use “提供双电机四驱版本”等自然表达；明确版本后直接说“配备/带/搭载”。全系词只用于确实全系配置。不能通过省略必要的配置适用范围让消费者误认起售价包含该功能。
17. Custom mode in a host without native question tools: use concise sequential text choices, not invented tool calls or claims of popup display. A follow-up revision never repeats the generation-mode gate.

18. 输入：家庭舒适型SUV，用户要求政策主推。预期：有效权益优先，舒适座舱和家庭空间是主要产品卖点；不为覆盖维度堆砌扭矩、加速和悬架。没有可靠优惠时改用已确认卖点。
19. 输入：希望减少“想要……也有对应版本可选”之类长句。预期：用已核验版本名称或简洁选择范围引入一组配置，随后直接写带、配备、搭载；不通过隐藏实际配置范围误导消费者。

## 迁移范围

本 Skill 以 2026-09-05 的汽车短视频文案生成工具 V3 项目交接设计为基础，结合汽车口播和拍摄脚本的实际使用习惯。原交接时 V3 Research/Copy Engine 的完整业务实现尚未验收；这里将其设计迁移为对话内的工作规范，不声称完全复刻当前服务器源代码、原始系统提示词或线上运行状态。不依赖原 Web 前端、第三方模型 API、SSH、部署、数据库、登录、会话缓存；不得请求或保存原项目密钥、私钥和服务器凭据。当前可用联网能力由宿主环境提供，无法联网时诚实降级。
