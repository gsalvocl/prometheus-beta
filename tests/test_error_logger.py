import pytest
import sys
import io
from src.error_logger import log_error

def test_log_error_prints_message():
    """Test that log_error correctly prints the error message."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    log_error("Test error message")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check the output
    assert captured_output.getvalue().strip() == "ERROR: Test error message"

def test_log_error_with_non_string_raises_type_error():
    """Test that log_error raises TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="Error message must be a string"):
        log_error(123)

def test_log_error_with_empty_string():
    """Test that log_error works with empty string."""
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Call the function
    log_error("")

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Check the output
    assert captured_output.getvalue().strip() == "ERROR: "