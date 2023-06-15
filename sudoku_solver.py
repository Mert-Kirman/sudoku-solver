print("Welcome to Sudoku Solver!")
start_count = int(input("How many numbers do we know ?\n"))
sudoku_board = [[[0] for i in range(9)] for j in range(9)]


# Function for printing the sudoku board
def img_printer(matrix):
    for r in range(len(matrix)):
        print(9 - r, end="\t")
        for c in range(len(matrix[0])):
            print(matrix[r][c][0], end="\t")
        print("\n")
    extra_line = [("\t" + chr(ord("a") + i)) for i in range(9)]
    print(" " + "".join(extra_line))
    print("\n")


# Place a desired number on the sudoku board
def matrix_filler(matrix, r, c, n):
    matrix[-1 * r][ord(c) - ord("a")][0] = n


# Place the numbers that are known at the beginning to the sudoku board
# These numbers are certainly correct, thus they are added to the sudoku matrix as strings
img_printer(sudoku_board)
for i in range(start_count):
    start_number = input("Which number ?\n")
    start_location = input("Which column and row do you want to place it ?\n")
    column, row = start_location.split()
    row = int(row)
    matrix_filler(sudoku_board, row, column, start_number)
    img_printer(sudoku_board)


# Check if numbers on the board are in accordance with sudoku puzzle rules
def check(matrix):
    # There should not be any duplicate number in a column
    for r in matrix:
        num_lst = []
        for c in r:
            if int(c[0]) == 0:
                continue
            elif int(c[0]) not in num_lst:
                num_lst.append(int(c[0]))
            else:
                return False

    # There should not be any duplicate number in a row
    for c in range(len(matrix[0])):
        num_lst = []
        for r in range(len(matrix)):
            if int(matrix[r][c][0]) == 0:
                continue
            elif int(matrix[r][c][0]) not in num_lst:
                num_lst.append(int(matrix[r][c][0]))
            else:
                return False

    # There should not be any duplicate number in a box
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            num_lst = []
            for r in range(i, 3 + i):
                for c in range(j, 3 + j):
                    if int(matrix[r][c][0]) == 0:
                        continue
                    elif int(matrix[r][c][0]) not in num_lst:
                        num_lst.append(int(matrix[r][c][0]))
                    else:
                        return False
    return True


# No zeros left in the sudoku board
def full(matrix):
    for i in matrix:
        for j in i:
            if j[0] == 0:
                return False
    return True


# Recursive function that tries possible numbers for each cell on the board and tries to find a solution
def rec_solver(matrix, row, column, n=1):
    if not (row < 0 or column < 0 or row > 8 or column > 8):
        if matrix[row][column][0] != 0 and type(matrix[row][column][0]) is not str:
            return "blocked"  # A number is already placed here, it cannot be changed
    if not check(matrix):
        if n == 9:
            return "stop"  # A number previously placed is wrong
        else:
            return
    if full(matrix):  # Solution found
        return matrix
    if row < 0 or column < 0 or row > 8 or column > 8:
        return "blocked"  # Cannot move in this direction as it is out of the board borders

    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # For moving left, down, right, up on the sudoku board
    for d in directions:
        for i in range(1, 10):
            change = False  # A variable denoting a string value inside a cell in the board is converted to an integer, used for backtracking
            if type(matrix[row][column][0]) is not str:
                matrix[row][column][0] = i
            else:
                change = True

            if change:
                matrix[row][column][0] = int(matrix[row][column][0])

            a = rec_solver(matrix, row + d[0], column + d[1], i)

            if a == "stop":
                if change:
                    matrix[row][column][0] = str(matrix[row][column][0])
                    return "stop"
                else:
                    matrix[row][column][0] = 0
                    return
            if a == "blocked":
                if change:
                    matrix[row][column][0] = str(matrix[row][column][0])
                break
            if a is not None:
                return a

            if change:
                matrix[row][column][0] = str(matrix[row][column][0])
                return  # A certainly correct number cannot be changed
            else:  # Try placing a different number
                matrix[row][column][0] = 0
                if i == 9:  # If all numbers for the current cell have been tried, go to a previous recursion layer
                    return


impossible = True
break_completely = False
for r in range(len(sudoku_board)):
    for c in range(len(sudoku_board[0])):
        if sudoku_board[r][c][0] == 0 or type(sudoku_board[r][c][0]) is str:
            b = rec_solver(sudoku_board, r, c)
            if b is not None:
                img_printer(b)
                print("SOLUTION FOUND !")
                impossible = False
            break_completely = True
            break
    if break_completely:
        break

if impossible:
    print("No solution possible !")
