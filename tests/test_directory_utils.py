import os
import tempfile
import pytest
from src.directory_utils import delete_directory

def test_delete_directory_success():
    """Test successful directory deletion."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files and subdirectories
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('test')
        with open(os.path.join(temp_dir, 'subdir', 'file2.txt'), 'w') as f:
            f.write('another test')
        
        # Delete the directory
        delete_directory(temp_dir)
        
        # Verify directory is deleted
        assert not os.path.exists(temp_dir)

def test_delete_nonexistent_directory():
    """Test deletion of a non-existent directory raises FileNotFoundError."""
    with tempfile.TemporaryDirectory() as parent_dir:
        non_existent_path = os.path.join(parent_dir, 'doesnotexist')
        with pytest.raises(FileNotFoundError):
            delete_directory(non_existent_path)

def test_delete_file_instead_of_directory():
    """Test attempting to delete a file instead of a directory raises ValueError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'testfile.txt')
        with open(file_path, 'w') as f:
            f.write('test')
        
        with pytest.raises(ValueError):
            delete_directory(file_path)

def test_delete_empty_directory():
    """Test deleting an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        empty_subdir = os.path.join(temp_dir, 'empty_subdir')
        os.makedirs(empty_subdir)
        
        delete_directory(empty_subdir)
        
        # Verify directory is deleted
        assert not os.path.exists(empty_subdir)