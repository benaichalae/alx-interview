#!/usr/bin/python3
"""
N queens solution finder module.
"""
import sys


def print_solution(solution):
    """Prints a solution in the required format.

    Args:
        solution (list of int): The list of column
        positions of queens in each row.
    """
    print([[i, solution[i]] for i in range(len(solution))])


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col].

    Args:
        board (list of int): The current state of the board.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens(n, row, board, solutions):
    """Recursively solves the N queens problem.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row being processed.
        board (list of int): The current state of the board.
        solutions (list of list of int): The list of all valid solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1


def main():
    """Main function to retrieve input and find solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_n_queens(n, 0, board, solutions)

    for solution in solutions:
        print_solution(solution)


if __name__ == "__main__":
    main()
