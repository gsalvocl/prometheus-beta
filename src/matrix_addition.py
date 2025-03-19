"""
Module for matrix addition with size compatibility checking.
"""
from typing import List, Union

def add_matrices(matrix1: List[List[Union[int, float]]], 
                 matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Add two matrices by adding corresponding elements.

    Args:
        matrix1 (List[List[Union[int, float]]]): First input matrix
        matrix2 (List[List[Union[int, float]]]): Second input matrix

    Returns:
        List[List[Union[int, float]]]: Resulting matrix after addition

    Raises:
        ValueError: If matrices have incompatible dimensions
        TypeError: If input is not a valid matrix (list of lists)
    """
    # Validate input is a matrix (list of lists)
    if not isinstance(matrix1, list) or not isinstance(matrix2, list):
        raise TypeError("Inputs must be lists")
    
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check row lengths are consistent within each matrix
    if any(not isinstance(row, list) for row in matrix1 + matrix2):
        raise TypeError("Matrix must be a list of lists")
    
    # Check matrix dimensions
    if len(matrix1) != len(matrix2):
        raise ValueError("Matrices must have the same number of rows")
    
    # Check that each row has the same length in both matrices
    if any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("Matrices must have the same column lengths")
    
    # Perform matrix addition
    return [
        [row1_elem + row2_elem for row1_elem, row2_elem in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]