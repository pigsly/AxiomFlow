---
name: render_pdr_status
description: Render PDR results with a required Rich bordered panel, without summarization or interpretation.
---

# SKILL: render_pdr_status

## Purpose

Render PDR result with a required Rich bordered panel output.

This skill is **observation-only**.
No summarization. No interpretation.

---

## Input

* `pdr_result` (JSON)

```json
{
  "overall_signal": "Review Suggested",
  "alignment_score": 86,
  "breakdown": {
    "req_spec_alignment": 45,
    "adr_alignment": 27,
    "execution_clarity": 14
  },
  "safety_gates": {
    "required_docs_present": true,
    "references_resolved": true,
    "contract_safety": "Needs Clarification"
  }
}
```

---

## Execution (YAML)

```yaml
executor: python_script

entry: runner.py

command:
  - python3
  - runner.py

input:
  type: json
  source: stdin
  fallback: lock.json

modes:
  - rich_panel

env:
  RENDER_MODE: rich_panel
```

`rich_panel` is the required default mode and renders a bordered status box with the `rich` package.

---

## Behavior

1. Parse PDR result (stdin or lock.json)
2. Normalize fields
3. Render output

---

## Layout (rich_panel)

Rich bordered status box:

* title: `AxiomFlow PDR Status`
* boxed key/value layout
* intended for non-interactive terminals and transcript-friendly output
* must be used as the standard output layout for this skill

`Observations` and `Summary List` are intentionally out of scope for this skill.
If a workflow requires them, they must be produced by the upstream PDR layer or another renderer.

---

## Constraints

* No mutation to PDR source
* Pure rendering only
* Deterministic output for same input
* No summarization layer
* No interpretation
* No `Observations` rendering
* No `Summary List` generation
* `rich_panel` is mandatory

---

## Notes

This skill belongs to the **Observation Layer**:

```
PDR Engine → JSON → Render Skill → UI
```

It must NOT:

* infer meaning
* generate summary
* render `Observations`
* generate `Summary List`
* suggest actions
