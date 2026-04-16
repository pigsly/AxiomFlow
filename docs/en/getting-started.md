# Getting Started

[中文](../zh/getting-started.md)

This page is not about theory. It is about how to bring AxiomFlow into a new project, or attach it to an existing one.

## Setup First: `AGENTS.md`

When you adopt AxiomFlow into another repo, create or update that repo's `AGENTS.md` before you start organizing document structure.

Use it to require the agent to read and follow `Governance.md` first.

This is not just a reminder. It is required repo-level setup. Without it, governance documents may exist, but they still may not actually constrain agent behavior.

Recommended wording:

```md
Before analysis, design, code generation, or document updates, read and follow `docs/en/Governance.md`.
If a task conflicts with governance documents, do not continue by assumption or work around it. Stop first and ask for human clarification.
```

If this rule is not written into the target repo's `AGENTS.md` first, later files such as `REQ`, `SPEC_STEP`, `ADR`, and `CONTRACT` can easily end up existing as documents without actually being bound to the execution entrypoint.

## What You Need

You need six document roles:

- `REQ`
- `SPEC_STEP`
- `ADR`
- `CONTRACT`
- `REFLECT`
- `SUGGEST`

You do not need to deploy the entire system on day one.

You only need enough structure to stop uncontrolled execution.

## Minimum Set

Start with these files:

- `REQ-001.md`
- `SPEC_STEP/SPEC-001.md`
- `SPEC_STEP/SPEC_Catalogue.md`
- `ADR.md`
- `CONTRACT.md`

These five files are already enough to establish:

- the target problem
- the implementation path
- the current architectural direction
- the hard boundaries
- the index of completed specs

If your project needs module-level architecture diagrams, keep one primary `ADR.md` and put supporting ADR files in a folder such as `docs/adr/`.

## PDR Rule

Run `PDR` before all of the following:

- analysis
- design
- code generation
- document updates

The first gain from this system is not more documentation.

The first gain is that work which should not continue gets stopped early.

## Prompts by Adoption Order

### 0. Create or update `AGENTS.md`

Command:

```text
Read docs/en/getting-started.md first.
Handle AGENTS.md first.
If the repo does not have AGENTS.md yet, create a minimal working version.
If it already exists, only add the AxiomFlow-required clauses and do not overwrite existing project rules.
Explicitly require the agent to read and follow docs/en/Governance.md before analysis, design, coding, or document updates.
If a task conflicts with governance documents, the agent must stop and ask for human clarification.
After that, tell me whether the next step is ready to move into REQ or whether any basic setup is still missing.
```

Notes:

Bind governance to the agent entrypoint first, then move into the rest of the document work.

### 1. Draft a small `REQ`

Command:

```text
Draft a small REQ for ________.
Output it in REQ document format.
If the requirement description is incomplete, list the gaps instead of inventing assumptions.
```

Notes:

Write down the requirement truth first. Do not let `REQ` absorb implementation decisions.

### 2. Derive an executable `SPEC`

Command:

```text
SPEC REQ-???
```

Notes:

Break the `REQ` into an executable work spec, but do not invent new requirements that were not authorized by the `REQ`.
If the `REQ` is not sufficient to support this `SPEC`, stop and point out the gap.

### 3. Refine the `SPEC` until it is directly executable

Command:

```text
Split SPEC-??? for step by step
```

Notes:

Fill in the step order, inputs and outputs, required checkpoints, and expected deliverables.
Do not expand the scope, and do not smuggle in new architectural decisions.
If the refinement has already entered `ADR` or `CONTRACT` territory, stop first.

### 4. Extract the initial `ADR` and `CONTRACT` from the first requirement

Command:

```text
EXTRACT ADR CONTRACT REQ-???
```

Notes:

`ADR` should contain only architectural direction and reasoning.
`CONTRACT` should contain only responsibility, data, or control boundaries that must not be crossed.
Do not put implementation steps into `ADR`, and do not turn temporary habits into `CONTRACT`.

### 5. Require `PDR` before implementation

Command:

```text
PDR
```

Notes:

Check whether the `SPEC` is aligned with `REQ`, `ADR`, and `CONTRACT`.
If documents conflict, information is missing, boundaries are unclear, or there is a risk of violating `CONTRACT`, stop and list the issues and impact.

### 6. Only enter `WC` after `PDR` passes, and complete the `SPEC`

Command:

```text
WC SPEC-???
```

Notes:

Only enter `WC` after `PDR` passes, based on the approved `SPEC`.
Implementation should stay within the scope authorized by this `SPEC`.
If documents and the current state do not match, stop immediately and report it instead of working around it.

### 7. After execution, record meaningful lessons in `REFLECT`

Command:

```text
REFLECT SPEC-???
```

Notes:

Record only meaningful bugs, lessons, repeated failure patterns, or assumptions that were proven wrong.
If there is not enough value, say directly that `REFLECT` is not needed this time.

### 8. When a pattern repeats, create `SUGGEST`

Command:

```text
SUGGEST
```

Notes:

First judge whether the related `REFLECT` records have formed a repeated pattern.
If yes, draft `SUGGEST` with the pattern, risk, and proposed upgrade direction.
Do not directly modify `ADR` or `CONTRACT`.

### 9. Only upgrade governance through `GU` after human approval

Command:

```text
GU SUG-????????????
```

Notes:

Only update formal governance after human approval.
Change only the approved governance scope and mark related proposal or evidence status.
If the approved content conflicts with current governance, stop and list the conflicts first.

## Suggested Layout

```text
docs/
  REQ/
    REQ-001.md
  SPEC_STEP/
    SPEC-001.md
    SPEC_Catalogue.md
  ADR.md
  adr/
    module-a-flow.md
    system-interaction.md
  CONTRACT.md
  REFLECT/
    REFLECT-001.md
  SUGGEST/
    SUG-YYYYMMDDHHMI.md
```

Folder names may vary by repo, but document roles and governance rules should not drift with them.

Recommended ADR convention:

- `ADR.md` is the only official primary ADR source
- `docs/adr/` stores supporting ADR files such as module flows or component diagrams
- supporting ADR files only become active when they are referenced by `ADR.md`

## How to Know You Are Using It Correctly

If you see the following, the system is starting to work correctly:

- implementation does not start before alignment is checked
- work stops when conflict appears instead of forcing a workaround
- architectural direction is explicit
- boundaries are explicit
- repeated errors produce governance proposals
- formal rules change only after human approval

## Next

- [Core Concepts](./concepts.md)
- [Workflow](./workflow.md)
- [Conflict Handling](./conflict-handling.md)
- [Examples](./examples/README.md)
