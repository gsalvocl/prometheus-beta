"""
Test suite for LZ4 compression and decompression functions.
"""

import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lz4_compression import lz4_compress, lz4_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    original = "hello world hello world"
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_repeated_sequences():
    """Test compression of data with repeated sequences."""
    original = "abcabcabcabcabcabc"
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_bytes_compression():
    """Test compression of byte data."""
    original = b'\x00\x01\x02\x03\x00\x01\x02\x03'
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError):
        lz4_compress("")
    
    with pytest.raises(ValueError):
        lz4_decompress(b'')

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        lz4_compress(123)
    
    with pytest.raises(TypeError):
        lz4_decompress(123)

def test_complex_data():
    """Test compression of more complex data."""
    original = "The quick brown fox jumps over the lazy dog " * 10
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed.decode('utf-8') == original

def test_binary_data():
    """Test compression of binary data."""
    original = bytes(range(256)) * 5
    compressed = lz4_compress(original)
    decompressed = lz4_decompress(compressed)
    
    assert decompressed == original