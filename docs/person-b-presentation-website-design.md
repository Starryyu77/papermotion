# Person B Presentation Website Design

## Product Frame

Person B owns the public-facing demonstration layer for PaperMotion. Person A owns the Trae Solo production workflow: paper understanding, mechanism specs, storyboard, scene specs, and Manim exact renders. The website should make that workflow visible, usable, and memorable.

The site should feel like a retro technical desktop environment: a focused `PaperMotion Workbench` where a viewer can inspect the formula-to-film workflow, play the current film draft, and open deeper scene/PixVerse details only when needed.

This is not a generic landing page. The first viewport is the product demo.

## Recommended Direction

Use a `PaperMotion Workbench` aesthetic:

- Inspired by early desktop OS interfaces such as classic Mac OS, early Mac OS X Aqua, and Windows 98.
- Do not copy Apple, Microsoft, Finder, Windows, or system icons directly.
- Create a fictional retro research workstation for paper-to-film workflows.
- Keep it professional enough for a demo, but memorable enough to stand apart from normal AI SaaS pages.

The visual target is:

```text
retro desktop UI + cinematic AI production console + paper/math artifact inspector
```

## Theme Options

### Option A: Aqua Research Workbench

Use this as the default recommendation.

- Blue-gray desktop wallpaper with subtle brushed bands or soft radial lighting.
- Glossy title bars, rounded window buttons, translucent panels used sparingly.
- Top menu bar with compact desktop commands.
- Bottom dock-like shelf with app icons for `Formula`, `Film`, `PixVerse`, `Manifest`, and `Solo`.
- Best fit when we want the site to feel like a polished old creative workstation.

### Option B: Win98 Lab Console

Keep this as a possible alternate skin.

- Flat gray panels, beveled borders, pixel checkboxes, taskbar, start-menu-like launcher.
- Higher density, more utilitarian, very clear hierarchy.
- Best fit when we want the site to feel more hackable and tool-like.

### Final Choice

Start with Option A, but borrow the legibility and control density of Option B. The MVP should look like a classic creative workstation, not a parody desktop or literal operating-system clone. Keep visible product language on PaperMotion, not on an OS brand.

## First Viewport Layout

The first viewport should show one working desktop workbench, not a marketing hero and not a scattered multi-window dashboard.

Required regions:

1. `Menu Bar`
   - Left: `PaperMotion` plus one primary inspect command.
   - Right: current demo name, render status, clock-style timestamp.

2. `Focused Film Workbench`
   - Background texture or wallpaper.
   - One large active window dominates the screen.
   - Shows Manim exact render or a placeholder player.
   - Has classic window controls.
   - Includes scene title, timecode, and chapter rail.

3. `Formula Overlay`
   - Shows `Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V`.
   - Symbol ledger with stable colors for Q, K, V, softmax, scaling, and weights.
   - Clickable formula tokens update the current explanation.

4. `Workflow Strip`
   - Compact status row under the film workbench.
   - Shows the file-backed pipeline in one line:
     `Manifest -> Enriched Scene Spec -> Manim/PixVerse`.
   - Offers `Open Inspector` as the single expansion path.

5. `Hidden Context Inspector`
   - Closed by default so the page has a clear visual focus.
   - Tabs expose Formula, Spec, and PixVerse detail.
   - Shows PixVerse jobs from the manifest.
   - Allows selecting a scene and generating a support shot.
   - Displays `queued`, `generating`, `polling`, `ready`, `failed`, or `fallback`.
   - Shows the active scene from `examples/attention/enriched_scene_spec.json`.
   - Displays timing, narration duration, visual type, Manim layer, TTS cue, music cue, PixVerse cue, assembly layer, and QA checks.

## Core User Story

As a viewer, I should immediately understand that PaperMotion turns a paper/formula into an inspectable production pipeline and a finished explainer film.

The main demo path:

1. Viewer lands on `PaperMotion Workbench`.
2. Film window is already open with the attention demo selected.
3. Viewer clicks scene chapters.
4. Formula window updates to explain the active symbol or transformation.
5. PixVerse console shows cinematic support shots for selected scenes.
6. Viewer can click `Generate Support Shot` to call PixVerse through our backend.
7. Generated clips appear in the queue and can be previewed or assigned to a scene.

## Functional Requirements

### Demo Player

- Play/pause current film draft or placeholder.
- Chapter rail synced to manifest scenes.
- Scene status labels:
  - `planned`
  - `manim-ready`
  - `pixverse-ready`
  - `assembled`
- If no MP4 exists yet, show a styled placeholder that names the expected video path.

### Formula And Symbol Ledger

- Display the attention formula prominently.
- Color symbols consistently:
  - Q: query signal
  - K: key signal
  - V: value signal
  - QK^T: similarity matrix
  - sqrt(d_k): scaling stabilizer
  - softmax: normalization
- Clicking a symbol should update:
  - short explanation
  - linked scene
  - Manim layer note
  - PixVerse boundary note, if relevant

### Manifest Inspector

- Read from `examples/attention/production_manifest.json`.
- Surface:
  - project title and status
  - scenes
  - visual asset requests
  - PixVerse jobs
  - rhythm map
  - artifact paths
- The UI must make the file-backed workflow obvious.

### Enriched Scene Spec Inspector

- Read from `examples/attention/enriched_scene_spec.json`.
- Treat it as the scene-level single source of truth for downstream execution.
- Surface for the active scene:
  - `timestamp_start_s`
  - `duration_s`
  - `narration_duration_s`
  - `visual_type`
  - `manim.scene_class`
  - `tts.text`
  - `music_cue`
  - `pixverse.job_id`
  - `assembly`
  - `qa_checks`
- The inspector should help viewers understand that the system is not just generating a video, but compiling structured scene instructions.

### PixVerse Generate Panel

- Frontend must not expose the API key.
- Frontend calls a backend route such as:
  - `POST /api/pixverse/generate`
  - `GET /api/pixverse/status/:video_id`
- Generate flow:
  1. Select a manifest PixVerse job.
  2. Confirm prompt and negative prompt.
  3. Submit generation.
  4. Show trace ID and video ID.
  5. Poll status.
  6. Save result URL/path into UI state.
  7. Mark the clip as preview-ready.
- The route should reject jobs that ask PixVerse to render exact formulas, matrices, or readable symbolic transformations.

### Workflow Proof

- Show that Trae Solo is the production cockpit, but the website is the presentation surface.
- Include a compact process strip:
  - `Solo MTC`
  - `Scene Specs`
  - `Manim Exact Layer`
  - `PixVerse Cinematic Layer`
  - `Final Demo Site`
- Every process step should point to a repo artifact or a planned artifact.

## Interaction Model

### Desktop Metaphor

- Windows can be visually layered.
- MVP does not need full free dragging if time is tight.
- Clicking a window brings it to front.
- Dock/taskbar icons toggle or focus windows.
- Menu items can open small dropdowns for polish, even if only a few actions are active.

### Main Interactions

- `Scene chapter click`: updates video chapter, formula note, PixVerse job focus, and workflow stage.
- `Formula token click`: highlights the linked scene and shows explanation.
- `Generate Support Shot`: sends selected PixVerse job to backend API.
- `Preview Result`: opens generated clip inside a small media viewer window.
- `Inspect Manifest`: opens a code-like artifact window with compact JSON sections.

### Empty And Loading States

- If Person A artifacts are missing, show a retro file placeholder, not blank UI.
- If PixVerse is still generating, show a progress bar and polling status.
- If PixVerse fails, show the failed trace ID and keep a fallback card.

## Motion Design

Motion should feel like an old desktop OS made responsive, not like a modern flashy landing page.

### Boot Sequence

- Duration: 600-900ms total.
- Sequence:
  1. Desktop background fades in.
  2. Menu bar slides down by 8-12px.
  3. Main film window opens with a quick scale from 0.98 to 1.
  4. Secondary windows stagger in by 40ms each.
- Skip or reduce this if `prefers-reduced-motion` is enabled.

### Window Focus

- Duration: 120-180ms.
- Active window title bar brightens.
- Window raises with a small shadow change.
- Avoid large movement; focus changes should feel crisp.

### Menu Dropdowns

- Duration: 100-140ms.
- Use quick opacity and 4px vertical motion.
- Menu highlight uses classic selected-row treatment.

### PixVerse Queue

- `queued`: static row with dotted border.
- `generating`: horizontal progress barber-pole or low-frame shimmer.
- `polling`: blinking status pixel every 700ms.
- `ready`: row flashes once, then shows a preview affordance.
- `failed`: red/amber system dialog styling with retry action.

### Scene Change

- Duration: 220-320ms.
- Formula highlight crossfades.
- Chapter rail indicator slides.
- PixVerse job focus updates after a 40ms stagger.
- Keep motion synchronized so it feels like one state change.

### Result Preview

- Generated clip opens in a small media window.
- Use a 250ms window open animation.
- If the clip is assigned to a scene, show a small link-line or highlight from queue row to scene row.

## Visual System

### Palette

Use a controlled retro-tech palette:

- `paper-white`: `#f6f2e8`
- `system-gray`: `#c8c8c8`
- `deep-ink`: `#101217`
- `aqua-blue`: `#4f9fd8`
- `classic-blue`: `#1f5fbf`
- `signal-green`: `#37d67a`
- `amber-alert`: `#d49b2a`
- `error-red`: `#c0473d`

Avoid default purple-blue AI gradients. Gradients are allowed only as subtle old-desktop glass or wallpaper treatments.

### Typography

- UI chrome: compact bitmap-like or system UI face.
- Body text: readable serif or humanist sans, depending on implementation availability.
- Code and manifest windows: monospaced.
- Formula: math-friendly serif or carefully styled text if MathJax/KaTeX is not installed.

Implementation can start with local/system fallbacks and add custom fonts only if build time allows.

### UI Components

- Classic title bars with three small window buttons.
- Beveled or inset panels for controls.
- Status badges styled like old OS labels.
- Scrollbars may be custom-styled for desktop, but must remain usable.
- Buttons should have pressed, hover, disabled, and loading states.

### Icons

Use custom lightweight pixel-style icons or simple CSS icon blocks. Avoid using actual Apple or Windows icons.

Required icon set:

- Formula document
- Film reel or video window
- PixVerse spark/render tile
- Manifest JSON file
- Solo workflow node
- Warning/system dialog

## Information Architecture

Suggested routes:

- `/`: main `PaperMotion Workbench` demo desktop.
- `/api/pixverse/generate`: server route for PixVerse generation.
- `/api/pixverse/status/:video_id`: server route for PixVerse polling.

Suggested frontend modules:

- `DesktopShell`
- `MenuBar`
- `WindowFrame`
- `Dock`
- `FilmWindow`
- `FormulaWindow`
- `PixVerseConsole`
- `WorkflowWindow`
- `ManifestInspector`
- `SystemDialog`

## Data Contract

The site should use two data contracts:

- `examples/attention/production_manifest.json`: project-level registry for title, intent, script beats, storyboard overview, PixVerse job summaries, asset status, and website navigation.
- `examples/attention/enriched_scene_spec.json`: scene-level single source of truth for timing, Manim, TTS, music, PixVerse, assembly, and QA.

Minimum fields needed by the site:

From `production_manifest.json`:

- `project.title`
- `project.status`
- `intent.learning_objective`
- `storyboard.scenes`
- `scenes`
- `visual_asset_requests`
- `pixverse_jobs`
- `asset_manifest`
- `edit_decision_list`
- `scene_spec_contract`

From `enriched_scene_spec.json`:

- `contract_version`
- `total_duration_s`
- `global_style_tokens`
- `scenes[*].timestamp_start_s`
- `scenes[*].duration_s`
- `scenes[*].visual_type`
- `scenes[*].manim`
- `scenes[*].pixverse`
- `scenes[*].tts`
- `scenes[*].music_cue`
- `scenes[*].assembly`
- `scenes[*].qa_checks`

If fields are missing, the site should render a clear placeholder and continue.

## PixVerse API Safety Boundary

PixVerse is allowed for:

- cinematic support clips
- abstract transitions
- atmospheric token-flow scenes
- concept metaphors
- intro/outro material
- image-to-video from Manim stills or storyboard keyframes

PixVerse is not allowed for:

- exact equations
- readable formula labels
- matrix arithmetic
- deterministic symbol transformations
- anything that could contradict the Manim explanation

The UI should communicate this boundary. Manim is the exact math layer. PixVerse is the cinematic support layer.

## MVP Acceptance Criteria

- First viewport looks like a retro desktop workbench.
- Viewer can understand the product without scrolling.
- Main film window, formula window, PixVerse console, and workflow window are visible or one click away.
- Attention demo data comes from `production_manifest.json` plus `enriched_scene_spec.json` or a thin adapter around both.
- PixVerse API key stays server-side.
- Generate flow supports submit, polling, success, failure, and fallback states.
- No text overlaps on common desktop and mobile widths.
- `prefers-reduced-motion` is respected.
- The visual style does not use real Apple or Windows assets.

## Implementation Sequence

1. Create static `PaperMotion Workbench` shell and window components.
2. Wire `production_manifest.json` into project, formula, storyboard, and PixVerse panels.
3. Wire `enriched_scene_spec.json` into Scene Spec Inspector, Assembly Monitor, timing, and layer readiness.
4. Add PixVerse backend proxy routes with environment-based API key.
5. Implement generate/polling UI states.
6. Add responsive layout for tablet/mobile as stacked windows.
7. Add motion polish and reduced-motion support.
8. Run browser QA for desktop and mobile.

## Open Decisions

- Whether the first implementation should be closer to Aqua or Win98.
- Whether to support real draggable windows in MVP or use fixed responsive positions.
- Whether to persist generated PixVerse results locally, in a database, or only in session state.
- Whether final assembly happens in the website or remains a separate offline step.
