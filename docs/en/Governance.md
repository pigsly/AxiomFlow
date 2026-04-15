# Governance Rules


## 1. Scope

These rules apply to the governance document types used in the repository:

- `REQ`: requirement documents
- `SPEC_STEP`: implementation-step documents
- `ADR`: architecture decision records
- `CONTRACT`: boundary and interface contracts
- `REFLECT`: recorded lessons and incidents
- `SUGGEST`: governance upgrade proposals

Additional rules:

- `REQ` and `SPEC_STEP` are the primary inputs for agent execution.
- `SPEC_STEP` may use `code_implement` to track implementation status.
- `ADR` and `CONTRACT` each allow only one formal primary document at a time.

## 2. Document Roles

### `REQ`

Defines the requirement, goal, scope, and expected result.

### `SPEC_STEP`

Defines concrete implementation steps and execution detail.

Use one `SPEC_Catalogue.md` plus multiple `SPEC-XXX.md` files.

### `ADR`

Defines the current milestone direction, architectural choices, and key decisions.

Use it for directional issues and shared structure decisions, not every local implementation detail.

Supporting ADR files are allowed for flow diagrams, interaction diagrams, or module-level expansion, but they are active only when the primary `ADR` references them.

### `CONTRACT`

Defines hard boundaries that remain valid across milestones, especially:

- responsibility boundaries
- data boundaries
- control boundaries

### `REFLECT`

Stores human-reviewed lessons such as mistakes, incidents, observations, and execution experience.

`REFLECT` should align to `SPEC_STEP` by default and should not directly rewrite `REQ`.

### `SUGGEST`

Abstracts repeated patterns from `REFLECT` entries and evaluates whether they should become `ADR` or `CONTRACT` proposals.

`SUGGEST` produces proposals only. It does not activate governance by itself.

## 3. Trust Order

When documents conflict, use this default trust order:

```text
CONTRACT > ADR > REQ > SPEC_STEP
SPEC_STEP > REFLECT > SUGGEST
```

Interpretation:

- `CONTRACT` is the highest-priority hard constraint.
- `ADR` defines current direction.
- `REQ` defines requirement scope.
- `SPEC_STEP` defines the execution path.
- `REFLECT` is an evidence source.
- `SUGGEST` is a proposal source.

### Governance Activation Rules

- `REFLECT` is evidence and is not active governance.
- `SUGGEST` is a proposal and is not active governance.
- `GU` is a governance upgrade action, not a document.
- Only human approval can move `SUGGEST` content into the formal `ADR` or `CONTRACT`.

## 4. Single Source of Truth

### `ADR`

- Allow one formal primary `ADR`.
- Supporting ADR files may exist for diagrams or local expansions.
- A supporting ADR file is active only when the primary `ADR` references it.
- A supporting ADR file may expand the primary `ADR` but may not define a parallel direction.
- If a supporting ADR file conflicts with the primary `ADR`, the primary `ADR` wins.
- When milestone direction changes, update the existing primary `ADR` instead of creating parallel primary versions.

### `CONTRACT`

- `CONTRACT` defines hard boundaries across major modules.
- Do not create a new formal version for each milestone unless a human explicitly resets the boundary.
- To change a boundary, update `CONTRACT` through `GU` or direct human action.

## 5. `PDR`: Pre-Development Review

Run `PDR` before:

- analysis
- design
- code generation
- document updates

`PDR` is both a pre-work review and a governance routing point. It decides whether the issue should stay at the `REQ` or `SPEC_STEP` level or be escalated into `REFLECT`, `SUGGEST`, `ADR`, or `CONTRACT`.

### Requirement and Spec Checks

- Check whether `SPEC_STEP` violates `REQ`.
- Check whether `REQ` and `SPEC_STEP` have gaps or drift.
- Under `SPEC_STEP/`, `SPEC-XXX.md` files are implementation specs and `SPEC_Catalogue.md` is the index of completed specs.
- Only `SPEC-XXX.md` files with `code_implement: done` may enter `SPEC_Catalogue.md`.
- Valid `code_implement` states are `todo`, `dev`, `done`, and `blocked`.
- `SUG-YYYYMMDDHHMI.md` must list the source `REFLECT-XXX.md` files.
- After `GU`, mark the corresponding `SUG-YYYYMMDDHHMI.md` and linked `REFLECT-XXX.md` entries as approved.

### Architecture and Boundary Checks

- Check whether the implementation direction matches `ADR`.
- If supporting ADR files are referenced, check whether they still align with the primary `ADR`.
- Check whether the work violates `CONTRACT`.
- Check whether `ADR`, `CONTRACT`, and `SPEC_STEP` conflict or leave unclear boundaries.

## 6. 衝突處理規則

若在 `PDR` 或執行過程中發現以下情況：

- 文件彼此衝突
- 邏輯背離
- 資訊缺漏
- 文件過期
- 產出可能違反治理文件

則必須採取以下流程：

### 1. 阻斷

立即停止當前實作、修改或產出。

- 若衝突發生在 `SPEC-XXX.md`，則將其 `code_implement` 設為 `blocked`
- 若衝突發生在 `REQ`、`ADR`、`CONTRACT` 或其他沒有 `code_implement` 的治理文件，則不得強行補欄位；改以警告記錄衝突並停機等待
- 警告記錄顯示在 CLI 介面即可

### 2. 警告

清楚列出：

- 衝突來源文件
- 具體矛盾點
- 可能影響範圍

### 3. 停機等待

將決策權交還給人類。

在未獲明確裁示或文件未更新前：

- 不得自行腦補
- 不得繞過規則
- 不得強行實作

這類情況預設視為 Level 4，不再以局部補丁方式繼續推進。

若 `SPEC-XXX.md` 已被標記為 `blocked`，只有在衝突文件已更新或人類已明確裁示後，才能解除 `blocked`。人類如果有需要會改成其他狀態。

---

## 7. 實作限制

- 不得產出違反 `CONTRACT`、`ADR` 的內容
- 不得在 `REQ`、`ADR`、`SPEC_STEP` 未覆蓋的情況下，自行擴張範圍
- 當細節未被 `REQ` 或 `SPEC_STEP` 覆蓋時，預設依循相關 `ADR`
- 若 `ADR` 與 `CONTRACT` 已明確限制方向，不得以使用者臨時語句直接覆蓋

---

## 8. 重要維運命令

- PDR
- REFLECT: 反映當前事件、BUG、SPEC，並將經驗輸出 REFLECT-XXX.md，如果SPEC,事件,BUG不重要，可以不輸出經驗。
- GG(SUGGEST): 評估目前經驗(REFLECT)集合, 對重複模式進行抽象，建議這個經驗應該轉入CONTRACT或ADR，輸出文字SUG-YYYYMMDDDHHMI.md(CONTRACT/ADR, REFLECT-XXX.md)。
- GU(GOVERNANCE_UPGRADE): 僅在人類批准後，依 SUGGEST 提案(SUG-YYYYMMDDDHHMI.md)更新正式 ADR 或 CONTRACT；未經批准不得生效。
- WC(write code): 依SPEC-XXX.md的規格，開始撰寫CODE；**執行前一定要先通過 PDR。** 完成SPEC後登錄/SPEC_STEP/SPEC_Catalogue.md並執行REFLECT。

---



## 9. 一句話原則

**先對齊文件，再開始實作；有衝突就停，不可硬做。**
