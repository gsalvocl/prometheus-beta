import pytest
import zlib
from src.deflate_compression import deflate_compress, deflate_decompress

def test_deflate_compress_string():
    """Test compression of a string"""
    original = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(original)
    assert compressed != original.encode('utf-8')
    # Check that compression doesn't trivially increase size or stay the same
    assert len(compressed) != len(original.encode('utf-8'))

def test_deflate_compress_bytes():
    """Test compression of bytes"""
    original = b"Binary data compression test"
    compressed = deflate_compress(original)
    assert compressed != original
    # Check that compression doesn't trivially increase size or stay the same
    assert len(compressed) != len(original)

def test_deflate_decompress():
    """Test round-trip compression and decompression"""
    original = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(original)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_deflate_binary_roundtrip():
    """Test round-trip compression and decompression with binary data"""
    original = b'\x00\x01\x02\x03\x04\x05\x06\x07'
    compressed = deflate_compress(original)
    decompressed = deflate_decompress(compressed)
    assert decompressed == original

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        deflate_compress(123)
    with pytest.raises(TypeError):
        deflate_decompress(123)

def test_none_input():
    """Test error handling for None input"""
    with pytest.raises(ValueError):
        deflate_compress(None)
    with pytest.raises(ValueError):
        deflate_decompress(None)

def test_empty_input():
    """Test error handling for empty input"""
    with pytest.raises(ValueError):
        deflate_compress(b'')
    with pytest.raises(ValueError):
        deflate_decompress(b'')

def test_large_data_compression():
    """Test compression of larger data"""
    original = b'0' * 10000
    compressed = deflate_compress(original)
    assert len(compressed) != len(original)
    decompressed = deflate_decompress(compressed)
    assert decompressed == original

def test_incompressible_data():
    """Test compression of data that doesn't compress well"""
    import secrets
    original = secrets.token_bytes(1000)  # Random bytes
    compressed = deflate_compress(original)
    decompressed = deflate_decompress(compressed)
    assert decompressed == original