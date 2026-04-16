# AxiomFlow

![AxiomFlow logo](./AxiomFlow_logo.png)

**Turn AI agents into governable builders.**

> Bound acceleration. Trace evolution.

AxiomFlow is a governance model for AI-assisted software delivery.

It is designed to keep AI-accelerated execution aligned, bounded, and traceable.

## BEFORE

AI helps teams rapidly produce requirements, proposals, code, and documentation.
At first, everything feels fast. But after a few weeks, the real problems start to surface:

- requirements, design, and architectural decisions get mixed together, making the project harder and harder to reason about later
- many important judgments seem reasonable in the moment, but later nobody can clearly explain why they were made
- boundaries and constraints are never written down clearly, and exist only in a few people's heads
- when new members take over, they can see the output but cannot reconnect the context
- AI can always produce content, but the standard is inconsistent, so the team keeps compensating afterward

In the end, the project looks like it is moving forward,
but in reality it is accelerating the spread of confusion.

## AFTER

AxiomFlow does not add one more layer of process.

It separates the different layers of project problems so they can be governed independently:

- `REQ`: what problem is actually being solved right now
- `SPEC`: how this work is going to be implemented
- `ADR`: why this direction was chosen instead of another one
- `CONTRACT`: which boundaries must not be crossed and which principles must not be broken

Once the problem, method, reasoning, and boundaries are separated clearly,
AI is no longer just producing more output.

It starts helping the project move forward in a way that is understandable, verifiable, and transferable.

The result is not that AI becomes slower.

It is that the more AI does, the more the team understands what it is doing.
## Start Here

Use this short path if you are new to the repo.

- [中文 README](./README.zh.md)
- [Getting Started](./docs/en/getting-started.md)
- [Version Guide](./docs/en/project-scale.md)
- [Upgrade Signals](./docs/en/upgrade-signals.md)

## Document Roles

Each document answers one question:

- `REQ`: what problem must be solved
- `SPEC`: how the work will be done
- `ADR`: why the architecture is taking this direction
- `CONTRACT`: which boundaries must not be crossed
- `REFLECT`: which lessons are worth keeping
- `SUGGEST`: which lessons may need a governance upgrade

Use only the roles you need for the current stage.

## Choose a Version

- [Simple](./docs/en/README.simple.md): for local, low-conflict work that mainly needs alignment before execution
- [Standard](./docs/en/README.standard.md): for teams that need to preserve repeated lessons through `REFLECT`
- [Advanced](./docs/en/README.advanced.md): for cases where repeated patterns need to be evaluated as `ADR` or `CONTRACT` candidates
- [Professional](./docs/en/README.professional.md): for high-conflict environments that require formal approval and stop authority

## Read by Topic

- Start the repo setup: [Getting Started](./docs/en/getting-started.md)
- Understand the document roles: [Core Concepts](./docs/en/concepts.md)
- See the execution loop: [Workflow](./docs/en/workflow.md)
- Learn when work must stop: [Conflict Handling](./docs/en/conflict-handling.md)
- See how learning feeds governance: [Feedback Loop](./docs/en/feedback-loop.md)
- Know when teams should upgrade: [Upgrade Signals](./docs/en/upgrade-signals.md)
- Choose the right operating version: [Version Guide](./docs/en/project-scale.md)
- Learn how to adopt it in a real team: [Adoption Guide](./docs/en/adoption-guide.md)
- See where it fits best: [Use Cases](./docs/en/use-cases.md)
- Understand why the model works: [Why This Works](./docs/en/why-this-works.md)
- Read the formal rules last: [Governance.md](./docs/en/Governance.md)
- Check common questions: [FAQ](./docs/en/faq.md)
- Review practical samples: [Examples](./docs/en/examples/README.md)
- See contribution guidance: [Contributing](./docs/en/CONTRIBUTING.md)

## Language

- English docs: [docs/en](./docs/en/README.md)
- 中文文件: [docs/zh](./docs/zh/getting-started.md)

## Community

- GitHub Issues: https://github.com/pigsly/AxiomFlow/issues
- X.com @pigslybear
- Contributing: [docs/en/CONTRIBUTING.md](./docs/en/CONTRIBUTING.md)
- Related project: [ClawMind](https://github.com/pigsly/ClawMind)
