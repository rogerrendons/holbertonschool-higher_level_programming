#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        return [[num**2 for num in matrix[i]] for i in range(len(matrix))]
