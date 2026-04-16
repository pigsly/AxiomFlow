# Workflow

[中文](../zh/workflow.md)

The core of AxiomFlow is a governance-constrained execution loop.

This loop does three things only: verify alignment before execution, preserve lessons after execution, and require approval before governance is upgraded.

## 1. `PDR`

`PDR` means Pre-Development Review.

It must happen before all of the following:

- analysis
- design
- code generation
- document updates

`PDR` checks:

- whether `SPEC_STEP` has drifted from `REQ`
- whether the implementation direction follows `ADR`
- whether any rule would violate `CONTRACT`
- whether documents contain conflict, drift, or critical gaps

If `PDR` does not pass, execution must not continue.

## 2. `WC`

`WC` means Write Code.

Only after `PDR` passes may work enter `WC`. `WC` implements according to `SPEC-XXX.md`.

If the related `SPEC` has a `code_implement` field, its status should reflect implementation progress, for example:

- `todo`
- `dev`
- `done`
- `blocked`

## 3. `REFLECT`

After meaningful work, errors, events, or findings, write the lessons into `REFLECT`.

For example:

- a bug pattern worth remembering
- repeated execution mistakes
- a design assumption that was proven wrong
- a misunderstanding of `SPEC` that caused rework

Not everything should be recorded.

Only meaningful events are worth preserving as long-term experience.

## 4. `GG`

`GG` produces `SUGGEST`.

Its purpose is to inspect repeated patterns in `REFLECT` and judge whether those lessons should be upgraded into formal governance:

- `ADR`
- `CONTRACT`

But `SUGGEST` is still not formal governance.

It is only a proposal.

## 5. `GU`

`GU` means Governance Upgrade.

This step can happen only after human approval.

Once approved, `GU` updates the formal `ADR` or `CONTRACT`, and marks the status of related proposals and evidence according to governance rules.

## Full Loop

```text
REQ -> SPEC_STEP -> PDR -> WC -> REFLECT -> GG -> GU
```

This forms a system: current truth constrains current implementation, while new experience can improve future truth, but never bypass approval.

## What Is Actually Different About This Workflow

Most development workflows optimize throughput.

This workflow optimizes controllable throughput.

When agent speed is already fast enough to amplify errors together with progress, that difference becomes important.
