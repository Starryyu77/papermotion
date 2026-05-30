# PaperMotion Review Checklist

## Solo Workflow

- [ ] All current tasks are listed in `solo/task-board.md`.
- [ ] Every stage has a file input and file output.
- [ ] `examples/attention/production_manifest.json` is the current source of truth.
- [ ] MTC mode artifacts are reviewed before Code Mode consumes them.
- [ ] Code Mode render/debug notes are written to `examples/attention/render_notes.md`.
- [ ] `memory/active/current.md` reflects the latest decision.

## Educational Correctness

- [ ] Formula symbols keep one meaning throughout.
- [ ] Color mapping is stable across video and website.
- [ ] The narration does not claim more than the source supports.
- [ ] Misconceptions are handled explicitly.

## Manim

- [ ] Low-quality render works before final render.
- [ ] The script uses common Manim APIs.
- [ ] The video is exported to the website asset path.

## Website

- [ ] First viewport shows the explainer experience.
- [ ] Chapter clicks update explanation text.
- [ ] Workflow timeline shows Trae Solo as the execution workspace.
- [ ] No text overlap on desktop or mobile.
- [ ] README has local run instructions.

## PixVerse

- [ ] PixVerse is a formal cinematic support stage.
- [ ] PixVerse is not responsible for exact formulas, matrices, or symbolic transformations.
- [ ] Every PixVerse request appears in `production_manifest.visual_asset_requests`.
- [ ] Every generation job appears in `production_manifest.pixverse_jobs`.
- [ ] Any PixVerse prompt preserves the educational metaphor and avoids readable equations.
- [ ] If generation is unavailable, the site still shows the PixVerse job spec and uses a placeholder.
