# Knight's Tour

Knight's Tour is an algorithmic problem in which a knight (a chess piece) must visit every square on a chessboard exactly once. This project implements a solution to the problem using Warnsdorf's rule, which prefers moves to squares with the fewest subsequent moves. The program also includes a visualization of the process, showing the knight's path on the chessboard.

## Description

**Knight's Tour** is an algorithmic problem where a knight must visit every square on a chessboard exactly once. This project uses Warnsdorf's rule to solve the problem, preferring moves to squares with the fewest subsequent moves. The program also includes a visualization of the knight's path.

## Functions

- `isValidMove(x, y, board)`: Checks if the move is valid within the chessboard and hasn't been visited yet.
- `getDegree(x, y, board)`: Returns the number of valid moves from the current position.
- `solveKnightsTour(x, y, moveI, path, deadEnds)`: Recursively solves the Knight's Tour problem using Warnsdorf's rule.
- `visualizeBoard(board, path, knightPosition)`: Visualizes the chessboard, the knight's path, and the counters.
- `main()`: The main function that runs the program, sets up the chessboard, and initializes the knight's starting positions.

## Installation

To install the necessary dependencies for Knight's Tour, run the following command:

```bash
pip install -r requirements.txt
