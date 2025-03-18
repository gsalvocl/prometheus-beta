import pytest
from src.bold_logger import log_bold_message

def test_log_bold_message(capsys):
    """Test that the message is logged in bold with correct ANSI escapes."""
    result = log_bold_message("Hello, World!")
    captured = capsys.readouterr()
    
    # Check return value
    assert result == '\033[1mHello, World!\033[0m'
    
    # Check printed output (visible in terminal)
    assert captured.out.strip() == '\033[1mHello, World!\033[0m'

def test_log_bold_message_with_numbers():
    """Test logging a message with numbers."""
    result = log_bold_message("Test 123")
    assert result == '\033[1mTest 123\033[0m'

def test_log_bold_message_with_special_chars():
    """Test logging a message with special characters."""
    result = log_bold_message("Hello, world! @#$%")
    assert result == '\033[1mHello, world! @#$%\033[0m'

def test_log_bold_message_empty_input():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold_message("")
    
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold_message("   ")

def test_log_bold_message_invalid_type():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_bold_message(123)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_bold_message(None)
    
    with pytest.raises(TypeError, match="Message must be a string"):
        log_bold_message(["hello"])