---
id: SPEC-002
title: Increase the Full House Score by 1 Point
related_req: REQ-001
related_adr: ADR
related_contract: CONTRACT
code_implement: todo
target_files:
  - scoring.py
  - tests/test_game.py
---

## 1. Goal

Change the Full House score from `5` points to `6` points and update the related tests. All other hand-rank scores remain unchanged.

## 2. Steps

1. Update the hand-rank score table and change `Full House` from `5` to `6`.
2. Confirm that all other hand-rank scores stay unchanged and that no other rule change is introduced.
3. Update the related tests to verify that `Full House` now returns the new score.
4. Confirm that total-score calculation and pass/fail judgment use the updated round score.

## 3. Verification

- [ ] Unit test: `Full House` maps correctly to `6` points.
- [ ] Unit test: existing scores for all other hand ranks remain unaffected.
- [ ] Unit test: the 3-round total-score calculation applies the updated `Full House` score.
