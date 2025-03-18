import pytest
import string
from src.password_generator import generate_random_password

def test_password_length():
    """Test that generated password matches specified length"""
    for length in [1, 5, 10, 20, 50]:
        password = generate_random_password(length)
        assert len(password) == length

def test_password_composition():
    """Test that password contains characters from different sets"""
    password = generate_random_password(20)
    
    # Check that the password contains a mix of character types
    assert any(char in string.ascii_lowercase for char in password)
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)

def test_randomness():
    """Test that multiple generated passwords are different"""
    passwords = set(generate_random_password(10) for _ in range(100))
    assert len(passwords) > 1  # Extremely unlikely to be all the same

def test_invalid_length_inputs():
    """Test error handling for invalid length inputs"""
    # Test zero length
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(0)
    
    # Test negative length
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_random_password(-5)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_random_password("10")
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_random_password(3.14)
    with pytest.raises(TypeError, match="Password length must be an integer"):
        generate_random_password(None)