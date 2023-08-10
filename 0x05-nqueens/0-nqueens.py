#!/usr/bin/python3
"""Implementing the nqueens problem using backtracking"""
import sys


def solve_nqueens(n):
    """Function that implements the solve nqueens algorithm"""
    def is_safe(board, row, col):
        """Helper function to check if it's safe to place queen"""
        for prev_row in range(row):
            if board[prev_row] == col or \
               abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def backtrack(row):
        """Function that appends a valid placement to solutions"""
        if row == n:
            solutions.append(list(board))
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        try:
            n = int(sys.argv[1])
            if n < 4:
                print("N must be at least 4")
                sys.exit(1)
            else:
                solutions = solve_nqueens(n)
                for solution in solutions:
                    solsol = []
                    for k, v in enumerate(solution):
                        sol = [k, v]
                        solsol.append(sol)
                    print(solsol)
        except ValueError:
            print("N must be a number")
            sys.exit(1)


if __name__ == "__main__":
    main()
