import pytest
from src.palindrome_word_pairs import find_palindrome_pair_indices

def test_basic_palindrome_pairs():
    """Test finding basic palindrome pairs."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pair_indices(words)
    assert (0, 1) in result and (1, 0) in result
    assert len(result) == 2

def test_empty_list():
    """Test with an empty list."""
    words = []
    result = find_palindrome_pair_indices(words)
    assert result == []

def test_no_palindrome_pairs():
    """Test a list with no palindrome pairs."""
    words = ["hello", "world", "python"]
    result = find_palindrome_pair_indices(words)
    assert result == []

def test_single_word_list():
    """Test a list with a single word."""
    words = ["radar"]
    result = find_palindrome_pair_indices(words)
    assert result == []

def test_multiple_palindrome_pairs():
    """Test a list with multiple palindrome pairs."""
    words = ["dog", "god", "cat", "tac"]
    result = find_palindrome_pair_indices(words)
    assert len(result) == 4
    assert (0, 1) in result and (1, 0) in result
    assert (2, 3) in result and (3, 2) in result

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        find_palindrome_pair_indices("not a list")

def test_non_string_elements():
    """Test that a ValueError is raised for non-string list elements."""
    with pytest.raises(ValueError):
        find_palindrome_pair_indices(["valid", 123, "string"])

def test_case_sensitive():
    """Test that the function is case-sensitive."""
    words = ["Dog", "god"]
    result = find_palindrome_pair_indices(words)
    assert result == []