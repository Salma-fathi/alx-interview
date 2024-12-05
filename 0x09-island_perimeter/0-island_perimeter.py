#!/usr/bin/python3
"""
A module: defines a function that calculates
the perimeter of an island on a given grid
"""

def island_perimeter(grid):
    """"  The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island)."""
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for each land cell
                perimeter += 4
                
                # Check adjacent cells and subtract 2 for each adjacent land cell
                # Check cell above
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # Check cell to the left
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
