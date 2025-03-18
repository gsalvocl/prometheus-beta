import pytest
from src.subarray_product_less_than_k import count_subarrays_with_product_less_than_k

def test_basic_functionality():
    """Test basic functionality of the function"""
    assert count_subarrays_with_product_less_than_k([10, 5, 2, 6], 100) == 8

def test_edge_cases():
    """Test various edge cases"""
    # Empty array
    assert count_subarrays_with_product_less_than_k([], 10) == 0
    
    # k is 1 or less (no valid subarrays)
    assert count_subarrays_with_product_less_than_k([1, 2, 3], 1) == 0
    
    # All elements are less than k
    assert count_subarrays_with_product_less_than_k([1, 2, 3], 10) == 6

def test_single_element_array():
    """Test arrays with a single element"""
    assert count_subarrays_with_product_less_than_k([5], 10) == 1
    assert count_subarrays_with_product_less_than_k([11], 10) == 0

def test_large_elements():
    """Test with large elements"""
    assert count_subarrays_with_product_less_than_k([1, 100, 10, 5], 50) == 3

def test_all_elements_greater_than_k():
    """Test when all elements are greater than k"""
    assert count_subarrays_with_product_less_than_k([10, 20, 30], 5) == 0

def test_mixed_elements():
    """Test array with mixed elements"""
    test_array = [1, 2, 3, 4]
    assert count_subarrays_with_product_less_than_k(test_array, 10) == 7