# Feedback Loop

[中文](../zh/feedback-loop.md)

AxiomFlow is not just a document model.

It is a closed loop that makes execution controllable and learning controllable.

Without this loop, the system becomes static documentation.

With this loop, the system becomes a governance engine.

## Core Loop

The minimum loop looks like this:

```text
REQ -> SPEC_STEP -> PDR -> WC -> REFLECT -> SUGGEST -> GU -> ADR / CONTRACT
```

Each step has its own job:

- `REQ` defines what problem must be solved
- `SPEC_STEP` defines how the work should be done
- `PDR` checks whether the plan is aligned before execution
- `WC` implements only after alignment is confirmed
- `REFLECT` records meaningful experience from execution
- `SUGGEST` turns repeated lessons into governance proposals
- `GU` upgrades approved proposals into formal governance

This loop matters because it blocks two failure modes:

- execution starts before alignment is checked
- learning happens, but structure does not improve with it

## Why the Loop Must Close

Many teams already do part of this:

- write requirements
- write specs
- implement
- learn something afterwards

What is usually missing is the return path.

Lessons stay in chat history, ticket comments, or individual memory, but never actually enter architecture direction or boundary governance.

This system adds the missing path upward, but only through explicit approval.

## Control Mechanism

This loop does not just let things flow.

It lets them flow under control.

What makes the loop trustworthy are three rules:

- no implementation before alignment review
- no continuation after conflict becomes visible
- no governance change before approval

These three rules are what stop the system from degrading into improvisation.

## Feedback Mechanism

The feedback mechanism starts with `REFLECT`.

Not every event should become governance. The system should only retain events that actually matter, such as:

- repeated execution mistakes
- bugs caused by boundary confusion
- drift from requirement to spec
- misunderstandings about architecture
- governance gaps that repeatedly slow or damage delivery

Once a pattern appears, `SUGGEST` translates it into a governance proposal.

The key difference is here:

- `REFLECT` preserves evidence
- `SUGGEST` interprets evidence
- `GU` changes the system

This separation makes the feedback loop useful without making governance unstable.

## Fast Loop and Slow Loop

This model actually contains two loops running at different speeds.

### Fast Loop

The fast loop handles daily delivery:

```text
REQ -> SPEC_STEP -> PDR -> WC
```

Its job is to control execution quality.

### Slow Loop

The slow loop handles governance evolution:

```text
REFLECT -> SUGGEST -> GU -> ADR / CONTRACT
```

Its job is to improve the rules of the system itself.

Healthy projects run both loops at the same time.

Unhealthy projects run only the fast loop, then keep crashing into the same failure patterns.

## What Good Feedback Looks Like

A good feedback loop does not create paperwork for every small event.

A good feedback loop does this:

- catches real mismatch before implementation
- preserves only meaningful lessons
- recognizes patterns instead of chasing noise
- upgrades governance only after humans confirm that the pattern is real

That is how the system stays strict and pragmatic at the same time.
