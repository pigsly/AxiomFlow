# Version Guide


這一頁只回答一個問題：

**你現在應該停在哪一版，不需要先讀到哪一版。**

如果你還不知道版本為什麼會升級，先讀 [Upgrade Signals](./upgrade-signals.md)。

## 四版對照

| 版本 | 主要解的痛點 | 你要理解的核心角色 | 典型流程 | 何時該升級 |
| --- | --- | --- | --- | --- |
| [簡單版](../en/README.simple.md) | 先不要在沒對齊文件時直接寫 code | `REQ` `SPEC` `ADR` `CONTRACT` | `REQ -> SPEC -> PDR -> WC` | 同類錯誤開始重複、規格一直補洞 |
| [普通版](../en/README.standard.md) | 把重複錯誤留下來，不再只靠人腦記 | `REQ` `SPEC` `ADR` `CONTRACT` `REFLECT` | `REQ -> SPEC -> PDR -> WC -> REFLECT` | 多個 `REFLECT` 開始指向同一種結構問題 |
| [進階版](../en/README.advanced.md) | 把重複事件升級成治理候選 | `REQ` `SPEC` `ADR` `CONTRACT` `REFLECT` `SUGGEST` | `REFLECT -> SUGGEST -> ADR / CONTRACT 提案` | 文件衝突已常阻斷開發，或需要正式批准 |
| [專業版](../en/README.professional.md) | 在治理衝突下仍能維持可控開發 | 全部角色 + 人類批准 / 阻斷機制 | `SUGGEST -> 批准 -> ADR / CONTRACT 更新` 或 `衝突 -> 阻斷停機` | 這已是最高層，不再往上升，改做治理重整 |

## 怎麼選

### 選簡單版

如果你現在卡在：

- 需求與實作還能講清楚
- 問題大多是局部修改
- 主要目標是先把 `PDR` 與基本護欄立起來

### 選普通版

如果你現在卡在：

- bug 不是第一次出現
- 規格常常補洞
- 你開始覺得有些事不能再靠聊天或人腦記住

### 選進階版

如果你現在卡在：

- 重複事件已經形成模式
- 不是 patch 一次就能解決
- 你開始需要判斷該升 `ADR` 還是升 `CONTRACT`

### 選專業版

如果你現在卡在：

- 文件衝突會直接卡住開發
- 一個需求常破壞另一個需求
- 你需要正式批准、阻斷、停機等待

## 一個快判斷法

- 還在問「怎麼做」：先停在簡單版
- 開始問「為什麼老是錯」：升普通版
- 開始問「這是不是該變成正式規則」：升進階版
- 開始問「不先重寫規則是不是根本不能做」：升專業版

## 閱讀建議

選定版本後，不要立刻回頭讀完整系統。

先這樣讀：

1. 對應版本 README
2. [Getting Started](./getting-started.md)
3. [Core Concepts](./concepts.md)

只有在需要時再往下讀：

- [Workflow](./workflow.md)
- [Feedback Loop](./feedback-loop.md)
- [Conflict Handling](./conflict-handling.md)
- [Governance.md](../en/Governance.md)
