import pytest
from src.smallest_list_sum import find_smallest_list_sum

def test_basic_positive_numbers():
    """Test with basic positive integers"""
    assert find_smallest_list_sum([1, 2, 3], [4, 5, 6]) == 5

def test_mixed_numbers():
    """Test with mixed positive and negative integers"""
    assert find_smallest_list_sum([-1, 2, 3], [4, -5, 6]) == 3

def test_single_element_lists():
    """Test with single-element lists"""
    assert find_smallest_list_sum([10], [5]) == 15

def test_floating_point_conversions():
    """Test lists with float-convertible elements"""
    assert find_smallest_list_sum([1.0, 2.0], [3, 4]) == 4

def test_empty_list_raises_error():
    """Test that empty lists raise a ValueError"""
    with pytest.raises(ValueError, match="Input lists cannot be empty"):
        find_smallest_list_sum([], [1, 2, 3])
    with pytest.raises(ValueError, match="Input lists cannot be empty"):
        find_smallest_list_sum([1, 2, 3], [])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_list_sum(123, [1, 2, 3])
    with pytest.raises(ValueError, match="Inputs must be lists"):
        find_smallest_list_sum([1, 2, 3], "not a list")

def test_non_integer_raises_error():
    """Test that non-integer elements raise a TypeError"""
    with pytest.raises(TypeError, match="All list elements must be integers"):
        find_smallest_list_sum(['a', 'b'], [1, 2])
    with pytest.raises(TypeError, match="All list elements must be integers"):
        find_smallest_list_sum([1, 2], [None, 3])

def test_repeated_elements():
    """Test lists with repeated elements"""
    assert find_smallest_list_sum([1, 1, 1], [2, 2, 2]) == 3