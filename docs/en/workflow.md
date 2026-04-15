# Workflow

[中文](../zh/workflow.md)

AxiomFlow uses a governed execution loop. The loop does three things:

- verify alignment before work
- keep useful lessons after work
- require approval before governance changes

## 1. `PDR`

`PDR` means Pre-Development Review.

Run it before:

- analysis
- design
- code generation
- document updates

Check:

- whether `SPEC_STEP` matches `REQ`
- whether the implementation follows `ADR`
- whether any rule violates `CONTRACT`
- whether documents conflict, drift, or omit key information

If `PDR` fails, do not continue.

## 2. `WC`

`WC` means Write Code.

Run `WC` only after `PDR` passes. Use the relevant `SPEC-XXX.md` as the implementation guide.

If the `SPEC` has a `code_implement` field, keep the status current:

- `todo`
- `dev`
- `done`
- `blocked`

## 3. `REFLECT`

After meaningful work, record lessons in `REFLECT`.

Examples:

- a bug pattern worth remembering
- a repeated execution mistake
- a failed design assumption
- a `SPEC` misunderstanding that caused rework

Do not record everything. Record events that should change future behavior.

## 4. `GG`

`GG` produces `SUGGEST`.

Its job is to find repeated patterns in `REFLECT` and decide whether they should become formal governance:

- `ADR`
- `CONTRACT`

`SUGGEST` is a proposal, not an active rule.

## 5. `GU`

`GU` means Governance Upgrade.

It happens only after human approval.

When approved, `GU` updates the formal `ADR` or `CONTRACT` and marks related proposals and evidence according to the governance rules.

## Full Loop

```text
REQ -> SPEC_STEP -> PDR -> WC -> REFLECT -> GG -> GU
```
