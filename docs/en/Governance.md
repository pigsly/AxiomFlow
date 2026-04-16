# Governance Rules

[中文](../zh/Governance.md)

## 1. Scope

These rules apply to the governance document types used in the repository:

- `REQ`: requirement documents
- `SPEC_STEP`: implementation-step documents
- `ADR`: architecture decision records
- `CONTRACT`: boundary and interface contracts
- `REFLECT`: records of lessons, incidents, and execution experience
- `SUGGEST`: governance upgrade proposals

Additional rules:

- `REQ` and `SPEC_STEP` are the primary inputs during agent execution.
- `SPEC_STEP` may use `code_implement` to track implementation status.
- `ADR` and `CONTRACT` each allow only one formal primary document at a time.

## 2. Document Roles

### `REQ`

Defines the requirement, goal, scope, and expected result.

### `SPEC_STEP`

Defines the concrete implementation steps and execution details.

Use one `SPEC_Catalogue.md` together with multiple `SPEC-XXX.md` files.

### `ADR`

Defines the current milestone direction, architectural choices, and key decisions.

It is used for direction-level issues and shared structural decisions, not every local implementation detail.

Supporting ADR files are allowed, such as flow diagrams, interaction diagrams, or module-level expansions, but they become active only when the primary `ADR` references them.

### `CONTRACT`

Defines hard boundaries that remain valid across milestones, especially:

- responsibility boundaries
- data boundaries
- control boundaries

### `REFLECT`

Stores human-reviewed lessons, including mistakes, incidents, observations, and execution experience.

`REFLECT` should align with `SPEC_STEP` by default, and should not directly rewrite `REQ`.

### `SUGGEST`

Abstracts repeated patterns from multiple `REFLECT` entries and evaluates whether they should become `ADR` or `CONTRACT` proposals.

`SUGGEST` produces proposals only. It does not become active by itself.

## 3. Trust Order

When documents conflict, the default trust order is:

```text
CONTRACT > ADR > REQ > SPEC_STEP
SPEC_STEP > REFLECT > SUGGEST
```

Interpretation:

- `CONTRACT` is the highest-priority hard constraint
- `ADR` defines the current direction
- `REQ` defines requirement scope
- `SPEC_STEP` defines the execution path
- `REFLECT` is an evidence source
- `SUGGEST` is a proposal source

### Governance Activation Rules

- `REFLECT` is evidence, not formal governance
- `SUGGEST` is a proposal, not formal governance
- `GU` is a governance upgrade action, not a document
- only after human approval may `SUGGEST` content enter the formal `ADR` or `CONTRACT`

## 4. Single Source of Truth

### `ADR`

- only one formal primary `ADR` is allowed
- supporting ADR files may exist for diagrams or local expansions
- supporting ADR files become active only when the primary `ADR` references them
- supporting ADR files may extend the primary `ADR`, but may not create a parallel direction
- if a supporting ADR file conflicts with the primary `ADR`, the primary `ADR` wins
- when milestone direction changes, update the existing primary `ADR` instead of creating a parallel primary version

### `CONTRACT`

- `CONTRACT` defines hard boundaries across major modules
- do not create a new formal version for each milestone unless a human explicitly resets the boundary
- to change a boundary, update `CONTRACT` through `GU` or direct human action

## 5. `PDR`: Pre-Development Review

`PDR` must be executed before all of the following:

- analysis
- design
- code generation
- document updates

`PDR` is both a pre-work review and a governance routing point. It is used to decide whether the issue should remain at the `REQ` or `SPEC_STEP` level, or be escalated into `REFLECT`, `SUGGEST`, `ADR`, or `CONTRACT`.

### Requirement and Spec Checks

- check whether `SPEC_STEP` violates `REQ`
- check whether `REQ` and `SPEC_STEP` contain gaps or drift
- under `SPEC_STEP/`, `SPEC-XXX.md` files are implementation specs and `SPEC_Catalogue.md` is the index of completed specs
- only `SPEC-XXX.md` files with `code_implement: done` may enter `SPEC_Catalogue.md`
- valid `code_implement` states are `todo`, `dev`, `done`, and `blocked`
- `SUG-YYYYMMDDHHMI.md` must list its source `REFLECT-XXX.md` files
- after `GU`, mark the corresponding `SUG-YYYYMMDDHHMI.md` and related `REFLECT-XXX.md` entries as approved

### Architecture and Boundary Checks

- check whether the implementation direction follows `ADR`
- if supporting ADR files are referenced, check whether they still align with the primary `ADR`
- check whether the work violates `CONTRACT`
- check whether `ADR`, `CONTRACT`, and `SPEC_STEP` conflict with each other or leave unclear boundaries

## 6. Conflict Handling Rules

If any of the following are discovered during `PDR` or execution:

- documents conflict with each other
- logic has drifted
- information is missing
- documents are outdated
- output may violate governance documents

then the following process must be taken:

### 1. Block

Immediately stop the current implementation, modification, or output.

- if the conflict appears in `SPEC-XXX.md`, set its `code_implement` to `blocked`
- if the conflict appears in `REQ`, `ADR`, `CONTRACT`, or other governance documents without `code_implement`, do not force new fields into them; instead record a warning and stop for human resolution
- showing the warning in the CLI is sufficient

### 2. Warn

Clearly list:

- the source document of the conflict
- the exact contradiction
- the likely impact scope

### 3. Stop and Wait

Return decision authority to a human.

Until explicit guidance is given or the documents are updated:

- do not invent assumptions
- do not work around the rules
- do not force implementation through

These situations are treated as Level 4 by default, and should no longer be advanced through local patching.

If `SPEC-XXX.md` has already been marked `blocked`, it may be unblocked only after the conflicting documents are updated or a human has explicitly ruled on the conflict. If needed, a human may change it to another status.

## 7. Implementation Limits

- do not produce output that violates `CONTRACT` or `ADR`
- do not expand scope on your own when `REQ`, `ADR`, or `SPEC_STEP` do not cover it
- when details are not covered by `REQ` or `SPEC_STEP`, follow the relevant `ADR` by default
- if `ADR` and `CONTRACT` already place explicit directional limits, user ad hoc phrasing must not override them directly

## 8. Important Operational Commands

- `PDR`
- `REFLECT`: reflect the current event, bug, or spec, and output the lesson as `REFLECT-XXX.md`; if the spec, event, or bug is not important, no lesson needs to be output
- `GG (SUGGEST)`: evaluate the current `REFLECT` set, abstract repeated patterns, and suggest whether they should be elevated into `CONTRACT` or `ADR`; output `SUG-YYYYMMDDHHMI.md`
- `GU (GOVERNANCE_UPGRADE)`: only after human approval, update the formal `ADR` or `CONTRACT` according to a `SUGGEST` proposal; without approval it must not take effect
- `WC (write code)`: start writing code according to `SPEC-XXX.md`; **`PDR` must pass before execution.** After completing the spec, register it in `SPEC_Catalogue.md` and run `REFLECT`

## 9. One-Sentence Principle

**Align the documents first, then begin implementation; if there is conflict, stop instead of forcing progress.**
