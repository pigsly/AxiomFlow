# Feedback Loop

[中文](../zh/feedback-loop.md)

AxiomFlow is not just a document model. It is a controlled learning loop.

## Core Loop

```text
REQ -> SPEC_STEP -> PDR -> WC -> REFLECT -> SUGGEST -> GU -> ADR / CONTRACT
```

Each step has one job:

- `REQ` defines the problem
- `SPEC_STEP` defines the implementation path
- `PDR` checks alignment before work
- `WC` executes only after alignment is confirmed
- `REFLECT` records useful lessons
- `SUGGEST` turns repeated lessons into governance proposals
- `GU` applies approved proposals to formal governance

## Why the Loop Must Close

Many teams already do some of this work:

- write requirements
- write specs
- implement
- learn lessons afterward

The usual gap is the return path. Lessons stay in chat logs, tickets, or memory instead of changing architecture direction or boundaries.

## Control Rules

Three rules make the loop reliable:

- do not implement before alignment review
- do not continue after visible conflict
- do not change governance without approval

These rules keep the system from collapsing into improvisation.

## Feedback Rules

Start feedback with `REFLECT`.

Not every event should become governance. Capture events that matter, such as:

- repeated execution mistakes
- bugs caused by unclear boundaries
- drift between requirement and spec
- misunderstandings about architecture
- governance gaps that slow delivery more than once

When a pattern is clear, convert it into a `SUGGEST`.
