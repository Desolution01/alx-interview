#!/usr/bin/python3
"""Rotate 2D Matrix"""

def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list): The 2D matrix to be rotated.
    """
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return

    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp

    rotate_2d_matrix(matrix)
    print(matrix)

