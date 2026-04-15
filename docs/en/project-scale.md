# Version Guide

[中文](../zh/project-scale.md)

This page answers one question: which version should you stop at right now?

If you are not sure why a team should upgrade, read [Upgrade Signals](./upgrade-signals.md) first.

## Comparison

| Version | Main Problem | Core Roles | Typical Flow | Upgrade Signal |
| --- | --- | --- | --- | --- |
| [Simple](./README.simple.md) | Stop agents from coding before alignment | `REQ` `SPEC_STEP` `ADR` `CONTRACT` | `REQ -> SPEC_STEP -> PDR -> WC` | repeated mistakes or constant spec patching |
| [Standard](./README.standard.md) | Preserve repeated lessons | `REQ` `SPEC_STEP` `ADR` `CONTRACT` `REFLECT` | `REQ -> SPEC_STEP -> PDR -> WC -> REFLECT` | multiple `REFLECT` entries point to the same structure problem |
| [Advanced](./README.advanced.md) | Turn repeated events into governance proposals | `REQ` `SPEC_STEP` `ADR` `CONTRACT` `REFLECT` `SUGGEST` | `REFLECT -> SUGGEST -> ADR / CONTRACT proposal` | governance conflict starts to block delivery |
| [Professional](./README.professional.md) | Keep delivery controllable under governance conflict | all roles plus human approval and stop rules | `SUGGEST -> approval -> ADR / CONTRACT update` or `conflict -> stop` | highest governance level; next step is governance redesign, not upgrade |

## How to Choose

Choose Simple when:

- most work stays inside one module
- `REQ + SPEC_STEP` is enough to describe the work
- `ADR` and `CONTRACT` act mainly as guardrails

Choose Standard when:

- the same bug has happened more than once
- specs keep needing patches
- the team needs to store lessons outside chat

Choose Advanced when:

- repeated events form a pattern
- patches no longer fix the root cause
- you need to decide whether the issue belongs in `ADR` or `CONTRACT`

Choose Professional when:

- document conflict blocks delivery
- one change often breaks another requirement
- you need formal approval and stop authority

## Recommended Reading Order

1. Read the matching version guide.
2. Read [Getting Started](./getting-started.md).
3. Read [Core Concepts](./concepts.md).
4. Continue with deeper documents only when needed.
