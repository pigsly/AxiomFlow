# Governance Rules


## 1. 適用範圍

這些規則適用於 repository 中使用的治理文件類型：

- `REQ`：需求文件
- `SPEC_STEP`：實作步驟文件
- `ADR`：架構決策記錄
- `CONTRACT`：邊界與介面契約
- `REFLECT`：經驗、事件與教訓記錄
- `SUGGEST`：治理升級提案

補充規則：

- `REQ` 與 `SPEC_STEP` 是 agent 執行時的主要輸入。
- `SPEC_STEP` 可以使用 `code_implement` 追蹤實作狀態。
- `ADR` 與 `CONTRACT` 在同一時間都只允許一份正式主文件。

## 2. 文件角色

### `REQ`

定義需求、目標、範圍與預期結果。

### `SPEC_STEP`

定義具體的實作步驟與執行細節。

使用一份 `SPEC_Catalogue.md` 搭配多份 `SPEC-XXX.md`。

### `ADR`

定義當前 milestone 的方向、架構選擇與關鍵決策。

它用來處理方向問題與共享結構決策，而不是每個局部實作細節。

可以有輔助 ADR 檔案，例如流程圖、互動圖或模組展開，但只有在主 `ADR` 引用時才生效。

### `CONTRACT`

定義跨 milestone 仍然有效的硬邊界，尤其是：

- 責任邊界
- 資料邊界
- 控制邊界

### `REFLECT`

儲存經過人類檢視的經驗，包括錯誤、事件、觀察與執行經驗。

`REFLECT` 預設應與 `SPEC_STEP` 對齊，不應直接改寫 `REQ`。

### `SUGGEST`

從多份 `REFLECT` 中抽象出重複模式，並判斷是否應升級成 `ADR` 或 `CONTRACT` 提案。

`SUGGEST` 只產生提案，本身不會直接生效。

## 3. Trust Order

當文件衝突時，預設 trust order 如下：

```text
CONTRACT > ADR > REQ > SPEC_STEP
SPEC_STEP > REFLECT > SUGGEST
```

解讀：

- `CONTRACT` 是最高優先級的硬約束
- `ADR` 定義當前方向
- `REQ` 定義需求範圍
- `SPEC_STEP` 定義執行路徑
- `REFLECT` 是證據來源
- `SUGGEST` 是提案來源

### 治理生效規則

- `REFLECT` 是證據，不是正式治理
- `SUGGEST` 是提案，不是正式治理
- `GU` 是治理升級動作，不是文件
- 只有人類批准後，`SUGGEST` 內容才能進入正式 `ADR` 或 `CONTRACT`

## 4. 單一真相來源

### `ADR`

- 只允許一份正式主 `ADR`
- 可以有輔助 ADR 檔案，用來放圖表或局部展開
- 輔助 ADR 只有在主 `ADR` 引用時才生效
- 輔助 ADR 可以擴充主 `ADR`，但不能形成平行方向
- 如果輔助 ADR 與主 `ADR` 衝突，以主 `ADR` 為準
- 當 milestone 方向改變時，更新既有主 `ADR`，不要建立平行主版本

### `CONTRACT`

- `CONTRACT` 定義跨主要模組的硬邊界
- 不要為每個 milestone 建立新的正式版本，除非人類明確重設邊界
- 如果要改變邊界，必須透過 `GU` 或人類直接操作更新 `CONTRACT`

## 5. `PDR`：Pre-Development Review

以下動作前都必須執行 `PDR`：

- 分析
- 設計
- 產碼
- 文件更新

`PDR` 同時是前置審查與治理分流點。它用來判斷這個問題應停留在 `REQ` 或 `SPEC_STEP` 層級，還是要升級到 `REFLECT`、`SUGGEST`、`ADR` 或 `CONTRACT`。

### Requirement 與 Spec 檢查

- 檢查 `SPEC_STEP` 是否違反 `REQ`
- 檢查 `REQ` 與 `SPEC_STEP` 是否有缺口或漂移
- 在 `SPEC_STEP/` 下，`SPEC-XXX.md` 是實作規格，`SPEC_Catalogue.md` 是已完成規格索引
- 只有 `code_implement: done` 的 `SPEC-XXX.md` 才能進入 `SPEC_Catalogue.md`
- `code_implement` 合法狀態是 `todo`、`dev`、`done`、`blocked`
- `SUG-YYYYMMDDHHMI.md` 必須列出來源 `REFLECT-XXX.md`
- 完成 `GU` 後，要把對應的 `SUG-YYYYMMDDHHMI.md` 與關聯 `REFLECT-XXX.md` 標記為已批准

### 架構與邊界檢查

- 檢查實作方向是否符合 `ADR`
- 如果引用了輔助 ADR，檢查它們是否仍與主 `ADR` 對齊
- 檢查工作是否違反 `CONTRACT`
- 檢查 `ADR`、`CONTRACT` 與 `SPEC_STEP` 是否互相衝突，或留下不清楚的邊界

## 6. 衝突處理規則

如果在 `PDR` 或執行過程中發現以下情況：

- 文件彼此衝突
- 邏輯背離
- 資訊缺漏
- 文件過期
- 產出可能違反治理文件

必須採取以下流程：

### 1. 阻斷

立即停止當前實作、修改或產出。

- 若衝突出現在 `SPEC-XXX.md`，將其 `code_implement` 設為 `blocked`
- 若衝突出現在 `REQ`、`ADR`、`CONTRACT` 或其他沒有 `code_implement` 的治理文件，不得強行補欄位；改以警告記錄衝突並停機等待
- 警告記錄顯示在 CLI 介面即可

### 2. 警告

清楚列出：

- 衝突來源文件
- 具體矛盾點
- 可能影響範圍

### 3. 停機等待

把決策權交還給人類。

在未獲得明確裁示或文件未更新前：

- 不得自行腦補
- 不得繞過規則
- 不得強行實作

這類情況預設視為 Level 4，不再用局部補丁方式繼續推進。

若 `SPEC-XXX.md` 已標記為 `blocked`，只有在衝突文件已更新或人類已明確裁示後，才能解除 `blocked`。如有需要，由人類改成其他狀態。

## 7. 實作限制

- 不得產出違反 `CONTRACT`、`ADR` 的內容
- 不得在 `REQ`、`ADR`、`SPEC_STEP` 未覆蓋的情況下，自行擴張範圍
- 當細節未被 `REQ` 或 `SPEC_STEP` 覆蓋時，預設依循相關 `ADR`
- 若 `ADR` 與 `CONTRACT` 已明確限制方向，不得用使用者臨時語句直接覆蓋

## 8. 重要維運命令

- `PDR`
- `REFLECT`：反映當前事件、bug、spec，並將經驗輸出為 `REFLECT-XXX.md`；如果 spec、事件或 bug 不重要，可以不輸出經驗
- `GG (SUGGEST)`：評估目前的 `REFLECT` 集合，對重複模式做抽象，建議應升入 `CONTRACT` 或 `ADR`，輸出 `SUG-YYYYMMDDHHMI.md`
- `GU (GOVERNANCE_UPGRADE)`：僅在人類批准後，依 `SUGGEST` 提案更新正式 `ADR` 或 `CONTRACT`；未經批准不得生效
- `WC (write code)`：依 `SPEC-XXX.md` 規格開始撰寫 code；**執行前一定要先通過 `PDR`。** 完成後登錄 `SPEC_Catalogue.md` 並執行 `REFLECT`

## 9. 一句話原則

**先對齊文件，再開始實作；有衝突就停，不可硬做。**
