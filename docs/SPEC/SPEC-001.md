---
id: SPEC-001
title: Implement the Core Flow of a Single-Player Poker Three-Round Score Challenge
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

Deliver the minimum playable version of the single-player poker three-round score challenge so that the player can:

- start the game with one 52-card deck
- draw 5 cards per round
- have 1 card-exchange opportunity per round
- play a total of 3 rounds
- receive a score based on the final hand rank
- determine whether the run passes based on the total score across 3 rounds

## 2. Steps

1. Build the data structure for a 52-card deck, including shuffle and draw flow.
2. Implement the single-round flow:
   - deal 5 cards to the player's hand
   - allow the player to choose one card to replace
   - draw a replacement card and form the final 5-card hand
3. Implement hand-rank detection for the ranks defined in this requirement:
   - Straight Flush
   - Four of a Kind
   - Full House
   - Flush
   - Straight
   - Three of a Kind
   - Two Pairs
4. Define the score table for each hand rank and convert each round result into a round score.
5. Implement the main three-round flow:
   - run 3 consecutive rounds
   - accumulate the score from each round
   - output each round result and the total score
6. Implement pass/fail judgment:
   - total score `>= 7` is a success
   - total score `0 - 6` is a failure
7. Add basic input handling:
   - duplicate replacement indexes
   - replacement indexes outside the valid range
   - correct settlement when the player chooses not to replace any card

## 3. Verification

- [ ] Unit test: the 52-card deck contains no duplicates, and deck size changes correctly after draws.
- [ ] Unit test: each specified hand rank is identified correctly.
- [ ] Unit test: return success when the 3-round total score is `>= 7`.
- [ ] Unit test: return failure when the 3-round total score is `0 - 6`.
- [ ] Integration test: the player can complete the 3-round flow and may replace cards only once per round.
