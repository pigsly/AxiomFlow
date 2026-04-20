# Templates


This directory contains reusable starter templates for the core governance document types.

Use these files when adopting AxiomFlow in a new repository.

## Included Templates

- [REQ.template.md](./REQ.template.md)
- [SPEC.template.md](./SPEC.template.md)
- [SPEC_Catalogue.template.md](./SPEC_Catalogue.template.md)
- [ADR.template.md](./ADR.template.md)
- [CONTRACT.template.md](./CONTRACT.template.md)
- [REFLECT.template.md](./REFLECT.template.md)
- [SUGGEST.template.md](./SUGGEST.template.md)

These templates are intentionally lightweight. They are meant to preserve the role of each document, not force one rigid writing style.

## Recommended ADR Layout

If you adopt supporting ADR files, use this convention:

```text
Tenets/
  ADR.md
  adr/
    module-a-flow.md
    system-interaction.md
```

- `ADR.md` is the primary ADR source
- files under `Tenets/adr/` are supporting ADR files
- supporting ADR files should be referenced from `ADR.md` before being treated as active governance
