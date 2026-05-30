# Prompt: PixVerse Cinematic Support

You are creating required cinematic support assets for a technical explainer video.

Input:
- A Manim still frame, short rough clip, or scene description.
- `examples/<demo>/production_manifest.json`
- `examples/<demo>/enriched_scene_spec.json`

Rules:
- Do not change formulas, symbols, matrices, or mathematical relationships.
- Use PixVerse for atmosphere, transition, intro/outro motion, explanatory objects, and metaphor shots.
- Keep duration short, ideally 5 seconds per generated clip.
- Prefer 16:9 output for website embedding.
- If using image-to-video, preserve the provided frame composition.
- Record every asset request in `production_manifest.visual_asset_requests`.
- Record every generation attempt in `production_manifest.pixverse_jobs`.
- Ensure every generated PixVerse clip corresponds to a `pixverse` entry in `enriched_scene_spec.scenes[*]`.

Output:
- PixVerse prompt.
- Negative prompt.
- Intended insertion point in the final video.
- Risk note for any possible mismatch with the educational content.
