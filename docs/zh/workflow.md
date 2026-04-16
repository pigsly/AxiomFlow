# Workflow


AxiomFlow 的核心，是一個受治理約束的執行循環。

這個循環只做三件事：執行前先驗證對齊，執行後留下經驗，治理升級必須經過批准。

## 1. `PDR`

`PDR` 是 Pre-Development Review。

它必須發生在以下動作之前：

- 分析
- 設計
- 產碼
- 文件更新

`PDR` 要檢查的是：

- `SPEC` 是否偏離 `REQ`
- 實作方向是否符合 `ADR`
- 任何規則是否踩到 `CONTRACT`
- 文件之間是否出現衝突、漂移或關鍵缺口

只要 `PDR` 沒過，執行就不能往下走。

## 2. `WC`

`WC` 是 Write Code。

只有在 `PDR` 通過後，才允許進入 `WC`。`WC` 依照 `SPEC-XXX.md` 執行實作。

如果對應 `SPEC` 有 `code_implement` 欄位，它的狀態應反映實作進度，例如：

- `todo`
- `dev`
- `done`
- `blocked`

## 3. `REFLECT`

在有意義的工作、錯誤、事件或發現之後，把經驗記進 `REFLECT`。

例如：

- 值得記住的 bug 模式
- 重複出現的執行失誤
- 被證明失敗的設計假設
- 導致返工的 `SPEC` 誤解

不是每件事都要記。只有有意義的事件，才值得變成長期經驗。

## 4. `GG`

`GG` 會產出 `SUGGEST`。

它的目的，是檢查 `REFLECT` 中反覆出現的模式，判斷這些教訓是否該升級成正式治理：

- `ADR`
- `CONTRACT`

但 `SUGGEST` 仍然不是正式治理，它只是提案。

## 5. `GU`

`GU` 是 Governance Upgrade。

這一步只能在人類批准後發生。

一旦批准，`GU` 就更新正式 `ADR` 或 `CONTRACT`，並依治理規則標記相關提案與證據的狀態。

## 完整循環

```text
REQ -> SPEC -> PDR -> WC -> REFLECT -> GG -> GU
```

這會形成一個系統：當前真相約束當前實作，而新的經驗可以改善未來真相，但不能繞過批准。

## 這個流程真正不一樣的地方

大多數開發流程優化的是 throughput。

這個流程優化的是可控的 throughput。

當 Agent 的速度已經快到能把錯誤一起放大時，這個差別就很重要。
