#!/usr/bin/python3
"""
Function to check the perimeter of an island
"""


def island_perimeter(grid):
    """Calculate island perimeter"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                max_perimeter = 4
                if row > 0 and grid[row - 1][col] == 1:
                    max_perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    max_perimeter -= 2
                perimeter += max_perimeter

    return perimeter
