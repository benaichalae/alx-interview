#!/usr/bin/python3
"""Module to compute the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island with no lakes.

    Args:
        grid (list of list of int): 2D list representing
        the grid where 1s represent land and 0s represent water.

    Returns:
        int: The perimeter of the island.
    """
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check if the top side is a boundary or water
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check if the right side is a boundary or water
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1
                # Check if the bottom side is a boundary or water
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check if the left side is a boundary or water
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1

    return perimeter
