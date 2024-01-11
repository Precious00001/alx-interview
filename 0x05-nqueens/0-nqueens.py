#!/usr/bin/python3
"""
   Description: The N queens puzzle is the challenge of placing N non-attacking
                queens on an N×N chessboard. Write a program that solves the N
                queens problem.
   Usage: nqueens N
"""

import sys


def print_board(board):
    """Prints the positions of queens on the chessboard.

    Args:
        board (list): A list of lists representing the chessboard.
    """
    queen_positions = []
    for a, row in enumerate(board):
        for b, col in enumerate(row):
            if col == 1:
                queen_positions.append([a, b])
    print(queen_positions)


def isSafe(board, row, col, number):
    """Checks if placing a queen at a specific position is safe.

    Args:
        board (list): A list of lists representing the chessboard.
        row (int): Row index to check for safety.
        col (int): Column index to check for safety.
        number (int): Size of the chessboard.

    Returns:
        bool: True if placing a queen is safe, False otherwise.
    """
    # Check this row in the left side
    for a in range(col):
        if board[row][a] == 1:
            return False

    # Check upper diagonal on the left side
    for a, b in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[a][b] == 1:
            return False

    # Check lower diagonal on the left side
    for a, b in zip(range(row, number, 1), range(col, -1, -1)):
        if board[a][b] == 1:
            return False

    return True


def solveNQUtil(board, col, number):
    """Recursively finds all possible solutions for N Queens.

    Args:
        board (list): A list of lists representing the chessboard.
        col (int): Current column being considered.
        number (int): Size of the chessboard.

    Returns:
        bool: True if a solution is found, False otherwise.
    """
    if col == number:
        print_board(board)
        return True
    res = False
    for a in range(number):
        if isSafe(board, a, col, number):
            board[a][col] = 1
            res = solveNQUtil(board, col + 1, number) or res
            board[a][col] = 0  # BACKTRACK

    return res


def solve(number):
    """Finds and prints all possible solutions for N Queens.

    Args:
        number (int): Size of the chessboard.
    """
    board = [[0 for a in range(number)] for a in range(number)]

    if not solveNQUtil(board, 0, number):
        print("No solution exists.")


def validate(args):
    """Validates the input data and returns the size of the chessboard.

    Args:
        args (list): List of command line arguments.

    Returns:
        int: Size of the chessboard.

    Raises:
        ValueError: If the input is invalid.
    """
    if len(args) == 2:
        try:
            number = int(args[1])
        except ValueError:
            print("N must be a number.")
            exit(1)
        if number < 4:
            print("N must be at least 4.")
            exit(1)
        return number
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    """Main method to execute the application."""
    number = validate(sys.argv)
    solve(number)
