#!/usr/bin/python3
"""
script that defines function for matrix division.
"""

def matrix_divided(matrix, div):
    """
    Divide elements of the matrix.

    Args:
        matrix (list): list of lists of ints or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix contains non-nums.
        TypeError: If matrix contains rows with different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        new matrix representing result of division.
    """

    # Check if matrix is a list of non-empty lists containing only integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be matrix of ints/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of matrix must have same size")

    # Check if div is an integer or a float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be num")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix containing the results of the division
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Return the new matrix
    return new_matrix
