import pytest
from src.alternating_dot_case import convert_to_alternating_dot_case

def test_convert_to_alternating_dot_case_basic():
    """Test basic string conversion"""
    assert convert_to_alternating_dot_case("hello") == "h.E.l.L.o"
    assert convert_to_alternating_dot_case("python") == "p.Y.t.H.o.N"

def test_convert_to_alternating_dot_case_empty_string():
    """Test empty string conversion"""
    assert convert_to_alternating_dot_case("") == ""

def test_convert_to_alternating_dot_case_single_character():
    """Test single character conversion"""
    assert convert_to_alternating_dot_case("a") == "a"
    assert convert_to_alternating_dot_case("Z") == "z"

def test_convert_to_alternating_dot_case_mixed_case():
    """Test mixed case input"""
    assert convert_to_alternating_dot_case("HeLLo") == "h.E.l.L.o"

def test_convert_to_alternating_dot_case_with_spaces():
    """Test string with spaces"""
    assert convert_to_alternating_dot_case("hello world") == "h.E.l.L.o. .W.o.R.l.D"

def test_convert_to_alternating_dot_case_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(None)
    
    with pytest.raises(TypeError):
        convert_to_alternating_dot_case(["list"])