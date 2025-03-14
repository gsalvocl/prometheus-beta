import pytest
from src.palindrome_checker import is_palindrome

def test_standard_palindromes():
    """Test standard palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    """Test non-palindrome scenarios"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test various edge cases"""
    # Empty string
    assert is_palindrome("") == True
    
    # Single character
    assert is_palindrome("a") == True
    assert is_palindrome("1") == True
    
    # Mixed case
    assert is_palindrome("Able was I ere I saw Elba") == True
    
    # Strings with numbers and special characters
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("123 321") == True
    
    # Strings with only non-alphanumeric characters
    assert is_palindrome("!@#") == True

def test_unicode_characters():
    """Test with unicode and international characters"""
    assert is_palindrome("なんでもないよ") == False
    assert is_palindrome("アンナ") == True  # Japanese name "Anna"

def test_whitespace_and_punctuation():
    """Test handling of whitespace and punctuation"""
    assert is_palindrome("  radar  ") == True
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("No 'x' in Nixon?") == True