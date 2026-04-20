# OpenAI Agents SDK vs Codex CLI

[中文](../../zh/integration/openai-agents-vs-codex-cli.md)

This guide compares:

- `openai-agents-python`
- Codex CLI

Use it to decide which layer should work with AxiomFlow.

## Short Answer

- `openai-agents-python`: build your own agent system
- Codex CLI: use a ready-made coding agent to do work directly

## Product Position

### `openai-agents-python`

This is a Python SDK for building agent workflows.

It supports:

- `Agent`
- `Handoffs`
- `Guardrails`
- `Sessions`
- `Tracing`
- `Human-in-the-loop`

Use it when you want to design the workflow engine itself.

### Codex CLI

This is an interactive coding agent for terminal work.

Use it when you want an agent that can:

- read a codebase
- edit files
- run commands
- complete short development loops with direct human collaboration

## Control Model

With `openai-agents-python`, you decide:

- which agents exist
- how handoffs work
- which guardrails run first
- which steps need approval

With Codex CLI, you mainly:

- give prompts
- review execution
- control access through sandbox and approval settings

## Best Fit with AxiomFlow

### Use `openai-agents-python` as the governance engine

It fits when you want to encode:

- `PDR`
- `GU`
- stop conditions
- multi-agent handoff
- traceable execution

### Use Codex CLI as the operations layer

It fits when you want to:

- patch local code
- inspect an unfamiliar repo
- run tests
- refactor
- execute one task or one short cycle at a time

Codex CLI 更適合做：

- `executor`
- `verifier`
- 本地互動入口
- codebase 直接操作

換句話說：

- 它比較像工作代理
- 不是治理核心本身

## 5. 真正差異不在「誰比較強」

不是一個比較高級，另一個比較低級。

真正差異是：

- `openai-agents-python` 偏系統搭建
- Codex CLI 偏日常操作

## 6. 如果套回這個 repo

### 用 `openai-agents-python`

你可以把這套治理模型做成：

- `REQ` 起草 agent
- `SPEC_STEP` 規劃 agent
- `PDR` guardrail
- `executor` handoff
- `REFLECT` 產生器
- `SUGGEST` 提案 agent
- `GU` 人類批准節點

優點：

- 治理規則可以內建
- 流程可重複
- 高風險控制比較穩

代價：

- 你要自己實作系統
- 前期設計成本比較高

### 用 Codex CLI

你可以把這套治理模型用操作約定的方式落地：

- 先看 `REQ`
- 再看 `SPEC_STEP`
- 過 `PDR`
- 再讓 agent 改 code
- 遇到衝突時停機

優點：

- 立刻可用
- 非常適合工程日常工作
- 本地 terminal 操作順

代價：

- 治理規則比較像人與流程約定
- 不像 SDK 那樣容易做成程式內建限制

## 7. 實務建議

如果你的目標是：

### 1. 先讓團隊開始用 agent 做事

先用 Codex CLI 會比較快。

因為：

- 進入成本低
- 可以直接在 repo 裡工作
- 很適合先把 `REQ / SPEC_STEP / PDR / WC` 跑起來

### 2. 把治理做成真正可執行的系統

用 `openai-agents-python` 會更適合。

因為：

- 你可以把規則寫成程式
- 可以做正式 handoff
- 可以做 approval gate
- 可以把 stop condition 做成 guardrail

### 3. 最穩的分工方式

最實務的做法通常不是二選一，而是分層：

- `openai-agents-python` 當治理核心
- Codex CLI 當本地工作代理與操作入口

也就是：

- SDK 管流程
- CLI 管執行

## 8. 對照表

| 面向 | `openai-agents-python` | Codex CLI |
| --- | --- | --- |
| 主要定位 | agent workflow SDK | terminal coding agent |
| 你在做什麼 | 建系統 | 用工具 |
| 控制流 | 自己寫 | 內建 agent loop |
| guardrail | 可程式化 | 以操作與 approval 為主 |
| handoff | 正式原語 | 沒有同等級可程式化 handoff 原語 |
| HITL | 很自然 | 有互動，但不是以 workflow gate 為核心 |
| tracing | 內建重點能力 | 不以 tracing pipeline 為核心 |
| 本地 coding 體驗 | 需自己接 | 很強 |
| 治理規則內建化 | 很適合 | 較弱 |
| 上手速度 | 較慢 | 較快 |
| 適合這個 repo 的位置 | 治理核心 | 操作層 |

## 9. 結論

如果你只是想直接在本地做工程工作，Codex CLI 比較直接。

如果你想把 AxiomFlow 變成真正可執行、可驗證、可阻斷的 agent 系統，`openai-agents-python` 會更契合。

最合理的組合通常是：

- 用 `openai-agents-python` 實作治理流程
- 用 Codex CLI 執行本地工程任務

## Sources

Official sources used:

- OpenAI Agents SDK docs: https://openai.github.io/openai-agents-python/
- OpenAI Agents SDK repo: https://github.com/openai/openai-agents-python
- Agents SDK model/docs navigation: https://openai.github.io/openai-agents-python/models/
- OpenAI Codex getting started/help: https://help.openai.com/en/articles/11096431-openai-codex-ci-getting-started
- OpenAI Codex product/articles:
  - https://openai.com/index/unrolling-the-codex-agent-loop/
  - https://openai.com/index/introducing-the-codex-app/

This comparison also includes integration judgment based on this repository's governance model. That mapping is an inference, not a statement from OpenAI.
