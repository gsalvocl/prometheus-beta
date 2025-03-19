import pytest
from src.find_missing_numbers import find_missing_numbers

def test_ascending_missing_numbers():
    """Test finding missing numbers in an ascending sorted array."""
    assert find_missing_numbers([1, 3, 5, 7]) == [2, 4, 6]
    assert find_missing_numbers([1, 2, 4, 6, 7, 9, 10]) == [3, 5, 8]

def test_descending_missing_numbers():
    """Test finding missing numbers in a descending sorted array."""
    assert find_missing_numbers([7, 5, 3, 1]) == [6, 4, 2]
    assert find_missing_numbers([10, 9, 7, 6, 4, 3, 1]) == [8, 5, 2]

def test_no_missing_numbers():
    """Test when no numbers are missing."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []
    assert find_missing_numbers([5, 4, 3, 2, 1]) == []

def test_empty_array():
    """Test with an empty array."""
    assert find_missing_numbers([]) == []

def test_single_element_array():
    """Test with a single element array."""
    assert find_missing_numbers([5]) == []
    assert find_missing_numbers([1]) == []

def test_large_range():
    """Test with a larger range of numbers."""
    assert find_missing_numbers([1, 3, 5, 10, 15, 20]) == [2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a list of positive integers"):
        find_missing_numbers([0, 1, 2])
    
    with pytest.raises(ValueError, match="Input must be a list of positive integers"):
        find_missing_numbers([-1, 2, 3])
    
    with pytest.raises(ValueError, match="Input must be a list of positive integers"):
        find_missing_numbers([1, 'a', 3])