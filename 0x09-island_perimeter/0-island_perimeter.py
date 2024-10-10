#!/usr/bin/python3

def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Add 4 for potential edges

                # Check if left neighbor is water
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                # Check if right neighbor is water
                if col + 1 >= cols or grid[row][col + 1] == 0:
                    perimeter += 1

                # Check if top neighbor is water (if not on top row)
                if row - 1 >= 0 and grid[row - 1][col] == 0:
                    perimeter += 1

                # Check if bottom neighbor is water (if not on bottom row)
                if row + 1 < rows and grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter
