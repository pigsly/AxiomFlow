# Version Guide

[中文](../zh/project-scale.md)

This page answers only one question:

**Which version should you stop at right now, not how far you need to read first.**

If you are still not sure why versions need to upgrade, read [Upgrade Signals](./upgrade-signals.md) first.

## Four-Version Comparison

| Version | Main problem it solves | Core roles you need to understand | Typical flow | When to upgrade |
| --- | --- | --- | --- | --- |
| [Simple](../en/README.simple.md) | Do not start writing code before documents are aligned | `REQ` `SPEC_STEP` `ADR` `CONTRACT` | `REQ -> SPEC_STEP -> PDR -> WC` | the same mistakes begin to repeat, or specs keep needing patches |
| [Standard](../en/README.standard.md) | Preserve repeated mistakes instead of relying on memory alone | `REQ` `SPEC_STEP` `ADR` `CONTRACT` `REFLECT` | `REQ -> SPEC_STEP -> PDR -> WC -> REFLECT` | multiple `REFLECT` entries begin pointing to the same structural issue |
| [Advanced](../en/README.advanced.md) | Turn repeated events into governance candidates | `REQ` `SPEC_STEP` `ADR` `CONTRACT` `REFLECT` `SUGGEST` | `REFLECT -> SUGGEST -> ADR / CONTRACT proposal` | document conflict often blocks development, or formal approval is needed |
| [Professional](../en/README.professional.md) | Keep development controllable even under governance conflict | all roles + human approval / blocking mechanism | `SUGGEST -> approval -> ADR / CONTRACT update` or `conflict -> blocked stop` | this is already the highest level; instead of upgrading further, governance itself needs redesign |

## How to Choose

### Choose Simple

If you are currently stuck in situations like:

- requirements and implementation can still be explained clearly
- most problems are still local changes
- the main goal is to establish `PDR` and the basic guardrails first

### Choose Standard

If you are currently stuck in situations like:

- bugs are no longer first-time events
- specs keep needing patches
- you are starting to feel that some things can no longer be kept only in chat or memory

### Choose Advanced

If you are currently stuck in situations like:

- repeated events have already become patterns
- one patch is no longer enough
- you are starting to judge whether something belongs in `ADR` or in `CONTRACT`

### Choose Professional

If you are currently stuck in situations like:

- document conflict directly blocks development
- one requirement often breaks another requirement
- you need formal approval, blocking, and stop-and-wait behavior

## A Quick Way to Judge

- still asking "how do we do this": stay in Simple first
- starting to ask "why does this keep going wrong": move to Standard
- starting to ask "should this become a formal rule": move to Advanced
- starting to ask "do we need to rewrite the rules before we can continue at all": move to Professional

## Reading Recommendation

After choosing a version, do not immediately go back and read the whole system.

Read in this order first:

1. the matching version README
2. [Getting Started](./getting-started.md)
3. [Core Concepts](./concepts.md)

Go deeper only when needed:

- [Workflow](./workflow.md)
- [Feedback Loop](./feedback-loop.md)
- [Conflict Handling](./conflict-handling.md)
- [Governance.md](../en/Governance.md)
