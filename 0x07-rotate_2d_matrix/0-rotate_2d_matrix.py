#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    if not isinstance(matrix, list) or not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(isinstance(row, list) and len(row) == cols for row in matrix):
        return

    rotated_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - i - 1] = matrix[i][j]

    matrix.clear()
    matrix.extend(rotated_matrix)
