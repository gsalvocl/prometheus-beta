def log_bold_message(message):
    """
    Log a message in bold text to the console.
    
    Args:
        message (str): The message to be logged in bold.
    
    Raises:
        TypeError: If the input is not a string.
        ValueError: If the message is empty.
    
    Returns:
        str: The bolded message (ANSI escaped for terminal output).
    """
    # Type checking
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    # Empty message validation
    if not message.strip():
        raise ValueError("Message cannot be empty")
    
    # ANSI escape codes for bold text
    BOLD_START = '\033[1m'
    BOLD_END = '\033[0m'
    
    # Bold message with ANSI escapes
    bold_message = f"{BOLD_START}{message}{BOLD_END}"
    
    # Print the message
    print(bold_message)
    
    return bold_message