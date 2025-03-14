def reverse_string_in_place(s):
    """
    Reverse a string in-place with O(1) space complexity.
    
    This function modifies the input string by reversing its characters 
    without creating a new string, optimizing for space complexity.
    
    Args:
        s (list): A mutable sequence of characters (list of chars)
    
    Raises:
        TypeError: If input is not a mutable sequence
    
    Time Complexity: O(n), where n is the length of the string
    Space Complexity: O(1), as the reversal is done in-place
    
    Examples:
        >>> arr = list('hello')
        >>> reverse_string_in_place(arr)
        >>> arr
        ['o', 'l', 'l', 'e', 'h']
    """
    # Check if input is a mutable sequence
    if not hasattr(s, '__setitem__'):
        raise TypeError("Input must be a mutable sequence like a list")
    
    # Two-pointer approach for in-place reversal
    left, right = 0, len(s) - 1
    
    while left < right:
        # Swap characters from both ends
        s[left], s[right] = s[right], s[left]
        
        # Move pointers towards center
        left += 1
        right -= 1
    
    return s  # Optional return, but modifies input in-place