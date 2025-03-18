import os
import gzip
import pytest
from src.gzip_decompressor import decompress_gzip_file

@pytest.fixture
def sample_gzip_file(tmp_path):
    """Create a sample gzip file for testing."""
    input_file = tmp_path / "sample.txt.gz"
    with gzip.open(input_file, 'wb') as f:
        f.write(b"This is a test file for gzip decompression.")
    return input_file

def test_successful_decompression(sample_gzip_file, tmp_path):
    """Test successful gzip file decompression."""
    output_path = tmp_path / "sample.txt"
    result = decompress_gzip_file(str(sample_gzip_file), str(output_path))
    
    assert os.path.exists(output_path)
    assert result == str(output_path)
    
    with open(output_path, 'rb') as f:
        content = f.read()
        assert content == b"This is a test file for gzip decompression."

def test_default_output_path(sample_gzip_file, tmp_path):
    """Test decompression with default output path."""
    default_output = str(sample_gzip_file)[:-3]  # Remove .gz
    result = decompress_gzip_file(str(sample_gzip_file))
    
    assert os.path.exists(default_output)
    assert result == default_output

def test_nonexistent_input_file(tmp_path):
    """Test handling of non-existent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_gzip_file(str(tmp_path / "nonexistent.txt.gz"))

def test_invalid_file_extension(tmp_path):
    """Test handling of file without .gz extension."""
    input_file = tmp_path / "sample.txt"
    with open(input_file, 'w') as f:
        f.write("Test content")
    
    with pytest.raises(ValueError):
        decompress_gzip_file(str(input_file))

def test_invalid_gzip_file(tmp_path):
    """Test handling of invalid gzip file."""
    invalid_gzip = tmp_path / "invalid.txt.gz"
    with open(invalid_gzip, 'wb') as f:
        f.write(b"Not a valid gzip file")
    
    with pytest.raises(ValueError):
        decompress_gzip_file(str(invalid_gzip))