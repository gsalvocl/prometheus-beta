import pytest
import logging
import sys
import io
from src.input_validation_logger import validate_input

def test_validate_input_basic():
    @validate_input()
    def test_func(x: int, y: int):
        return x + y
    
    # Capture stdout/stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    try:
        result = test_func(5, 3)
        assert result == 8
        
        # Check log contents
        output = captured_output.getvalue()
        assert "Input arguments: args=(5, 3), kwargs={}" in output
    finally:
        # Restore stdout/stderr
        sys.stderr = sys.__stderr__

def test_validate_input_no_args():
    @validate_input()
    def test_func():
        return True
    
    # Capture stdout/stderr 
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    try:
        result = test_func()
        assert result is True
        
        # Check log contents
        output = captured_output.getvalue()
        assert "No arguments provided" in output
    finally:
        # Restore stdout/stderr
        sys.stderr = sys.__stderr__

def test_validate_input_type_error():
    @validate_input()
    def test_func(x: int):
        return x
    
    # Capture stdout/stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    try:
        with pytest.raises(TypeError):
            test_func("not an int")
        
        # Check log contents
        output = captured_output.getvalue()
        assert "Input arguments: args=('not an int',), kwargs={}" in output
        assert "Type error in input validation" in output
    finally:
        # Restore stdout/stderr
        sys.stderr = sys.__stderr__

def test_validate_input_value_error():
    @validate_input()
    def test_func(x: int):
        if x < 0:
            raise ValueError("Negative values not allowed")
        return x
    
    # Capture stdout/stderr
    captured_output = io.StringIO()
    sys.stderr = captured_output
    
    try:
        with pytest.raises(ValueError):
            test_func(-5)
        
        # Check log contents
        output = captured_output.getvalue()
        assert "Input arguments: args=(-5,), kwargs={}" in output
        assert "Value error in input validation" in output
    finally:
        # Restore stdout/stderr
        sys.stderr = sys.__stderr__

def test_validate_input_custom_log_level():
    @validate_input(log_level=logging.INFO)
    def test_func(x: int):
        return x
    
    # Capture stdout/stderr
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        result = test_func(10)
        assert result == 10
        
        # Check log contents
        output = captured_output.getvalue()
        assert "Input arguments: args=(10,), kwargs={}" in output
        assert "Input validation successful" in output
    finally:
        # Restore stdout/stderr
        sys.stdout = sys.__stdout__