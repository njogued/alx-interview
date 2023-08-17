#!/usr/bin/python3
"""Function to rotate a 2D matrix in place"""


def rotate_2d_matrix(matrix):
    """Rotating a 2d matrix in place"""
    n = len(matrix)

    # Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for row in matrix:
        row.reverse()
