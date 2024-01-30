#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given position (row, col).
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, n, solutions):
    """
    Utility function to solve N-Queens problem using backtracking.
    """
    if row == n:
        # All queens are placed successfully
        solution = [
            [i, j] for i in range(n) for j in range(n) if board[i][j] == 1
        ]
        solutions.append(solution)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack


def print_solutions(n):
    """
    Print all possible solutions for the N-Queens problem.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number and at least 4")
        sys.exit(1)

    print_solutions(n)
