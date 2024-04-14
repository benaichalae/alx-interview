#!/usr/bin/python3
"""Module to generate Pascal's Triangle integers."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.

    Args:
        n (int): The number of rows in the Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.

    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)

    return triangle
