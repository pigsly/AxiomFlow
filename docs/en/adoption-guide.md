# Adoption Guide

[中文](../zh/adoption-guide.md)

This document is about how to bring AxiomFlow into a real team, instead of trying to rebuild the whole management system on day one.

## Start Small

Do not begin by turning it into a full documentation bureaucracy.

Start by building the smallest governance surface that is still enough to block unsafe execution:

- one `REQ`
- one `SPEC_STEP`
- one `ADR`
- one `CONTRACT`

That is already enough to establish:

- what needs to be done
- how the work should be done
- where the architecture is going
- which boundaries must not be crossed

## Phase 1: Build Control First, Then Talk About Expansion

The first goal is not completeness.

The first goal is control.

At this stage:

1. define one currently valid requirement
2. define one currently executable spec
3. define one current architecture direction
4. define one current boundary contract
5. require `PDR` before implementation

If you can do this much, your AI delivery loop is already safer than most teams.

## Phase 2: Establish Stop Conditions

Once the minimum document set exists, start enforcing stop rules.

The team must agree that execution stops whenever any of the following happens:

- `SPEC_STEP` conflicts with `REQ`
- implementation direction conflicts with `ADR`
- proposed work violates `CONTRACT`
- key information is missing

From this point on, the system changes not only the documents, but team behavior.

## Phase 3: Preserve Learning

Once the team is using `PDR` steadily, start using `REFLECT` to preserve meaningful experience.

Do not record everything.

Record only what is actually worth keeping:

- repeated misunderstandings
- bugs caused by document mismatch
- recurring boundary violations
- execution patterns that should influence future governance

## Phase 4: Upgrade Governance Deliberately

When patterns begin to repeat, create `SUGGEST`.

This step is the bridge between local experience and formal governance.

Governance upgrades can only happen through human-approved `GU`.

This matters because it keeps the system from destabilizing every time it learns something new.

## Team Responsibilities

Different teams may assign roles differently, but these responsibilities must be owned by someone:

- someone owns requirement truth
- someone owns architecture direction
- someone owns hard boundary definition
- someone executes or approves pre-development review
- someone decides whether proposals become formal governance

This model does not require a rigid org chart, but it does require clear decision ownership.

## Common Adoption Mistakes

Avoid these mistakes:

- writing many templates before defining decision ownership
- treating `ADR` as implementation detail
- writing `CONTRACT` as a long technical memo instead of hard boundaries
- recording everything in `REFLECT`
- letting `SUGGEST` behave like formal governance before approval
- continuing implementation after conflict is already visible

## What Good Adoption Looks Like

When you see these conditions, adoption is moving in the right direction:

- agents do not start work before alignment review
- conflicts lead to escalation instead of improvisation
- architecture and boundaries stay visible throughout delivery
- lessons are preserved without bypassing formal governance
- the team can clearly explain why a decision was allowed, blocked, or upgraded

## Recommended Adoption Order

For most teams, this order is enough:

1. publish `README.md`
2. create the minimum document set
3. require `PDR`
4. apply stop rules
5. start using templates
6. record meaningful `REFLECT`
7. use `SUGGEST` to inspect repeated patterns
8. upgrade governance through approved `GU`
