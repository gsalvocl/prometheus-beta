import os
import shutil

def delete_directory(path):
    """
    Delete a directory and all its contents.

    Args:
        path (str): Path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        PermissionError: If there are insufficient permissions to delete the directory.
        ValueError: If the path is not a directory.
    """
    # Validate input
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    if not os.path.isdir(path):
        raise ValueError(f"Path is not a directory: {path}")
    
    try:
        # Use shutil.rmtree for recursive deletion
        shutil.rmtree(path)
    except PermissionError:
        raise PermissionError(f"Insufficient permissions to delete directory: {path}")
    except Exception as e:
        raise RuntimeError(f"Error deleting directory: {e}")