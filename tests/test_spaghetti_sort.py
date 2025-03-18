import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test basic sorting of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_empty_list():
    """Test sorting an empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test sorting a list with a single element"""
    assert spaghetti_sort([42]) == [42]

def test_spaghetti_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert spaghetti_sort(input_list) == input_list

def test_spaghetti_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 7, -1]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_does_not_modify_original():
    """Test that the original list is not modified"""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    spaghetti_sort(input_list)
    assert input_list == original_copy

def test_spaghetti_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        spaghetti_sort("not a list")

def test_spaghetti_sort_incomparable_elements():
    """Test that ValueError is raised for incomparable elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        spaghetti_sort([1, 2, "a"])