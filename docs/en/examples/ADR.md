# ADR

## Context

The project needs one primary architecture source while still allowing module-level flow detail.

## Direction

The system uses governance-first execution instead of execution-first correction.

## Key Decisions

AI-assisted implementation must be constrained by explicit requirement, architecture, and boundary documents before work begins.

- The primary `ADR` remains the single formal source of architecture direction.
- Supporting ADR files may be used for module flows or component-level expansion.
- Supporting ADR files are active only when referenced by this primary ADR.

## Referenced Supporting ADR Files

- [ADR.module-flow.md](./ADR.module-flow.md): module-level component flow example

## Implications

- Teams can document module flow detail without splitting architecture truth into parallel ADRs.
- `PDR` must check that referenced supporting ADR files still align with the primary ADR.
