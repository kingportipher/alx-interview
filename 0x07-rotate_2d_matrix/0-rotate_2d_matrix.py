#!/usr/bin/python3

"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degree.
    """
    size = len(matrix)

    # Process the matrix in layers (outermost to innermost)
    for layer_index in range(size // 2):
        start = layer_index
        end = size - 1 - layer_index

        # Rotate elements in the current layer
        for element_index in range(start, end):
            # Save the top element
            temp = matrix[start][element_index]

            # Perform the four-way element swap
            matrix[start][element_index] = matrix[end - element_index + start][start]
            matrix[end - element_index + start][start] = matrix[end][end - element_index + start]
            matrix[end][end - element_index + start] = matrix[element_index][end]
            matrix[element_index][end] = temp

