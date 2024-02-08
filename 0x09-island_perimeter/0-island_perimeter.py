#!/usr/bin/python3

"""
A module that contains a function that returns the perimeter of an island
described in grid
"""


def island_perimeter(grid):
    """
    A function that outputs the perimeter of an island described by grid

    Args:
    - grid: A 2D list representing the island where 1s represent land and
    0s represent water

    Returns:
    - perimeter: The perimeter of the island
    """
    perimeter = 0
    grid_length = len(grid)
    # Iterate over each cell in the grid
    for row in range(grid_length):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                # Check neighboring cells to determine perimeter
                # Check if the cell is at the boundary or has water on its top
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                # Check if the cell is at the boundary or has water on its left
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                # Check if the cell is at the
                # boundary or has water on its right
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    perimeter += 1
                # Check if the cell is at the boundary
                # or has water on its bottom
                if row + 1 >= grid_length or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter
