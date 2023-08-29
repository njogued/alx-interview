#!/usr/bin/python3
"""Function to rotate a 2D matrix in place"""


def rotate_2d_matrix(matrix):
    start = (len(matrix) * (len(matrix) - 1)) + 1
    mapped = {}
    x = 0
    for row in matrix:
        for col in row:
            x += 1
            mapped[x] = col
    shifted = {}
    box = 0
    x = start
    for _ in range(1, len(matrix) + 1):
        x = start
        for _ in range(1, len(matrix) + 1):
            box += 1
            shifted[box] = mapped[x]
            x = x - len(matrix)
        start += 1
    new_matrix = []
    box = 0
    for _ in range(len(matrix)):
        one_row = []
        for _ in range(len(matrix)):
            box += 1
            one_row.append(shifted[box])
        new_matrix.append(one_row)
    return new_matrix
