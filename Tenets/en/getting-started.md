# Getting Started

[中文](../zh/getting-started.md)

This page is not about theory. It is about how to bring AxiomFlow into a new project, or attach it to an existing one.

It applies to workflows that use `Codex CLI` or `Copilot in VS Code` as the main operating entrypoint.

If `README.md` explains why AxiomFlow matters, this page explains how to start using it with the minimum structure that can actually govern execution.

## First Thing: `AGENTS.md`

When you adopt AxiomFlow into another repo, create or update that repo's `AGENTS.md` before you start organizing document structure.

Use it to require the agent to read and follow `Governance.md` first.

This is not just a reminder. It is required repo-level setup. Without it, governance documents may exist, but they still may not actually constrain agent behavior.

Recommended wording:

```md
Before analysis, design, code generation, or document updates, read and follow `Tenets/en/Governance.md`.
If a task conflicts with governance documents, do not continue by assumption or work around it. Stop first and ask for human clarification.
```

If this rule is not written into the target repo's `AGENTS.md` first, later files such as `REQ`, `SPEC`, `ADR`, and `CONTRACT` can easily end up existing as documents without actually being bound to the execution entrypoint.

## Where You Should Start Right Now

If you are currently dealing with situations like these:

- a new project just starting up
- a single requirement or single feature change
- boundaries are still fairly clear
- the main risk is that the agent may start working before alignment is checked

then the minimum starting set is enough:

If you establish only the minimum starting set first, you can begin adopting safely today.

- `REQ`
- `SPEC`
- `ADR`
- `CONTRACT`

If you are already seeing situations like these, do not stop at the minimum set:

- the same bugs or misunderstandings keep returning
- specs keep needing patches
- the team is starting to rely on people remembering lessons instead of the system guaranteeing them
- documents and implementation keep drifting apart

At that point, `REFLECT` should be part of the starting scope.

If you are already seeing more advanced situations like these:

- multiple `REFLECT` entries begin pointing to the same pattern
- the team keeps discussing whether something should become a formal rule
- the team needs to decide whether the issue belongs in `ADR` or `CONTRACT`

then you should no longer stop at the execution layer alone. `SUGGEST` should also be included.

The decision rule is simple:

- first block uncontrolled execution: start with the minimum set
- when repeated mistakes begin: add `REFLECT`
- when structural errors begin repeating: add `SUGGEST`

## Minimum Set

Start with these files:

- `REQ-001.md`
- `SPEC/SPEC-001.md`
- `SPEC/SPEC_Catalogue.md`
- `ADR.md`
- `CONTRACT.md`

These five files are already enough to establish:

- the target problem
- the implementation path
- the current architectural direction
- the hard boundaries
- the index of completed specs

If your project needs module-level architecture diagrams, keep one primary `ADR.md` and put supporting ADR files in a folder such as `Tenets/adr/`.

## What You Need

You need six document roles:

- `REQ`
- `SPEC`
- `ADR`
- `CONTRACT`
- `REFLECT`
- `SUGGEST`

You do not need to deploy the entire system on day one.

You only need enough structure to stop uncontrolled execution.

## Second Thing: `PDR` Rule

Run `PDR` before all of the following:

- analysis
- design
- code generation
- document updates

`PDR` is not one more process step. It is the point where AxiomFlow turns governance into an execution decision.

Before work starts, `PDR` checks whether the current work should continue, whether the direction is clear, and whether the implementation is still inside the approved boundary.

AI is a mirror. If you are clear, the agent amplifies that clarity. If you are vague, it amplifies that vagueness and drives the wrong direction deeper, faster.

So what `PDR` really does is force you to answer: what do you actually want? This is where your real learning begins.

In practice, `PDR` should make three things visible before `WC` begins:

- whether the current `SPEC` is aligned with `REQ`, `ADR`, and `CONTRACT`
- whether execution should proceed or stop
- why the decision was made

The default output should include:

- a `PDR Summary`
- a terminal status layout that shows alignment score, safety gates, and core review signals
- a short `Summary List` explaining the main reasons to proceed, review, or stop

This matters because governance only becomes useful when humans can read the result quickly enough to act on it.

## How to Operate by Adoption Order

The following content can be used through two entrypoints:

- if you use `Codex CLI`, treat it as an operating command
- if you use `Copilot in VS Code`, treat it as a prompt to paste into the chat window

The point is not the interface format. The point is to make the agent work through the same governance sequence.

This is a complete path from setup, to alignment, to execution, to governance upgrade.

### 0. Create or update `AGENTS.md`

Command:

```text
Handle AGENTS.md first.
If the repo does not have AGENTS.md yet, create a minimal working version.
If it already exists, only add the AxiomFlow-required clauses and do not overwrite existing project rules.
Explicitly require the agent to read and follow Tenets/en/Governance.md before analysis, design, coding, or document updates.
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

### 3. Extract the initial `ADR` and `CONTRACT` from the first requirement

Command:

```text
EXTRACT ADR CONTRACT from REQ-???
```

Notes:

`ADR` should contain only architectural direction and reasoning.
`CONTRACT` should contain only responsibility, data, or control boundaries that must not be crossed.
Do not put implementation steps into `ADR`, and do not turn temporary habits into `CONTRACT`.

### 4. Require `PDR` before implementation

Command:

```text
PDR ALL
```

Notes:

Check whether the `SPEC` is aligned with `REQ`, `ADR`, and `CONTRACT`.
If documents conflict, information is missing, boundaries are unclear, or there is a risk of violating `CONTRACT`, stop and list the issues and impact.

Typical outcomes look like this:

- `SPEC-001`: `OK` because the spec stays aligned with `REQ`, `ADR`, and `CONTRACT`
- `SPEC-002`: `Conflict Detected` because the spec changes scoring without updating `REQ`
- `SPEC-003`: `Conflict Detected` because the spec adds `Joker` and breaks the current card boundary

The point is not only to review work before execution. The point is to make go / stop judgment explicit before implementation starts.

### 5. Only enter `WC` after `PDR` passes, and complete the `SPEC`

Command:

```text
WC SPEC-???
```

Notes:

Only enter `WC` after `PDR` passes, based on the approved `SPEC`.
Implementation should stay within the scope authorized by this `SPEC`.
If documents and the current state do not match, stop immediately and report it instead of working around it.

### 6. After execution, record meaningful lessons in `REFLECT`

Command:

```text
REFLECT SPEC-???
```

Notes:

Record only meaningful bugs, lessons, repeated failure patterns, or assumptions that were proven wrong.
If there is not enough value, say directly that `REFLECT` is not needed this time.

### 7. When a pattern repeats, create `SUGGEST`

Command:

```text
SUGGEST ME
```

Notes:

First judge whether the related `REFLECT` records have formed a repeated pattern.
If yes, draft `SUGGEST` with the pattern, risk, and proposed upgrade direction.
Do not directly modify `ADR` or `CONTRACT`.

### 8. Only upgrade governance through `GU` after human approval

Command:

```text
GU SUG-YYYYMMDDHHMI
```

Notes:

Only update formal governance after human approval.
Change only the approved governance scope and mark related proposal or evidence status.
If the approved content conflicts with current governance, stop and list the conflicts first.

## Suggested Layout

```text
Tenets/
  REQ/
    REQ-001.md
  SPEC/
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
- `Tenets/adr/` stores supporting ADR files such as module flows or component diagrams
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
- [Working Samples](../../docs)
