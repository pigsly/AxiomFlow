# Getting Started

[中文](../zh/getting-started.md)

Use this page to start AxiomFlow in a new or existing project.

## Setup First: `AGENTS.md`

When you adopt AxiomFlow into another repository, add or update that repository's `AGENTS.md` before you set up document structure.

Use it to tell the agent to read and follow `Governance.md`.

This is not optional guidance. It is the repo-level setup that makes governance visible at the agent entrypoint.

Recommended wording:

```md
Before analysis, design, code generation, or document updates, read and follow `docs/en/Governance.md`.
If the task conflicts with governance documents, stop and ask for clarification instead of continuing by assumption.
```

If this rule is missing, the target repo may contain governance documents but still fail to bind agent behavior to them.

## What You Need

You need six document roles:

- `REQ`
- `SPEC_STEP`
- `ADR`
- `CONTRACT`
- `REFLECT`
- `SUGGEST`

Do not start with the full system unless you need it. Start with enough structure to stop unsafe execution.

## Minimum Set

Start with these files:

- `REQ-001.md`
- `SPEC_STEP/SPEC-001.md`
- `SPEC_STEP/SPEC_Catalogue.md`
- `ADR.md`
- `CONTRACT.md`

This set gives you:

- a clear problem
- an execution path
- one active architecture direction
- one set of hard boundaries
- a list of completed specs

If you need module-level diagrams, keep one primary `ADR.md` and place supporting ADR files in a folder such as `docs/adr/`.

## PDR Rule

Run `PDR` before:

- analysis
- design
- code generation
- document updates

The first benefit is not more documentation. The first benefit is that unsafe work stops early.

## Recommended Adoption Order

1. Write a small `REQ-001`.
2. Break it into one executable `SPEC_STEP`.
3. Refine the `SPEC_STEP` until the work is executable.
4. Extract the initial `ADR` and `CONTRACT` from that first requirement `REQ-001`.
5. Require `PDR` before implementation.
6. Store useful lessons in `REFLECT`.
7. Create `SUGGEST` when the same pattern repeats.
8. Apply governance changes only after human approval through `GU`.

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

Folder names may vary. Document roles and governance rules should not.

## Next

- [Core Concepts](./concepts.md)
- [Workflow](./workflow.md)
- [Examples](./examples/README.md)
