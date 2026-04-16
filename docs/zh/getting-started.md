# Getting Started


這一頁回答的不是理論，而是你要怎麼把 AxiomFlow 落到一個新專案，或接到一個既有專案裡。

## Setup 第一件事：`AGENTS.md`

當你把 AxiomFlow 導入另一個 repo 時，在開始整理文件結構前，先建立或更新那個 repo 的 `AGENTS.md`。

用它要求 agent 先讀並遵守 `Governance.md`。

這不是補充提醒，而是 repo 層級的必要 setup。沒有這一條，治理文件就算存在，也不一定會真的約束 agent 的行為。

建議寫法：

```md
在分析、設計、產碼或文件更新前，先閱讀並遵守 `docs/zh/Governance.md`。
如果任務與治理文件衝突，不要自行假設或繞過，應先停止並請求人類釐清。
```

如果這條沒有先寫進目標 repo 的 `AGENTS.md`，後面的 `REQ`、`SPEC_STEP`、`ADR`、`CONTRACT` 很容易只剩文件存在，卻沒有真正綁到執行入口。

## 你需要什麼

你需要的，是六個文件角色：

- `REQ`
- `SPEC_STEP`
- `ADR`
- `CONTRACT`
- `REFLECT`
- `SUGGEST`

你不需要第一天就把整套流程鋪滿。

你只需要先有足夠的結構，能把失控執行擋下來。

## 最小起步組

先從這幾份文件開始：

- `REQ-001.md`
- `SPEC_STEP/SPEC-001.md`
- `SPEC_STEP/SPEC_Catalogue.md`
- `ADR.md`
- `CONTRACT.md`

這五份文件，已經足夠先立住：

- 目標問題
- 實作路徑
- 當前架構方向
- 硬邊界
- 已完成規格索引

如果你的專案需要模組級架構圖，保留一份主 `ADR.md`，再把輔助 ADR 放進像 `docs/adr/` 這樣的資料夾。

## PDR 規則

在以下動作之前，都先跑 `PDR`：

- 分析
- 設計
- 產碼
- 文件更新

這套系統帶來的第一個收益，不是文件變多。

第一個收益，是把那些本來就不該繼續的工作先停下來。

## 依導入順序怎麼下指令

### 0. 先建立或更新 `AGENTS.md`

指令:

```text
先讀 docs/zh/getting-started.md。
先處理 AGENTS.md。
如果 repo 還沒有 AGENTS.md，就建立一份最小可用版本。
如果已經有，就只補 AxiomFlow 必要條款，不要覆蓋既有專案規則。
明確要求 agent 在分析、設計、產碼或文件更新前，先閱讀並遵守 docs/zh/Governance.md。
如果任務與治理文件衝突，必須停止並請求人類釐清。
完成後再回報我下一步適合進入 REQ 還是還缺什麼基礎設定。
```

說明:

先把治理綁進 agent 入口，再開始後面的文件工作。

### 1. 先寫一份小型 `REQ`

指令:

```text

幫我先起草一份小型 REQ，主題是 ________。
輸出成 REQ 文件格式。
如果你發現需求描述還不完整，先列出缺口，不要自己補假設。
```

說明:

先把需求真相寫清楚，不要讓 `REQ` 混進實作做法。

### 2. 從中拆出一份可執行的 `SPEC`

指令:

```text
SPEC REQ-???
```

說明:

把 `REQ` 拆成可執行的工作規格，但不要發明 `REQ` 沒授權的新需求。
如果 `REQ` 不足以支持這份 `SPEC`，就先停下來指出缺口。

### 3. 把 `SPEC` 細化到可直接執行

指令:

```text
Split SPEC-??? for step by step
```

說明:

補齊步驟順序、輸入輸出、必要檢查點與交付結果。
不要擴大範圍，也不要偷渡新的架構決策。
如果細化過程已經碰到 `ADR` 或 `CONTRACT` 層級，就先停。

### 4. 從第一份需求中萃取初始的 `ADR` 與 `CONTRACT`

指令:

```text
EXTRACT ADR CONTRACT REQ-???
```

說明:

`ADR` 只寫架構方向與理由。
`CONTRACT` 只寫不能被跨越的責任、資料或控制邊界。
不要把實作步驟寫進 `ADR`，也不要把暫時習慣寫成 `CONTRACT`。

### 5. 在實作前要求先做 `PDR`

指令:

```text
PDR 
```

說明:

檢查 `SPEC` 是否對齊 `REQ`、`ADR`、`CONTRACT`。
如果文件衝突、資訊不足、邊界不清或有違反 `CONTRACT` 風險，就停下來列出問題與影響。

### 6. 只有在 `PDR` 通過後，才開始進入 `WC`，並完成 `SPEC` 工作

指令:

```text
WC SPEC-???
```

說明:

只有在 `PDR` 通過後，才根據已批准的 `SPEC` 進入 `WC`。
實作時只改這份 `SPEC` 授權的範圍。
如果發現文件與現況不一致，立刻停止並回報，不要自行繞過。

### 7. 執行後，把值得留下的經驗記進 `REFLECT`

指令:

```text
REFLECT SPEC-???
```

說明:

只記錄有意義的 bug、教訓、重複失誤模式或被證明失敗的假設。
如果沒有足夠價值，直接告訴我這次不需要寫 `REFLECT`。

### 8. 當模式重複出現，再建立 `SUGGEST`

指令:

```text
SUGGEST 
```

說明:

先判斷相關 `REFLECT` 是否已形成重複模式。
如果值得，起草一份 `SUGGEST`，說明模式、風險與建議升級方向。
不要直接修改 `ADR` 或 `CONTRACT`。

### 9. 只有在人類批准後，才透過 `GU` 升級治理

指令:

```text
GU SUG-????????????
```

說明:

只有在人類批准後，才更新正式治理內容。
只修改已批准的治理範圍，並標記相關提案或證據狀態。
如果批准內容與現行治理衝突，就先停下來列出衝突。



## 建議目錄

```text
docs/
  REQ/
    REQ-001.md
  SPEC_STEP/
    SPEC-001.md
    SPEC_Catalogue.md
  ADR.md
  adr/
    module-a-flow.md
    system-interaction.md
  CONTRACT.md
  REFLECT/
    REFLECT-001.md
  SUGGEST/
    SUG-YYYYMMDDHHMI.md
```

資料夾名稱可以依 repo 調整，但文件角色與治理規則不要跟著漂移。

建議的 ADR 慣例：

- `ADR.md` 是唯一正式的主 ADR 來源
- `docs/adr/` 用來存放模組流程圖、元件圖等輔助 ADR
- 輔助 ADR 只有在被 `ADR.md` 引用時才生效

## 你什麼時候算用對了

當你看到以下狀態時，代表這套系統開始用對了：

- 對齊還沒檢查完，實作不會先開始
- 出現衝突時，執行會停下來，而不是硬繞過去
- 架構方向是明確的
- 邊界是明確的
- 重複錯誤會產生治理提案
- 正式規則只會經過人類批准後才改變

## 下一步

- [Core Concepts](./concepts.md)
- [Workflow](./workflow.md)
- [Conflict Handling](./conflict-handling.md)
- [Examples](./examples/README.md)
