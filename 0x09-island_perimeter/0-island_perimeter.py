#!/usr/bin/python3

"""
Module: island_perimeter

"""
def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.
    """
    perimeter = 0

    if not grid or not isinstance(grid, list) or not all(isinstance(row, list) for row in grid):
        return 0
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[row_idx])):
            # Only process land cells
            if grid[row_idx][col_idx] == 1:
                # Check top
                if row_idx == 0 or grid[row_idx - 1][col_idx] == 0:
                    perimeter += 1
                # Check bottom
                if row_idx == len(grid) - 1 or grid[row_idx + 1][col_idx] == 0:
                    perimeter += 1
                # Check left
                if col_idx == 0 or grid[row_idx][col_idx - 1] == 0:
                    perimeter += 1
                # Check right
                if col_idx == len(grid[row_idx]) - 1 or grid[row_idx][col_idx + 1] == 0:
                    perimeter += 1

    return perimeter
