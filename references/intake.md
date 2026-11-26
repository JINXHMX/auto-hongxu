# Generation Intake | Default and Custom

## 1. Route the request

Apply this only to new automotive copy-generation batches, not factual research, critiques, modifications of existing copy, selected-item regeneration, or a user who already chose a mode in the active task.

- Bare model name or equivalent model-only invocation: offer exactly one choice between 默认生成 and 自定义生成. Wait for that choice before research and drafting. The recommended option is 默认生成. Its short preview is 5 copies / 20 seconds / 5 lines / integrated marketing / entry starting price and flagship features / varied CTA. 自定义生成 opens only the missing preference questions.
- Explicit default/direct/skip or a request already specifying substantive generation settings: skip the mode gate, respect explicit fields, fill the remaining optional fields from defaults. A user can say "$auto-hongxu <model> 默认生成" for immediate execution.
- Explicit custom mode or a request for a questionnaire: skip the first selector and ask only unanswered settings. If custom settings are already complete, proceed directly.
- A follow-up such as "regenerate number 2" or "change to live-room CTA" preserves the active settings and never reopens the mode gate unless the user requests a new setup.

## 2. Native interface and fallback

Use a host-provided structured user-question tool only when it is actually available in the current turn and allowed by host instructions. This Skill does not install tools or create a custom modal. It defines the requested interaction.

- WorkBuddy: prefer the native question selector when exposed. WorkBuddy Enterprise SDK documents `AskUserQuestion` with questions, headers, options (label/description) and multiSelect. Use the actual exposed tool schema, not a fabricated call or hardcoded SDK invocation. Desktop availability depends on client version, model and mode. See https://www.codebuddy.cn/docs/workbuddy/Changelog and https://cloud.tencent.cn/document/product/1831/137037.
- Codex: prefer `request_user_input` only when exposed and permitted in the current collaboration mode. Follow the tool's schema, typically 1-3 short questions per call and 2-3 mutually exclusive options each; the client may supply free-form Other. Never switch collaboration mode or modify client config on behalf of the user just to show a selector.
- ChatGPT and other hosts: use a native choice/input interface if supplied and allowed. Otherwise use short text choices, e.g. A. 默认生成 / B. 自定义生成, and wait for the user's reply. If host instructions prohibit textual multiple-choice lists, ask one concise natural-language question instead.
- Never simulate a real tool call with a code block or claim a popup was displayed merely because instructions exist. A user who cancels the task should not receive a generated batch; a user who chooses skip/default gets defaults. If the native tool fails, fall back once to text instead of repeatedly invoking it. Respect the host's handling of unanswered optional questions.

## 3. Custom questionnaire

Ask in the user's language. Only ask fields not yet resolved. Group compatible questions (up to the tool's actual limit, preferably 2-3 per interaction); offer recommended defaults and free text where supported. No mandatory questionnaire for a user who chooses default. After answers are collected, fill skipped optional fields from defaults and generate without a redundant confirmation. Do not ask the user for technical field names.

| Setting | Default | Suggested options / input |
|---|---|---|
| copy_type | Integrated marketing | Integrated marketing; offer-led marketing; scenario/dialogue; user-defined |
| count | 5 | 3; 5; 10; custom integer |
| duration_seconds | 20 | 15; 20; 30; custom positive seconds |
| shot_count | 5 | 3; 5; 6; custom positive integer |
| emphasis | Multiple selling points | Integrated; user-selected configuration themes; offer-focused |
| vehicle_scope | Model line | Entry starting price + flagship features; specific trim (ask for name if needed) |
| price_policy | Verified applicable starting price and offers | Include verified price/offers; omit price; user-provided price/offer and eligibility |
| cta | Rotate channels | Rotate; live room; avatar DM; bottom-left link; showroom/test drive; no CTA |
| style | Short, direct, dense sales language | Default sales; high-energy promotional; conversational; user-defined |
| output_format | One copyable text block per script | Plain blocks; detailed storyboard if explicitly requested; poster text |

When the interface allows only 2-3 choices, combine options into broad mutually exclusive categories and ask for a free-text follow-up only when needed. Do not force all ten questions when a shorter selection covers the user's goal. A compact custom interview can first ask quantity, duration and shots, then copy type, price/feature scope and CTA; other style or source details are optional. For model-line scope, the price track and configuration track remain independent; a named trim request narrows the fact pack, and omitting price does not automatically remove CTA.

## 4. Effective request

Merge explicit user instructions > questionnaire answers > existing applicable preferences > defaults. Store the resulting settings only in the active task context. Proceed with research, fact pack, copy and quality checks from SKILL.md. Verify numbers, price eligibility and trim scope, then produce the requested number of clean copy blocks. If the user selects custom details conflicting with one another, ask only the one necessary clarifying question. Do not show questionnaire metadata, result schema, setting summary or technical logs inside the final copy blocks.


## 5. 数据清洗与槽位剥离原则 (引流错位法则)
在摄取原始车型资料时，必须强制切断价格与版本的关联，并将数据重组为以下两个核心独立槽位：
- **`{{hook_price}}`（引流锚点）**：强制且仅能提取全系**最低入门版售价**（或综合优惠后的最低起售价）。提取后，彻底遗忘入门版的减配信息。
- **`{{hero_specs}}`（价值锚点）**：强制且仅能提取该车型**顶配/高配版本**的核心越级配置（如高阶智驾、空气悬架、大屏、座椅通风按摩等）。提取后，彻底遗忘顶配版本的昂贵售价。
