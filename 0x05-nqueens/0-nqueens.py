#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    # Check if no queen attacks this cell in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if no queen attacks this cell in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if no queen attacks this cell in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)