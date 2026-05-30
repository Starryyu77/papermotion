# PaperMotion Workflow Video Prompt Draft

Status: confirmed product-demo direction; ready for reference image generation.

## Goal

Create a short AI-generated concept video that explains the complete PaperMotion workflow:

```text
paper/formula -> intent -> prerequisite graph -> curriculum -> teaching script -> storyboard -> enriched scene spec -> Manim exact layer + PixVerse cinematic layer -> voice/music/SFX -> assembly/QA -> PaperMotion Workbench website
```

The video should sell the workflow as a file-backed, reviewable Trae Solo production cockpit, not as a vague one-click AI video generator.

## Creative Direction

- Product-demo oriented, with cinematic polish used to clarify the workflow rather than overwhelm it.
- Retro technical workstation interface, inspired by early creative desktop tools, without copying any real OS brand.
- Geometric intuition explainer mood: precise, calm, educational, visually structured.
- Show repo files and artifacts as the trust layer.
- Manim owns exact formulas, matrices, labels, and deterministic transforms.
- PixVerse owns cinematic support shots, metaphor clips, atmospheric transitions, and object motion.
- Use uploaded reference images / generated keyframes as image-to-video inputs where possible so the Transformer attention explanation stays visually consistent across video generation.
- Keep scaled dot-product attention as the concrete demo topic.

## Main Video Prompt V2

Create a 35-45 second product demonstration video for "PaperMotion". The video should explain the complete workflow of the product, not just show abstract AI visuals.

Product idea:
PaperMotion is a Trae Solo-native production workflow that turns a research paper, formula, or technical mechanism into an inspectable educational visualization video. The workflow is file-backed, staged, reviewable, and transparent. It is not a one-click black-box AI video generator.

Story structure:
1. Start with a user uploading or selecting a research paper image / formula screenshot about Transformer attention. The formula is scaled dot-product attention: Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V.
2. The input enters a Trae Solo workspace. The interface shows this is a production cockpit, not a chat box.
3. The workflow expands into staged artifacts, each becoming a visible repo file card:
   input.md -> mechanism_spec.json -> storyboard.md -> production_manifest.json -> enriched_scene_spec.json.
4. Show the reasoning pipeline as a clean compiler-like sequence:
   Intent -> Prerequisite Graph -> Curriculum -> Teaching Script -> Storyboard -> Scene Spec.
5. The Scene Spec splits production into two layers:
   Manim Exact Layer: formulas, matrices, Q/K/V roles, heatmap, scaling, softmax weights, value-vector merge.
   PixVerse Cinematic Layer: text-free support shots, atmospheric transitions, glowing token fields, conceptual motion.
6. Show uploaded reference images / generated keyframes being used for image-to-video generation, so the Transformer visual style stays consistent across cinematic clips.
7. Add audio production lanes: voiceover, music, and SFX align to scene timing from enriched_scene_spec.json.
8. Show Assembly + QA: Manim clips, PixVerse clips, voiceover, music, and SFX lock into a timeline; QA checks verify timing, formulas, scene order, and artifact links.
9. End with the PaperMotion Workbench website: final explainer video playing in a retro research workstation UI, formula overlay visible, scene chapter rail active, workflow strip visible, inspector showing the exact artifacts behind the current scene.

Visual style:
Polished retro research workstation, product-demo clarity, cinematic AI production console, paper/math artifact inspector, blue-gray workstation wallpaper, crisp compact windows, subtle glass highlights, professional educational technology. Keep the product interface readable and structured. Use cinematic motion only to make the workflow feel smooth and credible.

Camera and motion: smooth controlled camera pushes, crisp UI reveals, file cards snapping into a pipeline, subtle parallax, no chaotic movement, no excessive particles. The video should feel like a transparent compiler for educational videos.

Mood: credible, technical, elegant, inspectable, calm, high-trust.

Aspect ratio: 16:9.
Duration: 35-45 seconds.
No voiceover text required inside the video except short UI labels. Keep all readable text minimal and clean.

## Negative Prompt

Generic AI SaaS dashboard, purple-blue gradient blobs, random equations, fake unreadable text, distorted symbols, messy code, chaotic particles, overdecorated futuristic HUD, misleading math, exact formulas inside cinematic PixVerse shots, brand-specific operating system UI, cluttered landing page, stock footage, humans talking to camera, excessive neon, dense paragraphs, low-resolution UI, flicker, warped typography.

## Short Prompt For Video Tool

Product demo video for PaperMotion, a Trae Solo-native workflow that converts a research paper or formula into an inspectable educational visualization film. Show a Transformer attention formula screenshot entering a retro research workstation. The workflow becomes repo file artifacts: input.md, mechanism_spec.json, storyboard.md, production_manifest.json, enriched_scene_spec.json. Show stages: Intent, Prerequisite Graph, Curriculum, Teaching Script, Storyboard, Scene Spec. Then split into Manim Exact Layer for precise formulas and heatmaps, and PixVerse Cinematic Layer for text-free cinematic support shots. Show uploaded keyframes used for image-to-video Transformer clips. Add voiceover/music/SFX lanes, assembly timeline, QA checks, final MP4, then end in PaperMotion Workbench website with film window, formula overlay, chapter rail, workflow strip, and artifact inspector. Style: polished retro research workstation, clear product demo, credible, technical, calm, blue-gray UI, compact glassy windows, no generic AI SaaS, no purple gradients, no warped math text.

## Suggested Reference Images To Generate After Confirmation

1. Opening research-paper-to-workspace frame:
   - Research paper on desk, attention formula highlighted, file-backed workflow artifacts beginning to rise into a retro technical workstation.

2. PaperMotion Workbench hero frame:
   - Retro research workstation UI with film window, formula overlay, chapter rail, workflow strip, and inspector panel.

3. Dual-layer production frame:
   - Split view showing Manim exact math layer on the left and PixVerse cinematic support layer on the right, connected by enriched_scene_spec.json in the middle.

4. Final assembly and QA frame:
   - Timeline with Manim, PixVerse, voiceover, music, and SFX lanes snapping together, QA checks passing, final MP4 routed into the website.

## User Confirmation

1. Tone: product-demo oriented.
2. Visual direction: current retro research workstation.
3. Demo topic: keep scaled dot-product attention.
4. Video generation mode: support using uploaded reference images / keyframes for Transformer image-to-video shots.
