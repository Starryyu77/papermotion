# Agent Coordination And PixVerse Integration

## Core Answer

Yes, PaperMotion needs a scheduling layer, but it should be a lightweight Producer / Orchestrator Agent, not a heavy backend.

The Orchestrator Agent does not write every artifact itself. Its job is to maintain a shared `production_manifest.json`, assign agent tasks, detect conflicts, and decide when a stage is ready for the next agent.

The coordination pattern should be:

```text
Agents do specialist work.
The Production Manifest is the shared contract.
The Orchestrator Agent updates task state and resolves conflicts.
Trae Solo is the workspace where all of this runs.
```

This solves the exact coordination question:

- The Teaching Script Agent can know which visual objects may need PixVerse because it writes `visual_asset_requests` into the manifest.
- The PixVerse Asset Agent can respond with `asset_status`, `expected_duration`, `style_risk`, and generated paths.
- The Music & SFX Agent can know where to slow down because the script and storyboard write `beat_markers`, `pacing_intent`, and `emphasis_level`.
- The Scene Spec Agent can know which objects are Manim-exact, PixVerse-cinematic, or static website assets because every scene has a `render_layer`.

## Important Style Boundary

The goal should not be to impersonate 3Blue1Brown or copy a living creator's exact personal style. Instead, create a reusable "geometric intuition explainer" style guide inspired by public educational-animation principles:

- Start from a felt confusion, then reveal structure.
- Use stable colors for stable meanings.
- Prefer geometric intuition before symbolic manipulation.
- Introduce only one new abstraction at a time.
- Keep prerequisite explanations minimal and just-in-time.
- Use visual continuity: objects transform instead of disappearing.
- Let narration point attention, not restate everything visible.

This is safer, more controllable, and easier for agents to follow than "write exactly like 3Blue1Brown."

## Final Agent Pipeline

### 0. Producer / Orchestrator Agent

Purpose:
- Owns `production_manifest.json`.
- Creates task board entries.
- Freezes stage outputs before downstream work.
- Resolves cross-agent conflicts.
- Runs acceptance checks.

Key outputs:
- `examples/<demo>/production_manifest.json`
- `solo/task-board.md`
- Updated `memory/active/current.md`

### 1. Intent Agent

Purpose:
- Parse the user's goal, target audience, desired depth, time budget, and final output type.
- Identify the central mechanism and the one thing the viewer must understand.

Output section:
- `intent`

Must answer:
- What is the learner trying to understand?
- What counts as success after watching?
- Which paper/formula area is in scope?
- What is explicitly out of scope?

### 2. Prerequisite Graph Agent

Purpose:
- Build a prerequisite graph, not a full textbook.
- Mark which symbols/concepts are blockers versus optional background.

Output section:
- `prerequisite_graph`

Just-in-time rule:
- Insert a short "by the way" only when a symbol or concept truly blocks the next step.
- Each inserted prerequisite gets at most one compact explanation unless marked as critical.

### 3. Curriculum Agent

Purpose:
- Sort concepts into the order that minimizes cognitive load.
- Decide when to delay definitions until the moment they become necessary.

Output section:
- `curriculum_plan`

Required fields:
- Concept order.
- Prerequisite insertion points.
- Concepts intentionally skipped.
- "Do not explain yet" notes.

### 4. Teaching Script Agent

Purpose:
- Write the teaching script in a geometric-intuition explainer voice.
- Convert mechanism into a narrative with beats.
- Declare visual asset needs early.
- Declare rhythm and slowdown points.

Output sections:
- `script.beats`
- `visual_asset_requests`
- `rhythm_map`

Key rule:
- The script should not only say words. It should mark the teaching intention of each beat:
  - reveal
  - compare
  - slow down
  - compress
  - surprise
  - misconception repair
  - recap

This is how Music/SFX and Scene Spec know where pacing must change.

### 5. Distillation / Style Agent

Purpose:
- Convert the raw script into the house style:
  - plainspoken but precise
  - vivid geometric metaphors
  - sparse "just-in-time" prerequisites
  - stable symbol references
  - low cognitive load

Output section:
- `style_pass`

The style agent should revise the script, not change the mechanism.

### 6. Storyboard Agent

Purpose:
- Create high-level scenes from the final script beats.
- Decide the scene sequence, major visual metaphor, and chapter labels.

Output section:
- `storyboard.scenes`

Each scene should include:
- Scene ID.
- Linked beat IDs.
- Learning objective.
- High-level visual description.
- Required assets.
- Approximate duration.
- Pacing intention.

### 7. Scene Spec Agent

Purpose:
- Convert storyboard scenes into precise visual specifications.
- Define coordinate systems, objects, camera moves, animation sequence, labels, colors, and timing.
- Specify what becomes Manim code and what becomes PixVerse material.

Output:
- `examples/<demo>/scene_specs/<scene_id>.json`
- Updates `production_manifest.scenes[*].scene_spec_path`

Render layer classification:
- `manim_exact`: formulas, matrices, arrows, geometric transforms, graphs, symbol changes.
- `pixverse_cinematic`: realistic or textured conceptual objects, atmospheric shots, transitions, metaphorical environments.
- `static_asset`: diagrams, icons, still frames.
- `website_only`: UI explanations and interactive chapter content.

Hard rule:
- PixVerse must not be asked to render exact formulas, matrices, or symbolic transformations. Manim owns exact math.

### 8. Manim Code Agent

Purpose:
- Generate Manim Python from scene specs.
- Use exact math, stable colors, repeatable timing, and repairable scene blocks.

Output:
- `manim/<demo>_demo.py`
- Manim MP4 render
- `examples/<demo>/render_notes.md`

### 9. Voiceover Agent

Purpose:
- Generate voiceover script and audio timing from script beats.
- Align sentence boundaries to scene timing.

Output sections:
- `voiceover.lines`
- `audio_manifest.voiceover`

For MVP:
- If real TTS is not ready, produce a timed voiceover script and use browser/demo captions.

### 10. Music & SFX Design Agent

Purpose:
- Use `rhythm_map` and scene timings to design music and effects.
- Mark where the video should slow down, where a reveal needs silence, and where a transition needs a small accent.

Output sections:
- `audio_manifest.music`
- `audio_manifest.sfx`

Coordination rule:
- Music should follow the teaching rhythm. It should not force the animation to move faster.

### 11. PixVerse Asset Agent

Purpose:
- Generate cinematic support assets from approved asset requests.
- Use PixVerse for explanatory objects, transitions, textured metaphors, or atmospheric shots.

Output:
- `pixverse_jobs`
- `asset_manifest`
- Generated video URLs or downloaded files

API reality:
- PixVerse Platform API is asynchronous.
- Requests use an API key and `Ai-trace-id`.
- A generation request returns `video_id`; status must be polled until success.
- Image-to-video supports static images / image IDs and motion prompts.
- Pricing depends on model, quality, duration, and audio.

Sources:
- https://docs.platform.pixverse.ai/pixverse-api-llm-txt-2109771m0
- https://docs.platform.pixverse.ai/image-to-video-882971m0
- https://docs.platform.pixverse.ai/image-to-video-generation-13016633e0
- https://docs.platform.pixverse.ai/pricing-796039m0

Recommended usage:
- Generate 3-5 second cinematic clips.
- Prefer image-to-video from Manim stills or storyboard keyframes.
- Use PixVerse for moments like:
  - abstract "tokens entering a transformer layer"
  - a conceptual attention spotlight
  - transition from raw text to mathematical structure
  - cinematic intro/outro

Avoid:
- Asking PixVerse to render readable equations.
- Asking PixVerse to preserve exact matrices.
- Using PixVerse clips that contradict the Manim explanation.

### 12. Assembly / Editor Agent

Purpose:
- Combine Manim, PixVerse clips, voiceover, music, and SFX according to the edit decision list.

Output:
- `examples/<demo>/edit_decision_list.json`
- final MP4 in website assets

### 13. Website Agent

Purpose:
- Present the final video and the workflow.
- Make chapters clickable.
- Expose selected artifacts so viewers can trust the transformation.

Output:
- `site/`

## Coordination Contract

Every agent reads and writes the same manifest:

```text
examples/<demo>/production_manifest.json
```

The Orchestrator Agent owns the canonical version. Specialist agents may propose changes, but cross-cutting changes must go back through the Orchestrator.

## How Script Knows PixVerse Asset Needs

Use a two-pass process:

### Pass 1: Script Draft With Asset Requests

The Teaching Script Agent writes each beat with:

- `spoken_text`
- `teaching_intent`
- `visual_need`
- `pixverse_asset_candidate`
- `pacing_intent`

Example:

```json
{
  "beat_id": "b03",
  "spoken_text": "Now every query asks: which keys feel most relevant to me?",
  "teaching_intent": "reveal",
  "visual_need": "attention as spotlight over token field",
  "pixverse_asset_candidate": {
    "needed": true,
    "type": "cinematic_transition",
    "prompt_intent": "a field of glowing token tiles, one query emits a soft searchlight across related tokens",
    "duration_seconds": 4
  },
  "pacing_intent": "slow_down"
}
```

### Pass 2: Asset Feasibility And Script Lock

The PixVerse Asset Agent reviews all candidates and responds:

- approved
- rejected
- replace_with_manim
- replace_with_static_asset
- generation_pending

Then the Orchestrator freezes the script and storyboard.

This means the writer can request PixVerse early, but final production only depends on approved assets.

## How Music Knows Where To Slow Down

The script and storyboard must produce a `rhythm_map`.

Example:

```json
{
  "beat_id": "b05",
  "scene_id": "s03",
  "time_intent": "slow_reveal",
  "target_duration_seconds": 8,
  "music_energy": "low",
  "sfx": ["soft_hit_on_heatmap_reveal"],
  "silence_before_seconds": 0.4,
  "reason": "viewer must notice that scaling prevents the softmax from becoming too sharp"
}
```

The Music & SFX Agent uses this map. The Manim Code Agent also uses it for animation timing. That keeps video rhythm, narration, and sound aligned.

## Recommended Data Flow

```text
Intent Agent
  -> intent
Prerequisite Graph Agent
  -> prerequisite_graph
Curriculum Agent
  -> curriculum_plan
Teaching Script Agent
  -> script beats + visual_asset_requests + rhythm_map
Style Agent
  -> revised script, same beat IDs
Storyboard Agent
  -> storyboard scenes
Scene Spec Agent
  -> scene_specs/*.json + render_layer classification
PixVerse Asset Agent
  -> pixverse_jobs + asset_manifest
Manim Code Agent
  -> exact math animation
Voiceover Agent
  -> voiceover timing
Music/SFX Agent
  -> audio_manifest
Assembly Agent
  -> final video
Website Agent
  -> demo surface
```

## What To Build In The 3-Hour MVP

Do not build all agents as software services. Build them as Trae Solo prompt stages plus file contracts.

Minimum for demo:

1. `production_manifest.json`
2. one `scene_specs/*.json`
3. Manim render for exact formula layer
4. one PixVerse job spec for a cinematic support clip
5. website section showing the agent workflow

This gives a credible product story without overbuilding.
