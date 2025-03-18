def log_error(message):
    """
    Log an error message to the console.

    Args:
        message (str): The error message to be logged.

    Raises:
        TypeError: If the message is not a string.
    """
    # Validate input is a string
    if not isinstance(message, str):
        raise TypeError("Error message must be a string")
    
    # Print error message to console with ERROR prefix
    print(f"ERROR: {message}")