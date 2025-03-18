import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding elements in a sorted list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 15) == 7

def test_binary_search_not_found():
    """Test elements not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 16) == -1
    assert binary_search(arr, 6) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element():
    """Test searching in a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    with pytest.raises(TypeError):
        binary_search(None, 5)

def test_binary_search_unsorted_list():
    """Test unsorted list raises ValueError"""
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 4], 3)

def test_binary_search_duplicate_values():
    """Test list with duplicate values"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    assert binary_search(arr, 3) in [3, 4, 5]  # any index of 3 is acceptable