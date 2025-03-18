import logging
import time
import pytest
from src.execution_timer import log_execution_time

# Setup a mock logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_basic_execution_time_logging():
    """Test that execution time is logged with default print"""
    @log_execution_time()
    def sample_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    result = sample_function(3, 4)
    assert result == 7  # Ensure function still works correctly

def test_custom_logger_logging():
    """Test logging with a custom logger"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def sample_function(x, y):
        time.sleep(0.1)  # Simulate some work
        return x + y
    
    result = sample_function(3, 4)
    assert result == 7  # Ensure function still works correctly
    
    # Check that a log entry was created
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'info'
    assert 'sample_function' in log_message
    assert 'seconds' in log_message

def test_exception_handling():
    """Test that exceptions are properly logged and re-raised"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def function_that_raises():
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError, match="Test exception"):
        function_that_raises()
    
    # Check that an error log was created
    assert len(mock_logger.logs) == 1
    log_level, log_message = mock_logger.logs[0]
    assert log_level == 'error'
    assert 'function_that_raises' in log_message
    assert 'Test exception' in log_message

def test_preserves_function_metadata():
    """Ensure the decorator preserves function metadata"""
    @log_execution_time()
    def test_function(x):
        """A docstring to test metadata preservation"""
        return x * 2
    
    assert test_function.__name__ == 'test_function'
    assert 'A docstring to test metadata preservation' in test_function.__doc__