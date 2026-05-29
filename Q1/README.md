   # Assignment 5 - Task 1 - Game Search Algorithms

## Objective

The objective of this assignment is to implement and test the following game search algorithms:

* Minimax Search
* Alpha-Beta Search
* Heuristic Alpha-Beta Search
* Monte-Carlo Tree Search (MCTS)

The implementation is done using the Tic-Tac-Toe game.

---

# Game Used: Tic-Tac-Toe

Tic-Tac-Toe is a two-player zero-sum game.

* Player X → Maximizing player
* Player O → Minimizing player

### Utility Values

| Result | Value |
| ------ | ----- |
| X Wins | +1    |
| O Wins | -1    |
| Draw   | 0     |

---

# Algorithms Implemented

## 1. Minimax Search

Minimax explores all possible moves and selects the best move assuming both players play optimally.

## 2. Alpha-Beta Search

Alpha-Beta pruning improves Minimax by skipping unnecessary branches that do not affect the final decision.

## 3. Heuristic Alpha-Beta Search

This uses depth-limited Alpha-Beta search. When the depth limit is reached, a heuristic evaluation function estimates the board score.

## 4. Monte-Carlo Tree Search (MCTS)

MCTS uses random simulations to estimate the best move. Since MCTS uses randomness, its output may vary slightly between runs.

---


# Test Cases

## Test Case 1

### Board

```text
X | X |  
O | O |  
  |   |
```

### Player to Move

```text
X
```

### Expected

X should place at position 2 and win.

### Output

```text
Minimax Move: 2 Value: 1
Alpha-Beta Move: 2 Value: 1
Heuristic Alpha-Beta Move: 2 Heuristic Value: 100
MCTS Move: 2
```

---

## Test Case 2

### Board

```text
X | O | X
  | O |  
  |   |
```

### Player to Move

```text
X
```

### Output

```text
Minimax Move: 7 Value: 0
Alpha-Beta Move: 7 Value: 0
Heuristic Alpha-Beta Move: 7 Heuristic Value: 10
MCTS Move: may vary
```

### Note

MCTS output can change because it uses random simulations.

---

## Test Case 3

### Board

```text
X | O | X
O | X |  
  |   | O
```

### Player to Move

```text
X
```

### Expected

X should place at position 6 and win.

### Output

```text
Minimax Move: 6 Value: 1
Alpha-Beta Move: 6 Value: 1
Heuristic Alpha-Beta Move: 6 Heuristic Value: 100
MCTS Move: 6
```

---

## Test Case 4

### Board

```text
O | O |  
X | X |  
  |   |
```

### Player to Move

```text
O
```

### Expected

O should place at position 2 and win.

### Output

```text
Minimax Move: 2 Value: -1
Alpha-Beta Move: 2 Value: -1
Heuristic Alpha-Beta Move: 2 Heuristic Value: -100
MCTS Move: 2
```

---

# Observation

* Minimax and Alpha-Beta produce the same optimal moves.
* Alpha-Beta reduces unnecessary search using pruning.
* Heuristic Alpha-Beta works using evaluation scores and limited depth.
* MCTS may produce different outputs in different runs because of randomness.

---

# Conclusion

All four required algorithms were implemented successfully using Tic-Tac-Toe.

The test cases show that the algorithms are working correctly and producing valid game decisions.
