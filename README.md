# Sudoku Puzzle Solver

Python program that recursively finds missing numbers on the sudoku board and prints the solution.

## How It Works

Program starts by creating a matrix full of zeros representing an empty sudoku puzzle board. The player enters the

amount of numbers that are known at the beginning of the puzzle and enters each number with its corresponding

coordinates in the console. After this recursive function is called. It moves along cells trying all the possible number

combinations and while doing so checks if the current board conforms with the rules of the sudoku puzzle. String values

in the sudoku matrix represent numbers given at the beginning of the program by the user and are not modified

throughout the recursion. This enables the recursive function to check every single cell of the sudoku board. At the

end of the program either a solution is found and shown to the user in the console or a message is shown saying no

solution is possible.

### Prerequisites

An IDE or text editor to run the python code.

## Running the tests

At the beginning of the program the player is asked how many numbers are known, what these numbers and their locations

are. Numbers and their coordinates should be entered in two separate lines. Coordinates should be in the following

format:

- a 4

- h 8

and so on.

As data is entered sudoku board will be visualized to help you keep track of the board you are creating.

"Extreme difficulty" sudoku puzzles may take up to 1.5 minutes to solve.
