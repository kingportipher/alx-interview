def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell contributes 4 to the perimeter initially
                perimeter += 4
                
                # Check above (i-1)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge

                # Check left (j-1)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared edge
    
    return perimeter
