# Website Builder Handoff: PaperMotion Workbench

Note: this handoff is now secondary. Person B is building the site directly in `site/`; use this document only as background if a dedicated builder is reintroduced.

## Copy-Paste Brief

You are the dedicated website builder for PaperMotion. Build the public demo website for the current repo.

The website is not a generic landing page. It is a retro desktop-style product demo called `PaperMotion Workbench`: a fictional retro research workstation where a viewer can inspect a formula-to-video pipeline, preview the film, inspect scene specs, and trigger PixVerse cinematic support generation.

Build the actual usable first screen, not marketing filler.

## Repo Context

Working directory:

```text
/Users/starryyu/Downloads/trae/papermotion
```

Current branch:

```text
person-b-presentation
```

Person A owns the internal Trae Solo production workflow:

- formula understanding
- script
- storyboard
- enriched scene spec
- Manim exact render

Person B owns the public presentation surface:

- website
- retro system UI
- PixVerse generate panel
- workflow visualization
- video embed
- final QA

## Must Read First

Read these files before implementing:

```text
docs/person-b-presentation-website-design.md
docs/project-plan-fusion.md
docs/trae-solo-native-workflow.md
examples/attention/production_manifest.json
examples/attention/enriched_scene_spec.json
contracts/production_manifest.schema.json
contracts/enriched_scene_spec.schema.json
```

If any optional input file is missing, continue with a clear placeholder:

```text
examples/attention/input.md
examples/attention/mechanism_spec.json
examples/attention/storyboard.md
site/public/videos/attention-demo.mp4
```

## Product Goal

Build a website that proves:

```text
Formula / paper mechanism
  -> structured teaching plan
  -> enriched scene spec
  -> Manim exact math layer
  -> PixVerse cinematic layer
  -> assembly / QA
  -> final explainer film
```

The viewer should understand this in the first viewport.

The demo topic is scaled dot-product attention:

```text
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V
```

## Required Aesthetic

Use `PaperMotion Workbench`.

Visual references:

- early Mac OS / early Mac OS X Aqua
- Windows 98 control density
- old desktop windows, menu bars, docks/taskbars, desktop icons, bevels, status lights

Important:

- Do not copy Apple, Microsoft, Finder, Windows, Mac OS, or system icons directly.
- Do not use real Apple/Microsoft logos or assets.
- The goal is a fictional retro research workstation, not an imitation OS.
- Avoid generic AI SaaS visuals.
- Avoid default blue-white landing page design.
- Avoid purple AI gradients.
- Avoid oversized hero sections.

The visual target:

```text
retro desktop UI + cinematic AI production console + paper/math artifact inspector
```

Recommended palette:

```text
paper-white   #f6f2e8
system-gray   #c8c8c8
deep-ink      #101217
aqua-blue     #4f9fd8
classic-blue  #1f5fbf
signal-green  #37d67a
amber-alert   #d49b2a
error-red     #c0473d
```

Use compact, highly readable UI. Information density is good, but text must not overlap.

## Technical Direction

If no site exists yet, create:

```text
site/
```

Recommended implementation:

- Vite + React + TypeScript
- CSS modules or plain CSS with variables
- No heavy UI framework unless already present
- Local JSON data loading from the repo or copied public data
- Backend/API routes only if the chosen framework supports them; otherwise create a clear API adapter layer and mock fallback

If using Next.js instead of Vite, keep the same UI and data contract. Do not spend time migrating unless needed.

## Data Contracts

Use two data sources.

### Project Registry

```text
examples/attention/production_manifest.json
```

Use it for:

- project title/status
- intent and learning objective
- storyboard scene list
- visual asset requests
- PixVerse job summaries
- asset manifest
- edit decision list
- pointer to enriched scene spec

### Scene-Level Source Of Truth

```text
examples/attention/enriched_scene_spec.json
```

Use it for:

- scene timing
- active scene state
- visual type: `manim`, `pixverse`, `hybrid`, `website_only`
- Manim scene class, objects, animation sequence
- TTS text and timing
- music cue
- PixVerse job prompt/status
- assembly layers
- QA checks

The website should visibly communicate this split:

```text
Manifest = project registry
Enriched Scene Spec = executable scene contract
```

## Required First Viewport

The first viewport must look like a working desktop.

Required visible or immediately focusable windows:

1. `Film Window`
   - largest window
   - video player or styled placeholder
   - chapter rail
   - active scene title and timecode

2. `Formula Window`
   - displays the attention formula
   - clickable symbol ledger
   - stable colors for Q, K, V, QK^T, sqrt(d_k), softmax, output/context

3. `PixVerse Console`
   - lists PixVerse jobs from manifest/spec
   - supports selected job view
   - shows prompt, negative prompt, status, trace/video ID placeholders
   - includes `Generate Support Shot` action

4. `Solo Workflow Window`
   - shows the pipeline:

```text
Input -> Intent -> Curriculum -> Script -> Storyboard -> Enriched Scene Spec -> Manim/TTS/Music/PixVerse -> Assembly -> Website
```

5. `Scene Spec Inspector`
   - active scene from `enriched_scene_spec.json`
   - show timing, visual type, Manim, TTS, music cue, PixVerse cue, assembly, QA checks

6. `Assembly Monitor`
   - layer readiness across scenes
   - makes Manim exact layer and PixVerse cinematic layer distinct

Also include:

- top menu bar: `PaperMotion  File  Workflow  PixVerse  View  Help`
- desktop icons: `attention.formula`, `production_manifest.json`, `enriched_scene_spec.json`, `pixverse_queue`, `final_film.mov`
- dock or taskbar icons to focus windows

## Interaction Requirements

### Scene Selection

When the user clicks a scene/chapter:

- Film Window updates active scene label/timecode.
- Formula Window highlights related formula part where possible.
- PixVerse Console focuses matching job if the scene has PixVerse.
- Scene Spec Inspector updates to that scene.
- Assembly Monitor highlights that scene.

### Formula Symbol Selection

Clickable symbols:

- `Q`
- `K`
- `V`
- `QK^T`
- `sqrt(d_k)`
- `softmax`
- output/context vector

Clicking a symbol should show:

- short explanation
- linked scene
- Manim exact layer note
- PixVerse boundary note if relevant

### PixVerse Generate Flow

Frontend must not expose the API key.

Ideal routes:

```text
POST /api/pixverse/generate
GET /api/pixverse/status/:video_id
```

If no backend is implemented yet, create a mock adapter with the same interface and clear TODO comments.

Generate flow:

1. Select a PixVerse job.
2. Confirm prompt and negative prompt.
3. Click `Generate Support Shot`.
4. Show status: `queued -> generating -> polling -> ready` or `failed`.
5. Show trace/video ID placeholders.
6. Show preview button when ready.

Safety rule:

- Reject or block jobs that ask PixVerse to render exact formulas, matrices, readable labels, or symbolic transformations.
- PixVerse is only for cinematic support, transitions, atmosphere, and metaphor clips.
- Manim owns exact math.

## Motion Requirements

Motion should feel like an old desktop UI made responsive.

Required:

- Boot sequence under 900ms.
- Menu bar enters first.
- Film Window opens next.
- Other windows stagger in by about 40ms.
- Clicking a window brings it forward with subtle title-bar and shadow change.
- Menu dropdowns use quick 100-140ms opacity/position motion.
- Scene changes use a 220-320ms coordinated update.
- PixVerse queue states should have old-system style indicators.
- Respect `prefers-reduced-motion`.

Avoid flashy landing-page animation.

## Video Handling

If this file exists:

```text
site/public/videos/attention-demo.mp4
```

Use it.

If not, show a styled placeholder in the Film Window:

- name the expected path
- show current scene list
- make it clear the player is ready for the MP4

Do not leave a blank video area.

## Responsive Requirements

Desktop:

- Use layered desktop windows.
- Film Window should dominate.
- Secondary windows can overlap but must remain readable.

Tablet/mobile:

- Convert windows into stacked panels.
- Preserve retro chrome.
- Keep text within bounds.
- Dock/taskbar can become horizontal tabs.

No text overlap is acceptable.

## Suggested Component Structure

```text
src/
  app/
  data/
    loadDemoData.ts
  components/
    DesktopShell.tsx
    MenuBar.tsx
    Dock.tsx
    WindowFrame.tsx
    FilmWindow.tsx
    FormulaWindow.tsx
    PixVerseConsole.tsx
    WorkflowWindow.tsx
    SceneSpecInspector.tsx
    AssemblyMonitor.tsx
    ManifestInspector.tsx
    SystemDialog.tsx
  styles/
    tokens.css
    desktop.css
    windows.css
```

Use different structure if the project stack requires it, but keep these logical boundaries.

## Content Notes

Use concise display copy. Do not fill the UI with explanatory paragraphs.

Good labels:

- `Manim Exact Layer`
- `PixVerse Cinematic Layer`
- `Scene Contract`
- `Assembly Queue`
- `Formula Ledger`
- `Generate Support Shot`
- `Ready for MP4`
- `Trace ID`

Avoid:

- generic "AI powered" marketing copy
- long bullet-heavy sections
- claims that the system can explain any paper automatically

## Accessibility And QA

Minimum:

- keyboard-focusable buttons
- clear active/focus states
- readable contrast
- `prefers-reduced-motion`
- no text overlap at desktop/mobile widths
- no inaccessible tiny controls for primary actions

Browser QA:

- desktop width around 1440px
- laptop width around 1280px
- mobile width around 390px

## Acceptance Criteria

The implementation is done when:

- Site runs locally.
- First viewport looks like `PaperMotion Workbench`, not a marketing landing page.
- Film, Formula, PixVerse, Workflow, Scene Spec, and Assembly windows are visible or focusable.
- Chapter clicks update multiple windows.
- Formula token clicks update explanation.
- PixVerse Console has generate/polling/ready/fail states, with API key never exposed.
- Manifest and enriched scene spec are both used.
- Missing MP4 still produces a polished placeholder.
- Manim and PixVerse responsibilities are clearly separated.
- No text overlaps on desktop or mobile.
- Visual style is retro technical desktop, not generic AI SaaS.

## Non-Goals For First Build

- Full user upload flow.
- Accounts.
- Payment.
- Full automatic PDF parser.
- Final production backend orchestration.
- Real drag-and-drop window management if it slows delivery.

Clickable/focusable fixed windows are acceptable for MVP.

## Implementation Order

1. Create the site app under `site/`.
2. Load/adapter the two JSON data files.
3. Build `DesktopShell`, `MenuBar`, `WindowFrame`, and dock/taskbar.
4. Build Film, Formula, PixVerse, Workflow, Scene Spec, and Assembly windows.
5. Wire active scene state across all windows.
6. Add PixVerse API adapter with mock fallback if backend is not ready.
7. Add responsive layout.
8. Add motion polish.
9. Run local QA and fix overlap.

## Final Deliverable

Return:

- local run command
- local URL
- files changed
- any unresolved backend/API assumptions
- screenshots or browser QA notes if available
