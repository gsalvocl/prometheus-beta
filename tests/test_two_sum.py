import pytest
from src.two_sum import two_sum

def test_basic_two_sum():
    """Test finding two indices that sum to a target"""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_no_solution():
    """Test when no solution exists"""
    assert two_sum([2, 3, 4], 10) == []

def test_multiple_solutions():
    """Verify returns first valid solution"""
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_same_element_solution():
    """Handle case where same element could be used twice"""
    assert two_sum([3, 3], 6) == [0, 1]

def test_negative_numbers():
    """Support negative numbers in the list"""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_zero_target():
    """Handle zero as a target sum"""
    assert two_sum([0, 0], 0) == [0, 1]

def test_invalid_input_not_list():
    """Raise TypeError if input is not a list"""
    with pytest.raises(TypeError):
        two_sum("not a list", 5)

def test_invalid_target_type():
    """Raise TypeError if target is not an integer"""
    with pytest.raises(TypeError):
        two_sum([1, 2, 3], "not an int")

def test_invalid_list_elements():
    """Raise ValueError if list contains non-integer elements"""
    with pytest.raises(ValueError):
        two_sum([1, "2", 3], 5)

def test_empty_list():
    """Handle empty list"""
    assert two_sum([], 5) == []

def test_large_numbers():
    """Test with larger numbers"""
    assert two_sum([1000000, 1000001, 1000002], 2000001) == [0, 1]