# FAQ

[中文](../zh/faq.md)

## Why not let the agent infer missing details?

Because weak alignment makes inference unsafe. The issue is not whether the agent can infer. The issue is whether the team can control when that inference is safe.

## Why are `ADR` and `CONTRACT` separate?

`ADR` defines direction. `CONTRACT` defines boundaries that must not be violated.

Direction may change with a milestone. Boundaries should remain stable unless humans explicitly change them.

## Why are `REFLECT` and `SUGGEST` not active immediately?

Because experience is evidence, not authority.

Without an approval boundary, every new lesson could silently rewrite governance.

## Why does the system stop instead of doing a best-effort continuation?

Because best-effort continuation is a common way to spread misalignment.

## Is this only for AI agents?

No. It is especially useful for AI-agent workflows, but the model also works for human teams that want stronger alignment.

## Do I need every document type on day one?

No. Start with:

- one `REQ`
- one `SPEC`
- one `ADR`
- one `CONTRACT`
