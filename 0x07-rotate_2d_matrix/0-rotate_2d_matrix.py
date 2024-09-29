#!/usr/bin/python3
"""
Rotate n * n matrix in 90 degress
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a n * n matrix
    Args:
        matrix: n * n matrix
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            if i != j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    for i in range(len(matrix)):
        mat = matrix[i]

        for j in range(len(mat) // 2):
            temp = mat[j]
            mat[j] = mat[len(mat) - 1 - j]
            mat[len(mat) - 1 - j] = temp
