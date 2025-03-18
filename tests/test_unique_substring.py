import pytest
from src.unique_substring import find_longest_substring

def test_normal_cases():
    """Test various normal input scenarios."""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_edge_cases():
    """Test edge cases like empty string, single character, etc."""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_full_unique_string():
    """Test when entire string has unique characters."""
    assert find_longest_substring("abcdef") == "abcdef"

def test_multiple_longest_substrings():
    """Test cases with multiple longest unique substrings."""
    result = find_longest_substring("abcdaf")
    assert result in ["abcd", "cdaf"]
    assert len(result) == 4

def test_unicode_characters():
    """Test with unicode and non-ASCII characters."""
    assert find_longest_substring("こんにちは") == "こんにち"

def test_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        find_longest_substring(None)
    
    with pytest.raises(TypeError):
        find_longest_substring(123)

def test_complex_scenarios():
    """Test more complex substring scenarios."""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"