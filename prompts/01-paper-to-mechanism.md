# Prompt: Paper Or Formula To Mechanism Spec

You are converting a complex paper mechanism into a short visual explainer workflow.

Input:
- Paper excerpt, formula, or mechanism description.

Output file:
- `examples/<demo>/mechanism_spec.json`

Requirements:
- Identify one learning objective.
- Extract a symbol ledger with stable names, meanings, and colors.
- Break the mechanism into 5-7 causal steps.
- For each step, propose one visual metaphor that can be rendered in Manim.
- Include common misconceptions and how the animation should prevent them.
- Do not invent claims not supported by the input.

JSON shape:

```json
{
  "title": "",
  "learning_objective": "",
  "source_excerpt": "",
  "symbol_ledger": [
    {
      "symbol": "",
      "meaning": "",
      "color": "",
      "visual_role": ""
    }
  ],
  "causal_steps": [
    {
      "id": "",
      "plain_language": "",
      "formula_link": "",
      "visual_metaphor": "",
      "manim_objects": []
    }
  ],
  "misconceptions": [
    {
      "risk": "",
      "animation_guardrail": ""
    }
  ]
}
```
