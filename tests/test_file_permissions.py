import os
import pytest
import stat
from src.file_permissions import get_file_permissions

def test_get_file_permissions_existing_file(tmp_path):
    # Create a test file with specific permissions
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Test content")
    test_file.chmod(0o755)  # rwxr-xr-x

    # Get permissions
    permissions = get_file_permissions(str(test_file))

    # Verify the returned dictionary structure and values
    assert isinstance(permissions, dict)
    assert permissions['numeric'] == '0o755'
    assert permissions['readable'] == 'rwxr-xr-x'
    
    # Check individual permissions
    assert permissions['owner_read'] == True
    assert permissions['owner_write'] == True
    assert permissions['owner_execute'] == True
    assert permissions['group_read'] == True
    assert permissions['group_execute'] == True
    assert permissions['group_write'] == False
    assert permissions['others_read'] == True
    assert permissions['others_execute'] == True
    assert permissions['others_write'] == False

def test_get_file_permissions_nonexistent_file(tmp_path):
    # Attempt to get permissions for a non-existent file
    nonexistent_file = tmp_path / "nonexistent.txt"
    
    with pytest.raises(FileNotFoundError):
        get_file_permissions(str(nonexistent_file))

def test_various_permission_combinations(tmp_path):
    # Test various permission combinations
    permission_cases = [
        (0o600, 'rw-------'),  # Owner read-write
        (0o400, 'r--------'),  # Owner read-only
        (0o200, '-w-------'),  # Owner write-only
        (0o100, '--x------'),  # Owner execute-only
        (0o644, 'rw-r--r--'),  # Standard file permissions
        (0o755, 'rwxr-xr-x'),  # Standard executable
    ]

    for numeric_perm, expected_readable in permission_cases:
        test_file = tmp_path / f"perm_{numeric_perm}.txt"
        test_file.write_text("Test")
        test_file.chmod(numeric_perm)

        permissions = get_file_permissions(str(test_file))
        
        assert permissions['numeric'] == f'0o{numeric_perm:o}'
        assert permissions['readable'] == expected_readable