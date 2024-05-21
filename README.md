Program Description:
====================
Knight's Tour
====================
Description: Knight's Tour is an algorithmic problem in which a knight (a chess piece) must visit every square on a chessboard exactly once. This project implements a solution to the problem using Warnsdorf's rule, which prefers moves to squares with the fewest subsequent moves. The program also includes a visualization of the process, showing the knight's path on the chessboard.
====================
Functions:

isValidMove(x, y, board): Checks if the move is valid within the chessboard and hasn't been visited yet.
getDegree(x, y, board): Returns the number of valid moves from the current position.
solveKnightsTour(x, y, moveI, path, deadEnds): Recursively solves the Knight's Tour problem using Warnsdorf's rule.
visualizeBoard(board, path, knightPosition): Visualizes the chessboard, the knight's path, and the counters.
main(): The main function that runs the program, sets up the chessboard, and initializes the knight's starting positions.
You will be prompted to enter the number of rows and columns for the chessboard. The knight will then attempt to complete the tour, starting from various positions.
===============================
Usage Examples:
===============================
After running the program, enter the number of rows and columns for the chessboard (e.g., 8x8).
Watch the visualization of the process on the chessboard.
Terminate the program by pressing the space bar if you want to interrupt the execution.
Notes:
===============================
The program can be interrupted by the user by pressing the space bar.
The visualization updates in real-time to provide a better overview of the solution process.
