def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    The Z algorithm finds all occurrences of a pattern within a text in O(n+m) time complexity.
    
    Args:
        text (str): The main text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices of all pattern occurrences in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are empty strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Concatenate pattern and text with a delimiter
    combined = pattern + '$' + text
    
    # Compute Z array
    z = [0] * len(combined)
    left, right = 0, 0
    
    # Z array computation
    for k in range(1, len(combined)):
        # If k is outside the current Z-box, compute Z[k] from scratch
        if k > right:
            left = right = k
            while right < len(combined) and combined[right - left] == combined[right]:
                right += 1
            z[k] = right - left
            right -= 1
        else:
            # k is inside the Z-box
            k1 = k - left
            
            # If the value does not stretch to the right end of the Z-box,
            # just copy the value
            if z[k1] < right - k + 1:
                z[k] = z[k1]
            else:
                # Otherwise, we need to do some more comparisons
                left = k
                while right < len(combined) and combined[right - left] == combined[right]:
                    right += 1
                z[k] = right - left
                right -= 1
    
    # Find matches
    matches = []
    for i in range(len(pattern) + 1, len(combined)):
        if z[i] == len(pattern):
            matches.append(i - len(pattern) - 1)
    
    return matches