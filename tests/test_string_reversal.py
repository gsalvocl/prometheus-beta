import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_string_basic():
    """Test basic string reversal"""
    s = list('hello')
    reverse_string_in_place(s)
    assert s == list('olleh')

def test_reverse_string_empty():
    """Test empty string reversal"""
    s = []
    reverse_string_in_place(s)
    assert s == []

def test_reverse_string_single_char():
    """Test single character string"""
    s = list('a')
    reverse_string_in_place(s)
    assert s == list('a')

def test_reverse_string_even_length():
    """Test string with even number of characters"""
    s = list('python')
    reverse_string_in_place(s)
    assert s == list('nohtyp')

def test_reverse_string_with_spaces():
    """Test string with spaces"""
    s = list('hello world')
    reverse_string_in_place(s)
    assert s == list('dlrow olleh')

def test_reverse_string_with_symbols():
    """Test string with symbols"""
    s = list('a1b2c3')
    reverse_string_in_place(s)
    assert s == list('3c2b1a')

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for immutable inputs"""
    with pytest.raises(TypeError):
        reverse_string_in_place('not a list')

def test_modify_in_place():
    """Verify that the original list is modified in-place"""
    s = list('reverse')
    original_id = id(s)
    reverse_string_in_place(s)
    assert id(s) == original_id  # Ensure same list object is used
    assert s == list('esrever')