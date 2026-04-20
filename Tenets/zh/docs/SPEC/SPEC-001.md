---
id: SPEC-001
title: 單人 poker 三局搶分遊戲核心流程實作
related_req: REQ-001
related_adr: ADR
related_contract: CONTRACT
code_implement: todo
target_files:
  - game.py
  - scoring.py
  - tests/test_game.py
---

## 1. Goal

完成單人 poker 三局搶分遊戲的最小可玩版本，讓玩家可以：

- 使用一副 52 張牌開始遊戲
- 每局抽 5 張牌
- 每局有 1 次換牌機會
- 共進行 3 局
- 依牌型取得分數
- 依 3 局總分判定是否達到過關門檻

## 2. Steps

1. 建立 52 張牌的資料結構與洗牌、抽牌流程。
2. 實作單局流程：
   - 發 5 張手牌
   - 允許玩家選擇要換掉的牌(一張)
   - 補牌後形成最終 5 張手牌
3. 實作本需求中的有效牌型判定：
   - Straight Flush
   - Four of a Kind
   - Full House
   - Flush
   - Straight
   - Three of a Kind
   - Two Pairs
4. 定義牌型對應分數表，並讓單局結果可換算為局分。
5. 實作三局主流程：
   - 連續進行 3 局
   - 累計每局得分
   - 輸出每局結果與總分
6. 實作過關判定：
   - 總分 `>= 7` 視為成功
   - 總分 `0 - 6` 視為失敗
7. 補上基本輸入處理：
   - 換牌輸入重複索引
   - 換牌索引超出範圍
   - 不換牌時仍可正常結算

## 3. Verification

- [ ] 單元測試：52 張牌不重複、抽牌後牌數正確。
- [ ] 單元測試：各指定牌型可被正確辨識。
- [ ] 單元測試：三局總分 `>= 7` 時回傳成功。
- [ ] 單元測試：三局總分 `0 - 6` 時回傳失敗。
- [ ] 整合測試：玩家完成三局流程且每局只可換牌一次。
