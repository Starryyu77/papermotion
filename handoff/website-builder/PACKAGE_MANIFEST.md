# PaperMotion Website Builder Package Manifest

## Start Here

Read this first:

```text
handoff/website-builder/README.md
```

It is the standalone implementation brief for the website builder.

## Package Contents

```text
handoff/website-builder/
  README.md
  PACKAGE_MANIFEST.md

  docs/
    person-b-presentation-website-design.md
    project-plan-fusion.md
    research-and-mvp-plan.md
    trae-solo-native-workflow.md

  contracts/
    production_manifest.schema.json
    enriched_scene_spec.schema.json

  examples/attention/
    production_manifest.json
    enriched_scene_spec.json

  prompts/
    05-website-integration.md

  solo/
    task-board.md
    review-checklist.md
```

## What To Build

Build the `PaperMotionOS Classic Workbench` website under the repo `site/` directory.

The first screen should be a retro desktop workbench, not a landing page.

Required windows:

- Film Window
- Formula Window
- PixVerse Console
- Solo Workflow Window
- Scene Spec Inspector
- Assembly Monitor

## Data To Use

Project-level registry:

```text
handoff/website-builder/examples/attention/production_manifest.json
```

Scene-level execution contract:

```text
handoff/website-builder/examples/attention/enriched_scene_spec.json
```

## GitHub Usage

If this package is in a GitHub repository, give the website builder the repository URL and ask it to start from:

```text
handoff/website-builder/README.md
```

If the builder expects root-relative project files, it may copy the package files back to their original paths:

```text
docs/
contracts/
examples/attention/
prompts/
solo/
```

The package is intentionally self-contained so the builder does not need access to the local machine path.
