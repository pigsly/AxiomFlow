---
id: SPEC-002
title: 調整 Full House 分數提高 1 分
related_req: REQ-001
related_adr: ADR
related_contract: CONTRACT
code_implement: todo
target_files:
  - scoring.py
  - tests/test_game.py
---

## 1. Goal

將 Full House 的得分從 `5` 分調整為 `6` 分，並同步更新相關測試，其他牌型分數不變。

## 2. Steps

1. 更新牌型分數表，將 `Full House` 的分數由 `5` 改為 `6`。
2. 確認其他牌型分數維持原定義，不引入額外規則變更。
3. 更新對應測試，驗證 `Full House` 會得到新分數。
4. 確認總分與過關判定流程仍使用更新後的局分計算。

## 3. Verification

- [ ] 單元測試：`Full House` 可正確對應為 `6` 分。
- [ ] 單元測試：其他既有牌型分數不受影響。
- [ ] 單元測試：三局總分計算會套用更新後的 `Full House` 分數。
