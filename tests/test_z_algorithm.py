import pytest
from src.z_algorithm import z_algorithm

def test_basic_string_matching():
    """Test basic string matching functionality."""
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    assert z_algorithm(text, pattern) == [10]

def test_multiple_occurrences():
    """Test finding multiple occurrences of a pattern."""
    text = "AAAAAAA"
    pattern = "AAA"
    assert z_algorithm(text, pattern) == [0, 1, 2, 3, 4]

def test_no_occurrences():
    """Test when pattern is not found in text."""
    text = "ABCDEF"
    pattern = "XYZ"
    assert z_algorithm(text, pattern) == []

def test_pattern_equals_text():
    """Test when pattern is the entire text."""
    text = "HELLO"
    pattern = "HELLO"
    assert z_algorithm(text, pattern) == [0]

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        z_algorithm(123, "pattern")
    with pytest.raises(TypeError):
        z_algorithm("text", 456)

def test_empty_inputs():
    """Test error handling for empty inputs."""
    with pytest.raises(ValueError):
        z_algorithm("", "pattern")
    with pytest.raises(ValueError):
        z_algorithm("text", "")

def test_case_sensitivity():
    """Test that matching is case-sensitive."""
    text = "AbcABCabc"
    pattern = "abc"
    assert z_algorithm(text, pattern) == [6]

def test_long_text_and_pattern():
    """Test with a longer text and pattern."""
    text = "a" * 1000 + "b"
    pattern = "a" * 500
    matches = z_algorithm(text, pattern)
    assert len(matches) == 501  # First 501 positions should match