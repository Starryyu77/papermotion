# Install As Trae Skill Pack

PaperMotion is intended to be installed by Trae Solo as a skill pack from a GitHub link plus an install prompt.

## Trae Solo Install

Give Trae this repository URL and the prompt in [prompts/trae-install-sku.md](../prompts/trae-install-sku.md).

Minimal human message:

```text
请安装这个 PaperMotion SKU：<GitHub repo URL>
按照仓库里的 prompts/trae-install-sku.md 执行。
```

Trae should clone the repo, read `papermotion.sku.json`, register or load the
`papermotion.sku.json.skills[]` entries using each file's frontmatter metadata,
confirm the root skill is available, and then continue through the PaperMotion skills.

The root skill is:

```text
skills/papermotion-research-video/SKILL.md
```

## Skill Registration Authority

`papermotion.sku.json.skills[]` is the authoritative list of skills to install. Do not
treat a directory glob as the source of truth.

For each path listed in `papermotion.sku.json.skills[]`:

1. Confirm the `SKILL.md` file exists.
2. Read its frontmatter `name` and `description`.
3. Register or load the skill in Trae Solo using that frontmatter metadata.

Installation is complete when every listed skill is registered or loadable and the root
skill is available.

## Post-Install Validation Backend

The post-install validation command is:

```bash
./setup.sh --check-only
```

This is not the product install by itself. It checks available runtime tools and validates
every `examples/*/dynamic_scene_model.json`.

Run the full backend only when you need to create or refresh a local validation
environment:

```bash
./setup.sh
```

Full setup creates `.venv`, installs the Python validator dependency, creates
`.env.local` from `.env.example`, checks available runtime tools, and validates examples.

Optional site check:

```bash
./setup.sh --with-site
```

For local Manim rendering:

```bash
./setup.sh --with-manim
```

Canonical validation:

```bash
./setup.sh --check-only
```

Useful single-file checks when your active `python3` can import `jsonschema`:

```bash
python3 scripts/validate_dynamic_scene_model.py examples/attention/dynamic_scene_model.json
python3 scripts/validate_dynamic_scene_model.py examples/adam-optimizer/dynamic_scene_model.json
python3 scripts/validate_dynamic_scene_model.py examples/ddpm-denoising/dynamic_scene_model.json
python3 scripts/validate_dynamic_scene_model.py examples/nerf-volume-rendering/dynamic_scene_model.json
```

Use `npm --prefix site run build` only when explicitly checking the optional website
surface.

Optional tools:

- `ffmpeg`: final video assembly/export.
- `manim`: deterministic formulas, matrices, diagrams, and exact animation.
- `node` / `npm`: optional site and future Remotion work.
- `Blender`: future polished 3D renderer.

Provider keys are optional and should stay in `.env.local`.
