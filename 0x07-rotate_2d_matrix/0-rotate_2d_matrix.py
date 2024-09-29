#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix: A 2D list representing the matrix to be rotated.
    """

    n = len(matrix)  # Get the size of the matrix

    # Loop through layers from the outer layer to the middle (if even size)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1

        # Loop through each element in the current layer
        for i in range(first, last):
            # Swap elements in a clockwise direction
            offset = i - first
            temp = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = temp
