import os
import stat

def get_file_permissions(file_path):
    """
    Retrieve the file permissions for a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        dict: A dictionary containing file permission details with the following keys:
            - 'numeric': Numeric representation of file permissions (e.g., 0o755)
            - 'readable': Human-readable permission string (e.g., 'rwxr-xr-x')
            - 'owner_read': Boolean indicating if owner has read permission
            - 'owner_write': Boolean indicating if owner has write permission
            - 'owner_execute': Boolean indicating if owner has execute permission
            - 'group_read': Boolean indicating if group has read permission
            - 'group_write': Boolean indicating if group has write permission
            - 'group_execute': Boolean indicating if group has execute permission
            - 'others_read': Boolean indicating if others have read permission
            - 'others_write': Boolean indicating if others have write permission
            - 'others_execute': Boolean indicating if others have execute permission

    Raises:
        FileNotFoundError: If the file does not exist
        PermissionError: If the file cannot be accessed
    """
    try:
        # Get file stats
        file_stats = os.stat(file_path)
        mode = file_stats.st_mode

        # Create permission dictionary
        permissions = {
            'numeric': oct(mode & 0o777),
            'readable': _convert_to_readable_permissions(mode),
            'owner_read': bool(mode & stat.S_IRUSR),
            'owner_write': bool(mode & stat.S_IWUSR),
            'owner_execute': bool(mode & stat.S_IXUSR),
            'group_read': bool(mode & stat.S_IRGRP),
            'group_write': bool(mode & stat.S_IWGRP),
            'group_execute': bool(mode & stat.S_IXGRP),
            'others_read': bool(mode & stat.S_IROTH),
            'others_write': bool(mode & stat.S_IWOTH),
            'others_execute': bool(mode & stat.S_IXOTH)
        }

        return permissions

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")

def _convert_to_readable_permissions(mode):
    """
    Convert numeric file mode to a readable permission string.

    Args:
        mode (int): Numeric file mode

    Returns:
        str: Readable permission string (e.g., 'rwxr-xr-x')
    """
    readable = '-' * 9
    perms = [
        (stat.S_IRUSR, 0), (stat.S_IWUSR, 1), (stat.S_IXUSR, 2),
        (stat.S_IRGRP, 3), (stat.S_IWGRP, 4), (stat.S_IXGRP, 5),
        (stat.S_IROTH, 6), (stat.S_IWOTH, 7), (stat.S_IXOTH, 8)
    ]

    for perm, index in perms:
        if mode & perm:
            readable = readable[:index] + 'rwx'[index % 3] + readable[index+1:]

    return readable