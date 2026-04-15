# Upgrade Signals

[中文](../zh/upgrade-signals.md)

This page explains when a team should move from Simple to Standard, Advanced, or Professional.

## Signal 1: Requirements Are No Longer Local

At first, the team changes one field, one API, or one flow step.

Later, one request starts affecting:

- multiple modules
- data, flow, permissions, and UI together
- older features in indirect ways

This is the point where local risk becomes structural risk.

## Signal 2: The Same Problem Keeps Returning

Examples:

- the same bug returns
- the same boundary error returns
- the team relies on memory instead of system rules

This is the point to start `REFLECT`.

## Signal 3: Documents and Implementation Drift Apart

Examples:

- `REQ` says one thing and `SPEC_STEP` says another
- `ADR` is outdated
- `CONTRACT` is too unclear for consistent use

This is the point where `PDR` becomes critical and `SUGGEST` may be necessary.

## Signal 4: Only Specific People Know How to Change the System

If delivery depends on unwritten knowledge from a few people, governance is too weak.

That often means architecture direction or hard boundaries need to be made explicit.

## Signal 5: Governance Conflict Blocks Delivery

If teams stop because they cannot tell which document to trust, you are already in Professional territory.
