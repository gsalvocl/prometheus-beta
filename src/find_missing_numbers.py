def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers in the array.
    
    Raises:
        ValueError: If the input is not a valid list of positive integers.
    """
    # Validate input
    if not arr:
        return []
    
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] < arr[-1]
    
    # Find the start and end of the range
    if is_ascending:
        start = min(arr)
        end = max(arr)
    else:
        start = max(arr)
        end = min(arr)
        arr = sorted(arr, reverse=True)
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing = []
    current_range = range(start, end + 1) if is_ascending else range(start, end - 1, -1)
    
    for num in current_range:
        if num not in num_set:
            missing.append(num)
    
    return missing