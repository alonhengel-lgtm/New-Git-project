# Tic-Tac-Toe (איקס עיגול)

A two-player tic-tac-toe game that runs in the terminal. Prompts and messages are in Hebrew.

## Requirements

- Python 3.x

No extra packages are needed.

## How to run

From the project folder:

```bash
python Ttictactoc.py
```

On some systems you may need:

```bash
python3 Ttictactoc.py
```

## How to play

1. Player **X** starts.
2. On each turn, enter a row and a column as two numbers from `0` to `2`, separated by a space.

   Example: `1 2` places a mark in the middle row, right column.

3. The board is printed after every valid move.
4. The game ends when a player gets three in a row (row, column, or diagonal), or when the board is full (tie).

Invalid input, out-of-range coordinates, and occupied cells are rejected, and you are asked to try again.

## Board coordinates

```
(0,0) | (0,1) | (0,2)
---------------------
(1,0) | (1,1) | (1,2)
---------------------
(2,0) | (2,1) | (2,2)
```

## Project structure

- `Ttictactoc.py` — game logic and the main play loop (`TicTacToe` class)
