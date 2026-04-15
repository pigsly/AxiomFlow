# Why This Works

[中文](../zh/why-this-works.md)

AxiomFlow works because it combines speed with control.

## 1. Controlled Acceleration

Systems fail when they can accelerate but cannot correct.

In AxiomFlow:

- `WC` is the acceleration point
- `PDR` is the correction point
- conflict handling is the brake

The goal is not to move slowly. The goal is to build execution that can stop, correct, and trace change before scaling speed.

## 2. Alignment First

If direction is wrong, speed only increases the size of the error.

AxiomFlow makes alignment concrete:

- `REQ` aligns problem and scope
- `SPEC_STEP` aligns execution
- `ADR` aligns architecture direction
- `CONTRACT` aligns hard boundaries

`PDR` makes this review mandatory instead of optional.

## 3. Structured Learning

Teams cannot scale reliable learning if lessons remain only in memory.

In AxiomFlow:

- `REFLECT` stores useful evidence
- `SUGGEST` turns repeated evidence into governance candidates
- `GU` applies approved changes to `ADR` or `CONTRACT`

This path lets experience improve the system, not just the conversation around it.
