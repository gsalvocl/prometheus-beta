import pytest
from src.exponential_search import exponential_search

def test_exponential_search_basic():
    """Test basic functionality of exponential search"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Test finding elements at different positions
    assert exponential_search(arr, 1) == 0   # First element
    assert exponential_search(arr, 19) == 9  # Last element
    assert exponential_search(arr, 7) == 3   # Middle element
    assert exponential_search(arr, 13) == 6  # Another middle element

def test_exponential_search_not_found():
    """Test when target is not in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    assert exponential_search(arr, 0) == -1   # Below range
    assert exponential_search(arr, 20) == -1  # Above range
    assert exponential_search(arr, 4) == -1   # Between elements

def test_exponential_search_edge_cases():
    """Test edge cases"""
    # Single element array
    assert exponential_search([5], 5) == 0
    assert exponential_search([5], 6) == -1

    # Larger sorted array
    large_arr = list(range(0, 1000, 2))
    assert exponential_search(large_arr, 500) == large_arr.index(500)
    assert exponential_search(large_arr, 501) == -1

def test_exponential_search_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Empty list
    with pytest.raises(ValueError, match="Cannot search an empty list"):
        exponential_search([], 5)
    
    # Non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        exponential_search("not a list", 5)

def test_exponential_search_duplicate_elements():
    """Test behavior with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5]
    
    # For duplicates, it should return the index of one of the duplicates
    assert exponential_search(arr, 3) in [3, 4, 5]
    assert exponential_search(arr, 5) in [8, 9, 10]