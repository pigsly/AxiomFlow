---
id: SPEC-003
title: Add a Joker and Allow It to Substitute for Any Card
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

Add a `Joker` to the deck and allow the `Joker` to substitute for any card during hand-rank evaluation.

## 2. Steps

1. Extend the deck data structure and add a `Joker` to the existing deck.
2. Update dealing and draw flow so the `Joker` can be shuffled, drawn, and replaced correctly.
3. Update hand-rank evaluation so the `Joker` can substitute for any rank and suit to form the best valid hand.
4. Confirm that scoring uses the final hand rank after `Joker` substitution.
5. Add related tests covering hand-rank evaluation and scoring when a `Joker` is involved.

## 3. Verification

- [ ] Unit test: the deck includes a `Joker`, and it participates correctly in shuffle and draw flow.
- [ ] Unit test: the `Joker` can substitute for any card to form a valid hand rank.
- [ ] Unit test: a hand containing a `Joker` is scored according to the best possible hand rank.
- [ ] Integration test: the player can draw, keep, or replace the `Joker` correctly during the 3-round flow.

## 4. Governance Note

This spec currently conflicts with the existing governance documents, so it remains marked as `blocked`:

- `REQ-001` currently defines a `52`-card deck
- `CONTRACT` currently forbids adding any other cards

Implementation must not begin until `REQ` / `CONTRACT` is updated or a human explicitly decides otherwise.
