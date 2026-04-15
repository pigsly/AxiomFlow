# Adoption Guide

[中文](../zh/adoption-guide.md)

This page explains how to introduce AxiomFlow to a real team without rebuilding the whole process at once.

## Start Small

Do not begin with a full documentation bureaucracy.

Start with the minimum governance surface that can stop unsafe work:

- one `REQ`
- one `SPEC_STEP`
- one `ADR`
- one `CONTRACT`

This is enough to define:

- what to build
- how to build it
- where architecture is going
- which boundaries must not be crossed

## Phase 1: Build Control First

The first goal is control, not completeness.

At this stage:

1. Define the active requirement.
2. Define the executable spec.
3. Define the current architecture direction.
4. Define the active boundary contract.
5. Require `PDR` before implementation.

## Phase 2: Establish Stop Rules

After the minimum set exists, agree on stop conditions.

Stop execution when:

- `SPEC_STEP` conflicts with `REQ`
- implementation direction conflicts with `ADR`
- proposed work violates `CONTRACT`
- key information is missing

## Phase 3: Keep Useful Lessons

Once the team uses `PDR` reliably, start writing `REFLECT`.

Record only lessons worth preserving:

- repeated misunderstandings
- bugs caused by document mismatch
- recurring boundary violations
- execution patterns that should affect future governance

## Phase 4: Upgrade Governance Deliberately

When patterns repeat, create `SUGGEST`.

This step turns local experience into a governance proposal. Governance upgrades must go through human approval.

## Team Responsibilities

Different teams can assign responsibilities differently, but someone must own:

- requirement quality
- implementation path quality
- architecture direction
- boundary control
- conflict escalation
