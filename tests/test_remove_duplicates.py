import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic duplicate removal"""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_large_list():
    """Test with a larger list of integers"""
    input_list = [10, 20, 30, 40, 20, 50, 10, 60, 70, 30, 80, 90, 40, 100]
    expected = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_all_duplicates():
    """Test a list with all elements being duplicates"""
    input_list = [1, 1, 1, 1, 1]
    expected = [1]
    assert remove_duplicates(input_list) == expected

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates"""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_empty_list():
    """Test an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_type_error():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        remove_duplicates("not a list")
    with pytest.raises(TypeError):
        remove_duplicates(123)