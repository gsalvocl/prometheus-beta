import pytest
import logging
from src.input_validation_logger import validate_input

def test_validate_input_basic():
    # Configure logging
    logger = logging.getLogger('test_func')
    logger.setLevel(logging.DEBUG)
    
    @validate_input()
    def test_func(x: int, y: int):
        return x + y
    
    # Capture log messages
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    try:
        result = test_func(5, 3)
        assert result == 8
        
        # Check log contents
        log_records = [record.getMessage() for record in logger.handlers[0].records]
        assert any("Input arguments: args=(5, 3), kwargs={}" in record for record in log_records)
        assert any("Input validation successful" in record for record in log_records)
    finally:
        logger.removeHandler(handler)

def test_validate_input_no_args():
    # Configure logging
    logger = logging.getLogger('test_func')
    logger.setLevel(logging.DEBUG)
    
    @validate_input()
    def test_func():
        return True
    
    # Capture log messages
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    try:
        result = test_func()
        assert result is True
        
        # Check log contents
        log_records = [record.getMessage() for record in logger.handlers[0].records]
        assert any("No arguments provided" in record for record in log_records)
    finally:
        logger.removeHandler(handler)

def test_validate_input_type_error():
    # Configure logging
    logger = logging.getLogger('test_func')
    logger.setLevel(logging.DEBUG)
    
    @validate_input()
    def test_func(x: int):
        return x
    
    # Capture log messages
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    try:
        with pytest.raises(TypeError):
            test_func("not an int")
        
        # Check log contents
        log_records = [record.getMessage() for record in logger.handlers[0].records]
        assert any("Input arguments: args=('not an int',), kwargs={}" in record for record in log_records)
        assert any("Type error in input validation" in record for record in log_records)
    finally:
        logger.removeHandler(handler)

def test_validate_input_value_error():
    # Configure logging
    logger = logging.getLogger('test_func')
    logger.setLevel(logging.DEBUG)
    
    @validate_input()
    def test_func(x: int):
        if x < 0:
            raise ValueError("Negative values not allowed")
        return x
    
    # Capture log messages
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    
    try:
        with pytest.raises(ValueError):
            test_func(-5)
        
        # Check log contents
        log_records = [record.getMessage() for record in logger.handlers[0].records]
        assert any("Input arguments: args=(-5,), kwargs={}" in record for record in log_records)
        assert any("Value error in input validation" in record for record in log_records)
    finally:
        logger.removeHandler(handler)

def test_validate_input_custom_log_level():
    # Configure logging
    logger = logging.getLogger('test_func')
    logger.setLevel(logging.INFO)
    
    @validate_input(log_level=logging.INFO)
    def test_func(x: int):
        return x
    
    # Capture log messages
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    try:
        result = test_func(10)
        assert result == 10
        
        # Check log contents
        log_records = [record.getMessage() for record in logger.handlers[0].records]
        assert any("Input arguments: args=(10,), kwargs={}" in record for record in log_records)
        assert any("Input validation successful" in record for record in log_records)
    finally:
        logger.removeHandler(handler)