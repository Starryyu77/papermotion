# PaperMotion Project Plan Fusion

## 背景

新的 `Formula2Video` 项目计划更偏完整生产管线：输入公式，经过多 Agent 理解、脚本、分镜、场景规格、Manim/TTS/Music/PixVerse 并行素材生成，再由 FFmpeg 合成和 QA 输出最终视频。

当前 PaperMotion 计划更偏 Trae Solo 原生 MVP：用 repo 文件作为协作合同，Person A 做 Solo 内部生产流，Person B 做展示网站、PixVerse 生成入口和最终演示体验。

融合后的方向是：

> PaperMotion 是 Formula2Video 的 Trae Solo-native 展示与生产工作台。`production_manifest.json` 管项目级状态，`enriched_scene_spec.json` 管场景级可执行规格，Person B 的 `PaperMotion Workbench` 网站负责展示、触发 PixVerse、预览素材和证明 workflow。

## 关键差异

| 维度 | 当前 PaperMotion 思路 | 新项目计划 | 融合决策 |
| --- | --- | --- | --- |
| 产品形态 | Solo workflow + demo website | 自动公式到视频 pipeline | 保留 Solo-native 工作流，网站作为展示/控制台 |
| 核心合同 | `production_manifest.json` | `enriched_scene_spec.json` | 双层合同：Manifest 是项目 registry，Enriched Scene Spec 是可执行场景 SSOT |
| MVP 重心 | attention demo + Manim + PixVerse + website | M1 先纯 Manim 闭环，再加声音、风格、PixVerse | 当前 hack/demo 仍做网站和 PixVerse，但底层里程碑按 M1-M5 递进 |
| Audio | 有 rhythm/audio slots，但不够具体 | TTS、Music、Assembly/QA 是明确 WP | 纳入正式工作包和 scene spec 字段 |
| Manim 可靠性 | scene specs + render notes | RAG + AST 静态检查 + 自修复 | 先不做 RAG，文档里保留 M5 加固路径 |
| PixVerse | cinematic support, not exact math | 写实层/图生视频，不渲染文字公式 | 完全一致；网站必须体现 Manim exact layer / PixVerse cinematic layer 边界 |
| 风格 | 几何直觉解释，不复制具体创作者 | 3B1B 风格脚本 skill | 改成 3B1B-inspired geometric intuition style，不冒充或复刻个人风格 |

## 融合后的系统架构

```text
用户输入：公式 / paper excerpt / 自然语言
        |
        v
阶段 A：理解与规划层（Person A / Solo MTC，串行）
Intent -> Prerequisite -> Curriculum -> Script -> Storyboard -> Enriched Scene Spec
        |
        v
阶段 B：素材生成层（Person A+B / Solo Code，按场景并行）
Manim exact layer | TTS | Music/SFX | PixVerse cinematic layer
        |
        v
阶段 C：合成与审核层（Assembly，串行）
FFmpeg assembly -> QA review -> final MP4
        |
        v
阶段 D：展示层（Person B）
PaperMotion Workbench website -> focused film workbench + formula overlay + hidden spec/PixVerse inspector + workflow proof
```

贯穿全程：

- `production_manifest.json`: 项目级 registry、任务状态、artifact index、网站展示入口。
- `enriched_scene_spec.json`: 场景级 Single Source of Truth，下游 Manim/TTS/Music/PixVerse/Assembly 各读各字段。
- Pipeline Orchestrator: 只调度、重试、校验和更新状态，不做内容决策。

## 数据合同分层

### 1. Production Manifest

路径：

```text
examples/<demo>/production_manifest.json
```

职责：

- 记录 demo metadata、intent、curriculum、script beats、storyboard 概览。
- 记录 artifact paths、PixVerse job list、asset manifest、edit decision list。
- 给 Person B 网站提供项目级展示数据。
- 指向当前 demo 的 `enriched_scene_spec.json`。

不负责：

- 不作为 Manim/TTS/Music/Assembly 的逐帧/逐秒执行规格。
- 不承载过细的 scene object/action/time contract。

### 2. Enriched Scene Spec

路径：

```text
examples/<demo>/enriched_scene_spec.json
```

职责：

- 唯一承载 scene-level executable spec。
- 每个 scene 必须包含：
  - `timestamp_start_s`
  - `narration`
  - `narration_duration_s`
  - `pacing`
  - `insight_moment`
  - `visual_type`
  - `manim`
  - `tts`
  - `music_cue`
  - `pixverse`
  - `assembly`
  - `qa_checks`
- 下游 Agent 只读取自己字段，避免互相猜测。

字段归属：

| 字段 | 主要消费者 |
| --- | --- |
| `manim.*`, `wait_after_s` | Manim Agent |
| `tts.*`, `narration_duration_s` | TTS Agent |
| `music_cue.*`, `pacing`, `insight_moment` | Music/SFX Agent |
| `pixverse.*`, `visual_type` | PixVerse Agent |
| `timestamp_start_s`, `assembly.*` | Assembly Agent |
| `qa_checks` | QA Agent + Website |

## 工作包映射

| WP | 模块 | 当前归属建议 | MVP 处理 |
| --- | --- | --- | --- |
| WP0 | Pipeline Orchestrator | shared / later | MVP 用文件和 task board 模拟 |
| WP1 | Intent Agent | Person A | 必做 |
| WP2 | Prerequisite + Curriculum Agent | Person A | 必做，使用极简即时原则 |
| WP3 | Script Agent | Person A | 必做，使用几何直觉解释风格和标签 |
| WP4 | Storyboard Agent | Person A | 必做 |
| WP5 | Scene Spec Agent | Person A | 必做，输出 enriched scene spec |
| WP6 | Manim Agent | Person A | 必做，先低清可渲染 |
| WP7 | TTS Agent | Person B / later | MVP 可先用 timed voiceover text |
| WP8 | Music Agent | Person B / later | MVP 可先输出 music cue plan |
| WP9 | PixVerse Agent | Person B | 可做；API 可用，网站提供生成入口 |
| WP10 | Assembly + QA Agent | Person B/shared | MVP 至少做 assembly plan 和网站预览 |
| Website | PaperMotion Workbench demo | Person B | 必做，展示工作流和触发 PixVerse |

## 当前 MVP 决策

当前分支 `person-b-presentation` 不改成完整后端 pipeline 分支。它继续专注 Person B 展示工作，但必须兼容新计划：

1. 网站从 `production_manifest.json` 读取项目/故事线。
2. 网站从 `enriched_scene_spec.json` 读取 scene timing、layer、TTS、music、PixVerse、QA 状态。
3. PixVerse Console 只生成 `visual_type == pixverse` 或 `hybrid` 且 `pixverse` 非空的 cinematic support clips。
4. Film Window 展示 Manim exact layer 或 placeholder。
5. Workflow Window 显示 M1-M5 里程碑，让观众知道系统可以从 MVP 走向完整 Formula2Video pipeline。

## 对 Person B 网站的影响

`PaperMotion Workbench` 保留复古工作站视觉，但收敛成一个主工作台和一个按需打开的 inspector：

- 主工作台：展示 film placeholder/player、scene chapters、formula overlay 和当前解释。
- Context Inspector：展示 `enriched_scene_spec.json` 中当前 scene 的 timing、layers、tts、music cue、pixverse cue、QA checks，并提供 PixVerse support shot 生成入口。

网站不只是“好看的官网”，而是 Formula2Video pipeline 的可视化控制台。

## 里程碑

### M1: 最小闭环

- 输入公式。
- 输出 script/storyboard/enriched scene spec。
- 渲染纯 Manim 无声视频。
- 网站能展示 scene timeline 和 workflow proof。

### M2: 声音

- 加入 TTS 字段和 timed voiceover。
- 检查音画偏差。

### M3: 风格与协同

- Script 带 `[MANIM]`, `[PIXVERSE]`, `[INSIGHT]`, `[HYBRID]` 标签。
- Enriched Scene Spec 通过 schema 校验。
- Orchestrator 开始承担调度和状态更新。

### M4: 全功能

- PixVerse cinematic layer。
- Music/SFX。
- FFmpeg 分层合成。
- Website 预览完整素材状态。

### M5: 质量加固

- Manim RAG golden set。
- AST/LaTeX 静态审查。
- 渲染失败自修复。
- 全流程重试、trace、QA report。

## 安全边界

- Manim owns exact formulas, matrices, graphs, labels, and symbolic transformations.
- PixVerse owns cinematic support, metaphor shots, transitions, and atmospheric motion.
- PixVerse must not render readable equations, matrices, or exact symbolic transformations.
- The house style is geometric intuition explainer. It may be inspired by high-quality educational animation principles, but it should not impersonate a specific creator.

## Immediate Repo Changes

- Add `contracts/enriched_scene_spec.schema.json`.
- Add `examples/attention/enriched_scene_spec.json`.
- Update `contracts/production_manifest.schema.json` with `scene_spec_contract`.
- Update Person B website design doc to read both manifest and enriched scene spec.
- Update task board so Person A owns the enriched scene spec and Person B displays/uses it.
