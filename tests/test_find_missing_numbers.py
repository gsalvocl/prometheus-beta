import pytest
from src.find_missing_numbers import find_missing_numbers

def test_basic_missing_numbers():
    """Test finding missing numbers in a simple scenario."""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_large_range_missing_numbers():
    """Test finding missing numbers in a larger range."""
    assert find_missing_numbers([1, 10]) == [2, 3, 4, 5, 6, 7, 8, 9]

def test_consecutive_numbers():
    """Test a case with no missing numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_repeated_numbers():
    """Test a case with repeated numbers."""
    assert find_missing_numbers([5, 5, 7]) == [6]

def test_single_number():
    """Test a case with a single number."""
    assert find_missing_numbers([5]) == []

def test_invalid_input_none():
    """Test that None input raises ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be None"):
        find_missing_numbers(None)

def test_invalid_input_empty():
    """Test that empty input raises ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_invalid_input_non_integer():
    """Test that non-integer input raises TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([1, '2', 3])

def test_descending_order():
    """Test that the function requires a sorted (ascending) input."""
    with pytest.raises(TypeError):
        find_missing_numbers([10, 5, 1])