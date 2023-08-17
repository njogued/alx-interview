#!/usr/bin/python3
"""Function to rotate a 2D matrix in place"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix leetcode"""
    n = len(matrix)
    new_matrix = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            new_row = col
            new_col = n - 1 - row
            new_matrix[new_row][new_col] = matrix[row][col]
    return new_matrix
