# How to Work with Codex

[中文](../zh/how-to-work-with-codex.md)

This page explains how to ask Codex for the right work in the right scope.

## Start with Four Things

State these items clearly:

- what you want done
- where the scope ends
- which files to read first
- which boundaries must not be crossed

The clearer the prompt, the better the result.

## Minimal Prompt Pattern

```text
Read README.md, Governance.md, and docs/en/getting-started.md first.
Handle ________.
Scope is limited to ________.
Do not change ________.
Run PDR before implementation. If documents conflict, stop and report the conflict.
```

This pattern sets:

- the task
- the scope
- the constraints
- the stop condition

## What You Must Provide

### 1. Task

Avoid vague requests such as:

```text
Help me change this.
```

Use a concrete request such as:

```text
Change the login flow to prefer email login and keep the existing OAuth path.
```

### 2. Scope

Do not force Codex to guess the write boundary.

Example:

```text
Only change the login flow and the related documents. Do not touch billing or permissions.
```

### 3. Relevant Files

If you know the key files, name them first.

Example:

```text
Read docs/REQ/REQ-003.md, docs/SPEC_STEP/SPEC-014.md, and ADR.md first.
```

## When to Stop

Tell Codex to stop when:

- documents conflict
- key information is missing
- the request would cross a stated boundary
- the proposed change needs a governance decision
