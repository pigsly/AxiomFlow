# Conflict Handling

[中文](../zh/conflict-handling.md)

When governance truth becomes unreliable, the system must stop.

This is one of the most important rules in AxiomFlow.

## When to Trigger Conflict Handling

Trigger conflict handling whenever you find any of the following:

- documents contradict each other
- actual logic has drifted from the declared direction
- key information is missing
- governance documents are outdated
- the output is likely to violate `ADR` or `CONTRACT`

## Required Response

Once conflict is detected, handle it in this order:

1. stop the current implementation or document update
2. identify the source of the conflict
3. describe the exact contradiction clearly
4. explain the likely impact
5. return the decision to a human

The system must not continue by assumption.

## `SPEC` Blocking Rule

If the conflict appears in `SPEC-XXX.md`, set its `code_implement` to `blocked`.

Do not clear that state until one of the following is true:

- the conflicting documents are updated, or
- a human explicitly resolves the conflict

## Formal Governance Documents Outside `SPEC`

If the conflict appears in a formal governance document, such as:

- `REQ`
- `ADR`
- `CONTRACT`

do not invent new fields, and do not patch around the problem by force.

Record a warning, then stop.

## Why the System Must Stop

Many teams treat stop conditions as friction.

This system treats stop conditions as protection.

When truth is inconsistent, if the agent keeps moving forward, speed turns from an advantage into a risk. The faster it works, the faster misalignment spreads.

Conflict handling exists to protect the credibility of the entire system output.
