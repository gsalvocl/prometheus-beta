def convert_to_alternating_dot_case(input_string):
    """
    Convert a string to alternating dot case.
    
    In alternating dot case, characters alternate between lowercase and uppercase, 
    with each character separated by a dot.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating dot case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> convert_to_alternating_dot_case("hello")
        'h.E.l.L.o'
        >>> convert_to_alternating_dot_case("python")
        'p.Y.t.H.o.N'
        >>> convert_to_alternating_dot_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Create alternating dot case
    result = []
    for i, char in enumerate(input_string):
        # Even indices (0, 2, 4...) are lowercase
        # Odd indices (1, 3, 5...) are uppercase
        if i % 2 == 0:
            result.append(char.lower())
        else:
            result.append(char.upper())
        
        # Add dot between characters, but not after the last character
        if i < len(input_string) - 1:
            result.append('.')
    
    return ''.join(result)