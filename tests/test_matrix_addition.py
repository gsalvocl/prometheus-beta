"""
Unit tests for matrix addition function.
"""
import pytest
from src.matrix_addition import add_matrices

def test_basic_matrix_addition():
    """Test basic matrix addition with integer matrices."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_matrix_addition_with_floats():
    """Test matrix addition with floating-point numbers."""
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    expected = [[2.0, 4.0], [6.0, 8.0]]
    assert add_matrices(matrix1, matrix2) == expected

def test_different_row_count_raises_error():
    """Test that matrices with different row counts raise ValueError."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same number of rows"):
        add_matrices(matrix1, matrix2)

def test_different_column_count_raises_error():
    """Test that matrices with different column counts raise ValueError."""
    matrix1 = [[1, 2, 3], [4, 5, 6]]
    matrix2 = [[7, 8], [9, 10]]
    with pytest.raises(ValueError, match="Matrices must have the same column lengths"):
        add_matrices(matrix1, matrix2)

def test_non_list_input_raises_error():
    """Test that non-list inputs raise TypeError."""
    with pytest.raises(TypeError, match="Inputs must be lists"):
        add_matrices("not a list", [[1, 2]])

def test_non_matrix_input_raises_error():
    """Test that inputs that are not lists of lists raise TypeError."""
    with pytest.raises(TypeError, match="Matrix must be a list of lists"):
        add_matrices([1, 2], [[3, 4]])

def test_empty_matrix_raises_error():
    """Test that empty matrices raise ValueError."""
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [[1, 2]])