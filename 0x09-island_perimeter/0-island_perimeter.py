#!/usr/bin/python3
"""
Function to check the perimeter of an island
"""


def island_perimeter(grid):
    """Calculate island perimeter"""
    perimeter = 0
    ones = {}
    row_num = 0
    for row in grid:
        row_islands = []
        item_num = 0
        for item in row:
            if item == 1:
                max_perimeter = 4
                row_islands.append(item_num)
                ones[row_num] = row_islands
                if item_num - 1 in ones[row_num]:
                    max_perimeter -= 2
                if row_num - 1 in ones.keys():
                    if item_num in ones[row_num - 1]:
                        max_perimeter -= 2
                perimeter += max_perimeter
            item_num += 1
        row_num += 1
    return perimeter
