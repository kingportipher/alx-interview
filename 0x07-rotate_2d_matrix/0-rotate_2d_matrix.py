#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates the given n x n 2D matrix by 90 degrees clockwise in-place.
    """
    n = len(matrix)
    
    # Transpose the matrix: swap rows and columns
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row to complete the rotation
    for i in range(n):
        matrix[i].reverse()

