# ADR Module Flow Example

This file is a supporting ADR file.

It is only active because it is referenced by [ADR.md](./ADR.md).

If this file conflicts with the primary ADR, the primary ADR wins.

## Module

Example Delivery Module

## Purpose

Expand the primary ADR with one module-level component flow.

## Component Flow

```mermaid
flowchart LR
    REQ[REQ Input] --> SPEC[SPEC Planning]
    SPEC --> PDR[PDR Check]
    PDR --> WC[WC Execution]
    WC --> RESULT[Module Output]
```

## Notes

- This file explains one module flow only.
- It does not define a separate architecture direction.
