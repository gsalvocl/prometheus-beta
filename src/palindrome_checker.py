import unicodedata

def is_palindrome(s: str) -> bool:
    """
    Determine if the given string is a palindrome.
    
    A palindrome reads the same forward and backward, ignoring spaces, 
    punctuation, and case sensitivity.
    
    Args:
        s (str): The input string to check for palindrome property
    
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("Was it a car or a cat I saw?")
        True
    """
    # Normalize Unicode characters and remove accents
    normalized_str = ''.join(
        char.lower() for char in unicodedata.normalize('NFKD', s)
        if unicodedata.category(char)[0] not in ['P', 'Z', 'C']  # Exclude punctuation, separators, control chars
    )
    
    # Check if the normalized string is equal to its reverse
    return normalized_str == normalized_str[::-1]