# Core Concepts

[中文](../zh/concepts.md)

AxiomFlow works by splitting project truth into different document roles.

Each role answers one kind of question. Once those questions are mixed together, governance starts to become unstable.

## `REQ`

`REQ` defines:

- what problem must be solved
- what result is expected
- which scope is allowed

`REQ` is not an implementation plan.

It is the source of requirement truth.

## `SPEC`

`SPEC` defines:

- how this work should be executed
- what the execution steps are
- what the concrete delivery path is

`SPEC` is where implementation becomes an executable path.

It must stay aligned with `REQ`, `ADR`, and `CONTRACT`.

## `ADR`

`ADR` stands for Architectural Decision Record.

`ADR` defines:

- the architecture direction for the current milestone
- key structural choices
- important system-level reasoning
- supporting diagrams or module-level architectural expansions when needed

`ADR` is meant to explain direction, not every low-level state transition.

At any given time, there must be only one official primary `ADR` source.

There may be supporting ADR files such as module flow diagrams or component diagrams, but they only become active when they are referenced by the primary `ADR`. They must not create a parallel architecture truth.

## `CONTRACT`

`CONTRACT` defines:

- responsibility boundaries
- data boundaries
- control boundaries
- limits that must not be broken

`CONTRACT` is the hardest layer in the system.

If implementation violates it, work must stop.

At any given time, there must be only one official `CONTRACT` source.

## `REFLECT`

`REFLECT` records:

- bugs
- incidents
- lessons
- execution experience worth preserving

`REFLECT` is evidence, not governance itself.

## `SUGGEST`

`SUGGEST` records:

- patterns extracted from multiple `REFLECT` entries
- proposals for governance change
- candidates for upgrade into `ADR` or `CONTRACT`

`SUGGEST` is the proposal layer.

It only becomes active after human approval and a governance upgrade.

## `PDR`

`PDR` is not a document role.

It is the governance gate that evaluates whether execution should proceed.

`PDR` checks whether the current `SPEC` is still aligned with:

- `REQ`
- `ADR`
- `CONTRACT`

Its job is not only to review work before implementation.

Its job is to turn governance into an explicit execution decision:

- proceed
- review first
- stop

In practice, `PDR` should produce a human-readable result that includes:

- a `PDR Summary`
- a terminal status layout
- a short `Summary List`

This is how the system makes alignment visible before `WC` begins.

## Working Samples

The repo includes working samples for these document roles.

- root `docs/` is the default English working sample set
- `Tenets/zh/docs/` is the Chinese sample source

If a Chinese-speaking team wants the repo-level working samples in Chinese, they can manually replace the root `docs/` contents with the files from `Tenets/zh/docs/`.

## Why the Separation Matters

If you do not separate these roles:

- requirements get mixed with implementation detail
- architectural direction gets overridden by local convenience
- boundaries become tacit knowledge
- lessons are forgotten, or applied inconsistently

If you do separate them well:

- the system knows where each type of truth comes from
- the agent knows what it is allowed to rely on
- the team knows where each kind of change belongs

## Trust Order

When conflict appears, trust order decides which document takes priority:

```text
CONTRACT > ADR > REQ > SPEC
SPEC > REFLECT > SUGGEST
```

This structure places formal governance above local execution, and places experience below approved rules until that experience is explicitly upgraded.
