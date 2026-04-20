# FAQ

[中文](../zh/faq.md)

## Why not let the agent infer missing details?

Because inference under weak alignment is one of the main failure modes in AI-assisted engineering.

The problem is not that the agent cannot infer.

The problem is that the team cannot reliably control when those inferences are safe.

## Why are `ADR` and `CONTRACT` separate?

`ADR` defines direction.

`CONTRACT` defines boundaries that must not be violated.

Direction may evolve with a milestone.

Boundaries should remain stable unless humans explicitly change them.

## Why are `REFLECT` and `SUGGEST` not immediately active?

Because experience is evidence, not authority.

Without an approval boundary, every new lesson could silently rewrite governance and create instability.

## Why does the system stop instead of trying a best-effort continuation?

Because best-effort continuation is how misalignment spreads.

This system is designed for controlled execution, not optimistic execution.

## Is this only for AI agents?

No.

It is especially useful for AI-agent workflows, but the model also works for human teams that want stronger alignment between requirements, architecture, implementation, and learning.

## Do I need every document type on day one?

No.

You should start with the minimum governance surface:

- one `REQ`
- one `SPEC`
- one `ADR`
- one `CONTRACT`

Then add `REFLECT` and `SUGGEST` when you want operational learning to feed back into governance.
