#!/usr/bin/env python3
"""Validate PaperMotion dynamic_scene_model JSON files.

JSON Schema catches shape errors. This script also catches semantic contract
errors that JSON Schema cannot express cleanly, such as dangling refs and
duplicate IDs.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def add_id(ids: dict[str, str], errors: list[str], value: str | None, path: str) -> None:
    if not value:
        return
    if value in ids:
        errors.append(f"duplicate id '{value}' at {path}; first seen at {ids[value]}")
    else:
        ids[value] = path


def check_refs(refs: list[str], allowed: set[str], errors: list[str], path: str) -> None:
    for ref in refs or []:
        if not ref:
            continue
        if ref not in allowed:
            errors.append(f"dangling ref '{ref}' at {path}")


def collect_source_ids(model: dict[str, Any]) -> set[str]:
    source_links = model.get("source_links", {})
    ids: set[str] = set()
    for key in (
        "source_claim_ids",
        "formula_ids",
        "figure_ids",
        "mechanism_step_ids",
        "symbol_ids",
    ):
        ids.update(source_links.get(key, []) or [])
    return ids


def validate_semantics(model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    all_ids: dict[str, str] = {}

    semantic = model.get("semantic_units", {})
    visual = model.get("visual_model", {})
    dynamic = model.get("dynamic_model", {})
    camera = model.get("camera_model", {})
    exactness = model.get("exactness_policy", {})
    renderer = model.get("renderer_plan", {})
    handoff = model.get("handoff", {})

    semantic_entity_ids = {x.get("id") for x in semantic.get("entities", [])}
    semantic_operator_ids = {x.get("id") for x in semantic.get("operators", [])}
    semantic_state_ids = {x.get("id") for x in semantic.get("states", [])}
    semantic_relation_ids = {x.get("id") for x in semantic.get("relations", [])}
    invariant_ids = {x.get("id") for x in semantic.get("invariants", [])}
    assumption_ids = {x.get("id") for x in semantic.get("assumptions", [])}
    semantic_ids = set().union(
        semantic_entity_ids,
        semantic_operator_ids,
        semantic_state_ids,
        semantic_relation_ids,
        invariant_ids,
        assumption_ids,
    )

    space_ids = {x.get("id") for x in visual.get("spaces", [])}
    visual_object_ids = {x.get("id") for x in visual.get("objects", [])}
    encoding_ids = {x.get("id") for x in visual.get("encodings", [])}
    layout_ids = {x.get("id") for x in visual.get("layout_constraints", [])}
    visual_ids = set().union(space_ids, visual_object_ids, encoding_ids, layout_ids)

    beat_ids = {x.get("id") for x in dynamic.get("beats", [])}
    dynamic_state_ids = {x.get("id") for x in dynamic.get("states", [])}
    transition_ids = {x.get("id") for x in dynamic.get("transitions", [])}
    motion_ids = {x.get("id") for x in dynamic.get("motion_primitives", [])}
    dynamic_ids = set().union(beat_ids, dynamic_state_ids, transition_ids, motion_ids)

    shot_ids = {x.get("id") for x in camera.get("shots", [])}
    camera_intent_ids = {x.get("id") for x in camera.get("camera_intents", [])}
    layer_ids = {x.get("layer_id") for x in renderer.get("layer_plan", [])}
    scene_ids = {x.get("scene_hint") for x in dynamic.get("beats", []) if x.get("scene_hint")}
    object_exactness = {x.get("id"): x.get("exactness") for x in visual.get("objects", [])}

    for group_name, group, key in (
        ("semantic.entities", semantic.get("entities", []), "id"),
        ("semantic.operators", semantic.get("operators", []), "id"),
        ("semantic.states", semantic.get("states", []), "id"),
        ("semantic.relations", semantic.get("relations", []), "id"),
        ("semantic.invariants", semantic.get("invariants", []), "id"),
        ("semantic.assumptions", semantic.get("assumptions", []), "id"),
        ("visual.spaces", visual.get("spaces", []), "id"),
        ("visual.objects", visual.get("objects", []), "id"),
        ("visual.encodings", visual.get("encodings", []), "id"),
        ("visual.layout_constraints", visual.get("layout_constraints", []), "id"),
        ("dynamic.beats", dynamic.get("beats", []), "id"),
        ("dynamic.states", dynamic.get("states", []), "id"),
        ("dynamic.transitions", dynamic.get("transitions", []), "id"),
        ("dynamic.motion_primitives", dynamic.get("motion_primitives", []), "id"),
        ("camera.shots", camera.get("shots", []), "id"),
        ("camera.camera_intents", camera.get("camera_intents", []), "id"),
        ("renderer.layer_plan", renderer.get("layer_plan", []), "layer_id"),
        ("exactness.simplifications", exactness.get("simplifications", []), "id"),
        ("open_questions", model.get("open_questions", []), "id"),
        ("known_risks", model.get("known_risks", []), "id"),
    ):
        for idx, item in enumerate(group):
            add_id(all_ids, errors, item.get(key), f"{group_name}[{idx}].{key}")

    source_ids = collect_source_ids(model)

    for idx, item in enumerate(semantic.get("entities", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"semantic.entities[{idx}].source_refs")

    for idx, item in enumerate(semantic.get("operators", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"semantic.operators[{idx}].source_refs")
        check_refs(item.get("input_refs", []), semantic_entity_ids, errors, f"semantic.operators[{idx}].input_refs")
        check_refs(item.get("output_refs", []), semantic_entity_ids, errors, f"semantic.operators[{idx}].output_refs")

    for idx, item in enumerate(semantic.get("states", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"semantic.states[{idx}].source_refs")

    for idx, item in enumerate(semantic.get("relations", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"semantic.relations[{idx}].source_refs")
        check_refs([item.get("from_ref")], semantic_entity_ids, errors, f"semantic.relations[{idx}].from_ref")
        check_refs([item.get("to_ref")], semantic_entity_ids, errors, f"semantic.relations[{idx}].to_ref")

    for idx, item in enumerate(semantic.get("invariants", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"semantic.invariants[{idx}].source_refs")

    for idx, item in enumerate(visual.get("objects", [])):
        check_refs(item.get("entity_refs", []), semantic_entity_ids, errors, f"visual.objects[{idx}].entity_refs")
        check_refs(item.get("source_refs", []), source_ids, errors, f"visual.objects[{idx}].source_refs")
        check_refs([item.get("space_ref")], space_ids, errors, f"visual.objects[{idx}].space_ref")

    for idx, item in enumerate(visual.get("encodings", [])):
        check_refs(item.get("object_refs", []), visual_object_ids, errors, f"visual.encodings[{idx}].object_refs")

    for idx, item in enumerate(visual.get("layout_constraints", [])):
        check_refs(item.get("object_refs", []), visual_object_ids, errors, f"visual.layout_constraints[{idx}].object_refs")

    for idx, item in enumerate(dynamic.get("beats", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"dynamic.beats[{idx}].source_refs")
        check_refs(item.get("object_refs", []), visual_object_ids, errors, f"dynamic.beats[{idx}].object_refs")

    for idx, item in enumerate(dynamic.get("states", [])):
        check_refs([item.get("beat_ref")], beat_ids, errors, f"dynamic.states[{idx}].beat_ref")
        if item.get("semantic_state_ref"):
            check_refs([item.get("semantic_state_ref")], semantic_state_ids, errors, f"dynamic.states[{idx}].semantic_state_ref")
        for jdx, object_state in enumerate(item.get("object_states", [])):
            check_refs([object_state.get("object_ref")], visual_object_ids, errors, f"dynamic.states[{idx}].object_states[{jdx}].object_ref")

    for idx, item in enumerate(dynamic.get("transitions", [])):
        check_refs([item.get("from_state_ref")], dynamic_state_ids, errors, f"dynamic.transitions[{idx}].from_state_ref")
        check_refs([item.get("to_state_ref")], dynamic_state_ids, errors, f"dynamic.transitions[{idx}].to_state_ref")
        check_refs(item.get("motion_primitive_refs", []), motion_ids, errors, f"dynamic.transitions[{idx}].motion_primitive_refs")
        for jdx, corr in enumerate(item.get("object_correspondence", [])):
            check_refs([corr.get("before_object_ref")], visual_object_ids, errors, f"dynamic.transitions[{idx}].object_correspondence[{jdx}].before_object_ref")
            check_refs([corr.get("after_object_ref")], visual_object_ids, errors, f"dynamic.transitions[{idx}].object_correspondence[{jdx}].after_object_ref")

    for idx, item in enumerate(dynamic.get("motion_primitives", [])):
        check_refs(item.get("object_refs", []), visual_object_ids, errors, f"dynamic.motion_primitives[{idx}].object_refs")
        for key in ("from_object_ref", "to_object_ref"):
            if item.get(key):
                check_refs([item.get(key)], visual_object_ids, errors, f"dynamic.motion_primitives[{idx}].{key}")
        if item.get("required_invariant_ref"):
            check_refs([item.get("required_invariant_ref")], invariant_ids, errors, f"dynamic.motion_primitives[{idx}].required_invariant_ref")

    for idx, item in enumerate(camera.get("shots", [])):
        check_refs(item.get("beat_refs", []), beat_ids, errors, f"camera.shots[{idx}].beat_refs")
        check_refs(item.get("focus_targets", []), visual_object_ids, errors, f"camera.shots[{idx}].focus_targets")

    for idx, item in enumerate(camera.get("camera_intents", [])):
        check_refs(item.get("beat_refs", []), beat_ids, errors, f"camera.camera_intents[{idx}].beat_refs")

    for idx, item in enumerate(exactness.get("exact_required", [])):
        check_refs([item.get("object_or_claim_ref")], visual_object_ids | source_ids, errors, f"exactness.exact_required[{idx}].object_or_claim_ref")

    for idx, item in enumerate(exactness.get("metaphor_allowed", [])):
        check_refs([item.get("layer_or_object_ref")], visual_object_ids | layer_ids, errors, f"exactness.metaphor_allowed[{idx}].layer_or_object_ref")

    for idx, item in enumerate(exactness.get("simplifications", [])):
        check_refs(item.get("source_refs", []), source_ids, errors, f"exactness.simplifications[{idx}].source_refs")
        check_refs(item.get("assumption_refs", []), assumption_ids, errors, f"exactness.simplifications[{idx}].assumption_refs")

    for idx, item in enumerate(renderer.get("layer_plan", [])):
        layer_object_refs = set(item.get("object_refs", []))
        exactness_items = item.get("exactness_by_object", [])
        exactness_object_refs = {x.get("object_ref") for x in exactness_items}
        check_refs(item.get("object_refs", []), visual_object_ids, errors, f"renderer.layer_plan[{idx}].object_refs")
        if exactness_object_refs != layer_object_refs:
            missing = sorted(layer_object_refs - exactness_object_refs)
            extra = sorted(exactness_object_refs - layer_object_refs)
            if missing:
                errors.append(f"renderer.layer_plan[{idx}].exactness_by_object missing refs: {', '.join(missing)}")
            if extra:
                errors.append(f"renderer.layer_plan[{idx}].exactness_by_object has extra refs: {', '.join(extra)}")
        for jdx, exact_item in enumerate(exactness_items):
            object_ref = exact_item.get("object_ref")
            check_refs([object_ref], visual_object_ids, errors, f"renderer.layer_plan[{idx}].exactness_by_object[{jdx}].object_ref")
            if object_ref not in layer_object_refs:
                errors.append(
                    f"exactness_by_object ref '{object_ref}' at renderer.layer_plan[{idx}].exactness_by_object[{jdx}] "
                    "is not listed in the same layer's object_refs"
                )
            declared = exact_item.get("exactness")
            source_exactness = object_exactness.get(object_ref)
            if source_exactness and declared != source_exactness:
                errors.append(
                    f"renderer.layer_plan[{idx}].exactness_by_object[{jdx}] declares '{declared}' "
                    f"for '{object_ref}', but visual_model.objects declares '{source_exactness}'"
                )
        actual_levels = {x.get("exactness") for x in exactness_items if x.get("exactness")}
        actual_levels.update(x.get("exactness") for x in item.get("layer_exactness_overrides", []) if x.get("exactness"))
        declared_levels = set(item.get("contains_exactness_levels", []))
        if declared_levels != actual_levels:
            errors.append(
                f"renderer.layer_plan[{idx}].contains_exactness_levels {sorted(declared_levels)} "
                f"does not match exactness_by_object plus layer_exactness_overrides {sorted(actual_levels)}"
            )

    for idx, item in enumerate(handoff.get("storyboard_beat_refs", [])):
        check_refs([item.get("beat_ref")], beat_ids, errors, f"handoff.storyboard_beat_refs[{idx}].beat_ref")
        check_refs([item.get("scene_hint")], scene_ids, errors, f"handoff.storyboard_beat_refs[{idx}].scene_hint")

    for idx, item in enumerate(handoff.get("enriched_scene_spec_hints", [])):
        check_refs([item.get("scene_id")], scene_ids, errors, f"handoff.enriched_scene_spec_hints[{idx}].scene_id")
        check_refs(item.get("visual_object_refs", []), visual_object_ids, errors, f"handoff.enriched_scene_spec_hints[{idx}].visual_object_refs")
        check_refs(item.get("motion_primitive_refs", []), motion_ids, errors, f"handoff.enriched_scene_spec_hints[{idx}].motion_primitive_refs")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("--schema", type=Path, default=Path("contracts/dynamic_scene_model.schema.json"))
    args = parser.parse_args()

    model = load_json(args.model)
    errors: list[str] = []

    try:
        import jsonschema  # type: ignore
    except Exception as exc:  # pragma: no cover - environment fallback
        errors.append(f"jsonschema import failed: {exc}")
    else:
        schema = load_json(args.schema)
        validator = jsonschema.Draft202012Validator(schema)
        for error in sorted(validator.iter_errors(model), key=lambda e: list(e.path)):
            path = "/".join(str(x) for x in error.path) or "<root>"
            errors.append(f"schema {path}: {error.message}")

    errors.extend(validate_semantics(model))

    if errors:
        print(f"{args.model}: invalid ({len(errors)} errors)")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"{args.model}: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
