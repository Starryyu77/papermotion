---
name: research-video-qa
description: Use when reviewing a generated research or math explainer video workflow for scientific correctness, symbol consistency, visual readability, pacing, and claim boundaries. Produces a QA report before final assembly or publication.
---

# Research Video QA

Use this skill before finalizing a research explainer video.

## Inputs

- `input.md`
- `mechanism_spec.json`
- `storyboard.md`
- `production_manifest.json`
- `enriched_scene_spec.json`
- rendered scene layers or rough video

## Output

Write:

- `examples/<demo>/qa_report.md`

## Review Checklist

Check:

- source claims are supported by the input
- symbols keep one meaning throughout
- prerequisites are introduced before use
- exact math is rendered by deterministic layers
- AI video does not contain readable fake text or unsupported diagrams
- narration matches visuals
- scene pacing leaves time for notation changes
- text, labels, and equations are readable
- output paths exist for claimed assets

## Severity

- Blocking: scientific error, unsupported claim, unreadable core formula, missing claimed output.
- Major: confusing symbol reuse, pacing too fast at key mechanism, AI clip risks misleading the viewer.
- Minor: polish, non-core visual alignment, wording improvements.

Do not approve final publication with blocking issues open.
