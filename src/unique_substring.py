def find_longest_substring(s: str) -> str:
    """
    Find the longest substring with unique characters.

    Args:
        s (str): Input string to search for the longest unique substring.

    Returns:
        str: The longest substring where each character appears only once.
             If multiple such substrings exist with the same length, 
             returns the first one encountered.
             Returns an empty string if input is empty or None.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    # Strict type checking
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or single character, return it
    if len(s) <= 1:
        return s
    
    # Sliding window approach to find longest unique substring
    longest_substring = ""
    start = 0
    
    for end in range(len(s)):
        # Create substring from start to current end
        current_substring = s[start:end+1]
        
        # If current substring has all unique characters
        if len(set(current_substring)) == len(current_substring):
            # Update longest substring if current is longer
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
        else:
            # Advance start pointer to maintain unique characters
            while len(set(s[start:end+1])) < end - start + 1:
                start += 1
    
    return longest_substring