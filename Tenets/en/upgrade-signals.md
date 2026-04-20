# Upgrade Signals

[中文](../zh/upgrade-signals.md)

This page is not a formal rule.

It answers one very practical question:

**How do you know when it is time to move from Simple to Standard, Advanced, or even Professional?**

## A Story

At the beginning, the team only wants agents to help accelerate development.

The earliest requests are usually simple.

Change one field, patch one API, adjust one flow node.

At that stage, as long as `REQ`, `SPEC`, `ADR`, and `CONTRACT` stay aligned, work can usually finish safely.

That is the problem the [Simple README](../en/README.simple.md) is meant to solve.

But systems do not stay there forever.

## Signal 1: Requirements Are No Longer Local Changes

At first it was only one field, one API, or one flow node.

Later it becomes:

- changing A also requires changing B, C, and D
- one requirement affects data, flow, permissions, and UI at the same time
- small changes start affecting old features

This means the system has moved from local risk into structural risk.

At that point, you at least need to decide whether you can still remain in the Simple version.

If `REQ + SPEC + PDR` is still enough to control the risk, you may stay where you are.
If the team starts repeatedly patching holes, it usually begins moving toward Standard.

## Signal 2: The Same Problem Keeps Returning

For example:

- the same bug keeps coming back
- the same boundary mistake keeps happening
- people remember the fix, but the system does not guarantee it

At that point, it is no longer enough to just fix code.

You need to start preserving experience so errors are not only repaired, but remembered.

That is the starting point of the [Standard README](../en/README.standard.md):

- `REQ -> SPEC -> PDR -> WC -> REFLECT`

The point is not to add process for its own sake.

The point is to stop the team from relying only on human memory to preserve lessons.

## Signal 3: Documents and Implementation Begin to Drift Apart

For example:

- `REQ` says one thing while `SPEC` does another
- `ADR` is not updated, but the actual direction has already drifted
- `CONTRACT` is not written clearly enough, so everyone interprets it differently

This is exactly the situation `PDR` is supposed to handle:

before implementation, check whether `REQ / SPEC / ADR / CONTRACT` are still aligned.

If this drift is no longer a one-off but multiple events keep pointing to the same structural issue, then staying in Standard is often no longer enough.

At that point, teams usually move into the [Advanced README](../en/README.advanced.md) and begin asking:

- should this be upgraded into `ADR`
- or should it be upgraded into `CONTRACT`

## Signal 4: Only Specific People Know How the System Can Be Changed

As soon as you see situations like these:

- only one person knows whether this area can be touched
- only one person knows why it was designed this way
- if that person is unavailable, risk rises sharply

That means knowledge still lives in people instead of being stored as governance assets.

This usually means the team is moving from Standard toward Advanced, because the issue is no longer only whether things should be recorded, but whether the knowledge should be upgraded into formal governance truth.

## Signal 5: Changes Often Need to Stop for Discussion First

Once the team frequently asks questions like:

- will this change violate a boundary?
- is this request still within the original scope?
- should we keep accepting this kind of exception in the future?

That means you are already in a stage where governance modules must participate in decision-making, instead of this being only a coding problem.

That is the situation handled by the [Professional README](../en/README.professional.md):

- human approval
- formal governance upgrades
- conflict blocking
- stop-and-wait behavior

At this level, the system is no longer handling implementation detail.

It is handling the rules themselves.

## Which Version Matches Which Signal

- if you are only making local changes: stay in [Simple](../en/README.simple.md)
- if the same problems keep returning: move up to [Standard](../en/README.standard.md)
- if documents and implementation start drifting apart: usually move toward [Standard](../en/README.standard.md) or [Advanced](../en/README.advanced.md)
- if knowledge is concentrated in a few people: move from [Standard](../en/README.standard.md) toward [Advanced](../en/README.advanced.md)
- if changes frequently need to stop for governance discussion: move into [Professional](../en/README.professional.md)

## How to Read This

If you are still not sure which version you are in:

1. read this story first
2. then read the [Version Guide](./project-scale.md)
3. then choose the matching version README
