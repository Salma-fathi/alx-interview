#!/usr/bin/python3
"""
A module that defines a function to calculate
the perimeter of an island on a given grid.
"""


def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid.

    Args:
        grid (List[List[int]]): A list of list of integers where:
            - 0 represents water
            - 1 represents land

    Notes:
        - The grid is completely surrounded by water
        - There is only one island (or nothing)
        - The island doesn't have "lakes"

    Returns:
        int: The perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4

                # Check adjacent cells and subtract 2 for each adjacent land cell
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
