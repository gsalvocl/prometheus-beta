def find_smallest_list_sum(list1, list2):
    """
    Find the smallest possible sum between two lists of integers.
    
    Args:
        list1 (list): First list of integers
        list2 (list): Second list of integers
    
    Returns:
        int: The smallest possible sum that can be created by taking one element 
             from each list
    
    Raises:
        ValueError: If either input is not a list or is empty
        TypeError: If lists contain non-integer elements
    """
    # Validate input lists
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise ValueError("Inputs must be lists")
    
    if len(list1) == 0 or len(list2) == 0:
        raise ValueError("Input lists cannot be empty")
    
    # Validate list contents are integers
    try:
        list1 = [int(x) for x in list1]
        list2 = [int(x) for x in list2]
    except (ValueError, TypeError):
        raise TypeError("All list elements must be integers or convertible to integers")
    
    # Find the smallest possible sum by taking the minimum element from each list
    smallest_sum = min(list1) + min(list2)
    
    return smallest_sum