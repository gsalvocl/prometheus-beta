import pytest
import logging
import io
from src.input_validation_logger import validate_input

# Capture log output for testing
def capture_logs(log_level=logging.WARNING):
    # Create a string handler
    log_capture = io.StringIO()
    handler = logging.StreamHandler(log_capture)
    handler.setLevel(log_level)
    
    # Get the root logger and configure it
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Remove existing handlers to avoid duplicate logging
    for existing_handler in logger.handlers[:]:
        logger.removeHandler(existing_handler)
    
    logger.addHandler(handler)
    
    return log_capture, handler, logger

def remove_log_handler(handler, logger):
    logger.removeHandler(handler)

def test_validate_input_basic():
    @validate_input()
    def test_func(x: int, y: int):
        return x + y
    
    # Reset logging to capture logs consistently
    logging.getLogger().handlers.clear()
    log_capture, handler, logger = capture_logs()
    
    try:
        result = test_func(5, 3)
        assert result == 8
        
        # Flush the log capture to ensure all logs are written
        handler.flush()
        
        # Check log contents
        log_output = log_capture.getvalue()
        assert "Input arguments: args=(5, 3), kwargs={}" in log_output
        assert "Input validation successful" in log_output
    finally:
        remove_log_handler(handler, logger)

def test_validate_input_no_args():
    @validate_input()
    def test_func():
        return True
    
    # Reset logging to capture logs consistently
    logging.getLogger().handlers.clear()
    log_capture, handler, logger = capture_logs()
    
    try:
        result = test_func()
        assert result is True
        
        # Flush the log capture to ensure all logs are written
        handler.flush()
        
        # Check log contents
        log_output = log_capture.getvalue()
        assert "No arguments provided" in log_output
    finally:
        remove_log_handler(handler, logger)

def test_validate_input_type_error():
    @validate_input()
    def test_func(x: int):
        return x
    
    # Reset logging to capture logs consistently
    logging.getLogger().handlers.clear()
    log_capture, handler, logger = capture_logs()
    
    try:
        with pytest.raises(TypeError):
            test_func("not an int")
        
        # Flush the log capture to ensure all logs are written
        handler.flush()
        
        # Check log contents
        log_output = log_capture.getvalue()
        assert "Type error in input validation" in log_output
    finally:
        remove_log_handler(handler, logger)

def test_validate_input_value_error():
    @validate_input()
    def test_func(x: int):
        if x < 0:
            raise ValueError("Negative values not allowed")
        return x
    
    # Reset logging to capture logs consistently
    logging.getLogger().handlers.clear()
    log_capture, handler, logger = capture_logs()
    
    try:
        with pytest.raises(ValueError):
            test_func(-5)
        
        # Flush the log capture to ensure all logs are written
        handler.flush()
        
        # Check log contents
        log_output = log_capture.getvalue()
        assert "Value error in input validation" in log_output
    finally:
        remove_log_handler(handler, logger)

def test_validate_input_custom_log_level():
    @validate_input(log_level=logging.INFO)
    def test_func(x: int):
        return x
    
    # Reset logging to capture logs consistently
    logging.getLogger().handlers.clear()
    log_capture, handler, logger = capture_logs(logging.INFO)
    
    try:
        result = test_func(10)
        assert result == 10
        
        # Flush the log capture to ensure all logs are written
        handler.flush()
        
        # Check log contents
        log_output = log_capture.getvalue()
        assert "Input arguments: args=(10,), kwargs={}" in log_output
        assert "Input validation successful" in log_output
    finally:
        remove_log_handler(handler, logger)