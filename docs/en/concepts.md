# Core Concepts

[中文](../zh/concepts.md)

AxiomFlow separates project truth by document role. Each role answers one kind of question.

## `REQ`

`REQ` defines:

- the problem to solve
- the expected result
- the allowed scope

`REQ` is not an implementation plan.

## `SPEC_STEP`

`SPEC_STEP` defines:

- how the work will be implemented
- the execution steps
- the delivery path

It must stay aligned with `REQ`, `ADR`, and `CONTRACT`.

## `ADR`

`ADR` defines:

- the current architectural direction
- key structure choices
- system-level reasoning
- any active supporting ADR references

Use one primary `ADR` as the formal source of direction. Supporting ADR files are active only when the primary `ADR` references them.

## `CONTRACT`

`CONTRACT` defines:

- responsibility boundaries
- data boundaries
- control boundaries
- hard limits that cannot be broken

If implementation violates `CONTRACT`, the work must stop.

## `REFLECT`

`REFLECT` records:

- bugs
- incidents
- lessons
- execution patterns worth keeping

`REFLECT` is evidence, not active governance.

## `SUGGEST`

`SUGGEST` records:

- patterns found across `REFLECT` entries
- governance change proposals
- candidates for `ADR` or `CONTRACT`

`SUGGEST` becomes active only after human approval and a governance update.
