# PaperMotion Trae Demo Runbook And Presentation Script

This document is the operator-facing guide for demonstrating PaperMotion in Trae Solo.

## 1. Trae Solo Configuration

### Recommended Install Prompt

Paste this into Trae Solo:

```text
请把这个 GitHub 仓库作为 PaperMotion skill pack / SKU 安装到本地工作区：

https://github.com/Starryyu77/papermotion.git

如果可以选择分支，请使用：
person-a-production-workflow

请按照仓库里的 prompts/trae-install-sku.md 执行。
```

### What Trae Should Do

1. Clone the repository.
2. Read `papermotion.sku.json`.
3. Treat `papermotion.sku.json.skills[]` as the authoritative skill list.
4. For each listed `SKILL.md`, read frontmatter `name` and `description`.
5. Register or load the listed skills in Trae.
6. Confirm the root skill is available:

```text
skills/papermotion-research-video/SKILL.md
```

7. Optionally run post-install validation:

```bash
./setup.sh --check-only
```

Installation is considered successful when every listed skill is registered or loadable. `./setup.sh` is only the validation backend, not the product install.

### Skills To Confirm

| Skill | Purpose |
| --- | --- |
| `papermotion-research-video` | Root skill and workflow coordinator |
| `research-video-orchestrator` | End-to-end run coordination |
| `paper-to-visual-brief` | Source material to `input.md` and `mechanism_spec.json` |
| `dynamic-visual-reasoning` | Mechanism to `dynamic_scene_model.json` |
| `math-storyboard-director` | Teaching beats and storyboard |
| `manim-exact-layer` | Deterministic exact-math animation |
| `ai-cinematic-support` | Optional non-exact cinematic support |
| `research-video-qa` | Source fidelity and visual QA |

## 2. Demo Closed Loop

### Demo Goal

Show that PaperMotion can take a formula, decompose its mechanism, create a dynamic scene model, connect it to render artifacts, and preview a research explainer video.

### Input Prompt For Trae

```text
使用 PaperMotion 的 papermotion-research-video root skill，把下面公式做成一个科研解释视频：

Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V

观众：机器学习方向研究生
目标：解释 Q/K/V、score matrix、softmax weights 和 weighted value aggregation
输出：先使用 paper-to-visual-brief 生成或检查 mechanism_spec.json；
然后使用 dynamic-visual-reasoning 生成或检查 dynamic_scene_model.json；
最后展示 examples/attention 里的现有 storyboard、scene spec、Manim render 和 demo video。
不要把网站作为默认产品路径，网站只作为最后展示面。
```

### Expected Output Files

For the attention demo:

```text
examples/attention/input.md
examples/attention/mechanism_spec.json
examples/attention/dynamic_scene_model.json
examples/attention/storyboard.md
examples/attention/enriched_scene_spec.json
examples/attention/production_manifest.json
site/public/videos/attention-demo.mp4
```

Validation:

```bash
./setup.sh --check-only
```

Expected validation result:

```text
examples/adam-optimizer/dynamic_scene_model.json: valid
examples/attention/dynamic_scene_model.json: valid
examples/ddpm-denoising/dynamic_scene_model.json: valid
examples/nerf-volume-rendering/dynamic_scene_model.json: valid
```

### Demo Narrative

1. **Input**: Show the formula `Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V`.
2. **Mechanism Spec**: Open `examples/attention/mechanism_spec.json` and show symbol ledger plus causal steps.
3. **Dynamic Scene Model**: Open `examples/attention/dynamic_scene_model.json` and explain that this is the mechanism-to-3D-dynamic-scene contract.
4. **Storyboard / Scene Contract**: Show `storyboard.md` and `enriched_scene_spec.json`.
5. **Exact Render**: Show `manim/attention_demo.py` and `site/public/videos/scenes/*.webm`.
6. **Final Preview**: Open `site/public/videos/attention-demo.mp4` or click the poster in README.
7. **Generalization**: Show that Adam, DDPM, and NeRF also validate through the same `dynamic_scene_model` schema.

## 3. Presentation Script

大家好，我们今天展示的是 PaperMotion。它不是一个普通的网站，也不是一个只会总结论文的工具。我们的目标是给科研工作者做一个 Trae Solo skill pack，让 AI Agent 能把论文、公式、算法和机制，转成可检查、可复用、可渲染的科研解释视频工作流。

核心问题是：科研内容不是简单画图就能讲清楚。很多内容，尤其是数学公式、模型结构和三维机制，真正困难的是“机制如何变成动态场景”。比如 attention 公式里面的 Q、K、V，不只是几个符号，而是有角色分工、比较关系、归一化过程和信息聚合过程。PaperMotion 做的事情，就是把这些机制拆成文件化、结构化、可验证的中间表示。

我们的流程分成几步。第一步是论文拆解。Trae 本身已经能读论文、识别图片、理解公式，但它不会自动把论文拆成视频生产所需的结构。所以我们用 `paper-to-visual-brief` skill，把输入变成 `input.md` 和 `mechanism_spec.json`。这里会记录符号表、机制步骤、关键公式、误解风险和 claim boundary。

第二步是动态视觉建模，这是项目最核心的部分。我们用 `dynamic-visual-reasoning` skill 生成 `dynamic_scene_model.json`。它不是 storyboard，也不是渲染代码，而是一个 renderer-neutral 的动态场景合约。里面定义了语义实体、视觉对象、空间布局、运动原语、镜头计划、精确层和比喻层的边界。这样 AI 不只是说“画一个好看的动画”，而是明确每个对象为什么出现、怎么移动、代表什么技术含义。

第三步是 storyboard 和 scene contract。我们把动态场景模型转成教学节奏和场景合约，比如 attention 示例里会分成 token context、Q/K/V roles、similarity heatmap、softmax weights、weighted values 几个场景。每个场景都能追溯到源公式和机制步骤。

第四步是渲染层分工。我们把精确数学层和 cinematic support 分开。公式、矩阵、坐标轴、图结构、Q/K/V 标签这些必须由 Manim、Three.js、Blender 或其他确定性 renderer 负责。AI video provider 只能做非精确的氛围、转场、背景和支持镜头，不能生成可读公式，也不能承担科学 claim。这是为了保证科研视频不是“看起来像对的”，而是可以检查、可以验证。

第五步是 assembly 和 QA。最终视频不是黑盒生成出来的，而是由 repo 里的 artifacts 串起来：`mechanism_spec.json`、`dynamic_scene_model.json`、`storyboard.md`、`enriched_scene_spec.json`、rendered clips 和 QA checks。我们可以检查公式是否忠实、符号是否稳定、3D 动作是否真的解释机制、AI support 有没有产生假文字或错误结构。

今天的 demo 会用 scaled dot-product attention：`Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V`。输入是一条公式和目标观众，输出是一组可检查文件，加上一个已经渲染好的 demo video。我们还准备了 Adam、DDPM、NeRF 三个例子，证明这个动态场景模型不是 attention 特化的，而是能覆盖优化过程、生成模型和三维神经渲染。

总结一下，PaperMotion 的定位是：让 Trae Solo 从“能读懂科研材料”进一步变成“能组织科研视频生产”。它的关键技术不是单个网页或单个视频模型，而是 skill pack、文件化合约、动态场景模型、确定性渲染和 QA 边界。这样科研工作者可以从论文或公式出发，得到一个可解释、可检查、可迭代的视频生产流程。

## 4. Technical Talking Points

### Skill Pack Layer

`papermotion.sku.json` is the install manifest. Trae reads the exact `skills[]` list and loads each skill by frontmatter metadata. This makes PaperMotion portable as a GitHub-delivered skill pack.

### Dynamic Scene Model

`dynamic_scene_model.json` is the core IR. It separates:

- semantic units: entities, operators, states, relations, invariants;
- visual model: objects, spaces, encodings, layout constraints;
- dynamic model: beats, states, transitions, motion primitives;
- camera model: shots, movement, focus targets;
- exactness policy: what must be deterministic vs. what can be metaphorical;
- renderer plan: Manim, Three.js, Blender, Remotion, FFmpeg, optional AI video.

### Renderer Boundary

Exact scientific content goes to deterministic tools. AI video is optional support only. This prevents fake formulas, unstable labels, and visually plausible but technically wrong scenes.

### Validation

`contracts/dynamic_scene_model.schema.json` defines the shape of the IR, while `scripts/validate_dynamic_scene_model.py` also checks semantic references, duplicate IDs, layer exactness consistency, and dangling object refs.
