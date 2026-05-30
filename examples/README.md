# PaperMotion Examples

These examples are skill-pack test cases for the PaperMotion workflow. They are
not website demos. Each case is meant to test whether the skills can turn a
paper, formula, or mechanism into a schema-backed dynamic visual model.

## Validation

Validate all dynamic scene examples with:

```bash
./setup.sh --check-only
```

Validate one example with:

```bash
python3 scripts/validate_dynamic_scene_model.py examples/<demo>/dynamic_scene_model.json
```

The single-file command requires the active `python3` to have `jsonschema`
installed. The canonical post-install validation path is `./setup.sh --check-only`
because it selects an available Python runtime with the validator dependency.

## Current Examples

| Demo | Source | Mechanism focus | Current artifacts |
| --- | --- | --- | --- |
| `attention` | Scaled dot-product attention formula | Q/K/V roles, score matrix, softmax normalization, weighted value aggregation | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json`, `storyboard.md`, `enriched_scene_spec.json`, `production_manifest.json` |
| `adam-optimizer` | Adam optimizer paper, https://arxiv.org/abs/1412.6980 | Noisy gradient, first moment, second moment, adaptive update step | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json` |
| `ddpm-denoising` | Denoising Diffusion Probabilistic Models, https://arxiv.org/abs/2006.11239 | Fixed forward noising, closed-form noisy state, learned iterative reverse denoising | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json` |
| `nerf-volume-rendering` | NeRF, https://arxiv.org/abs/2003.08934 | Ray sampling, field query, density/color outputs, transmittance-weighted volume integration | `input.md`, `mechanism_spec.json`, `dynamic_scene_model.json` |

## Example Status

`attention` is the most complete sample run because it also includes storyboard,
scene specs, rendered-layer notes, and production-manifest artifacts.

`adam-optimizer`, `ddpm-denoising`, and `nerf-volume-rendering` are dynamic scene
model generalization cases. They prove the `dynamic-visual-reasoning` skill can
structure optimization, probabilistic generation, and 3D neural rendering
mechanisms, but they still need downstream storyboard, scene contract, renderer,
and QA artifacts before they become full video runs.
