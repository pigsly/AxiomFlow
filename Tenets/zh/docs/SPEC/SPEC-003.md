---
id: SPEC-003
title: 增加 Joker 並允許替代任何牌
related_req: REQ-001
related_adr: ADR
related_contract: CONTRACT
code_implement: blocked
target_files:
  - game.py
  - scoring.py
  - tests/test_game.py
---

## 1. Goal

在牌組中增加 `Joker`，並允許 `Joker` 在牌型判定時替代任何牌使用。

## 2. Steps

1. 擴充牌組資料結構，在原本牌組中加入 `Joker`。
2. 更新發牌與抽牌流程，使 `Joker` 可被正常洗牌、抽出與換牌。
3. 更新牌型判定邏輯，使 `Joker` 可以替代任意點數與花色，協助形成最佳牌型。
4. 確認計分流程會依 `Joker` 替代後的最終牌型計分。
5. 補上對應測試，涵蓋 `Joker` 參與的牌型判定與計分。

## 3. Verification

- [ ] 單元測試：牌組中包含 `Joker`，且可正常參與洗牌與抽牌。
- [ ] 單元測試：`Joker` 可替代任意牌形成有效牌型。
- [ ] 單元測試：含 `Joker` 的手牌會以最佳可形成牌型正確計分。
- [ ] 整合測試：玩家在三局流程中可正常抽到、保留或換掉 `Joker`。

## 4. Governance Note

此規格目前與既有治理文件衝突，因此先標記為 `blocked`：

- `REQ-001` 目前定義為一副 `52` 張牌
- `CONTRACT` 目前禁止加入其他牌

在 `REQ` / `CONTRACT` 更新或人類明確裁示前，不應進入實作。
