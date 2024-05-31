#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_matrix(matrix):
    """
    Rotates an n x n 2D matrix in place by 90 degrees clockwise.
    """
    n = len(matrix)
    # Loop through layers
    for layer in range(n // 2):
        # Define first, last elements for current layer
        first = layer
        last = n - layer - 1

    # Loop through elements in the current layer
    for i in range(first, last):
        # Swap elements in a circular fashion
        offset = i - first
        temp = matrix[first][i]
        matrix[first][i] = matrix[last - offset][first]
        matrix[last - offset][first] = matrix[last][last - offset]
        matrix[last][last - offset] = matrix[i][last]
        matrix[i][last] = temp
