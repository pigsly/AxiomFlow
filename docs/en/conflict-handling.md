# Conflict Handling

[中文](../zh/conflict-handling.md)

When governance truth is unreliable, the system must stop.

## When to Trigger Conflict Handling

Trigger conflict handling when you find any of these conditions:

- documents contradict each other
- the real implementation has drifted from the stated direction
- key information is missing
- governance documents are outdated
- the proposed output may violate `ADR` or `CONTRACT`

## Required Response

Handle conflict in this order:

1. Stop the current implementation or document update.
2. Identify the conflict source.
3. Describe the exact contradiction.
4. Explain the likely impact.
5. Return the decision to a human.

Do not continue on assumptions.

## `SPEC` Blocking Rule

If the conflict appears in `SPEC-XXX.md`, set `code_implement` to `blocked`.

Do not clear that state until:

- the conflicting documents are updated, or
- a human explicitly resolves the conflict

## Conflicts in Formal Governance

If the conflict is inside a formal governance document such as:

- `REQ`
- `ADR`
- `CONTRACT`

do not invent new fields or patch around the issue. Record the warning and stop.

## Why the System Stops

Many teams treat stop conditions as friction.

AxiomFlow treats them as protection. If truth is inconsistent, speed becomes a risk multiplier.
