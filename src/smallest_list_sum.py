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
    
    # Print all possible sums for debugging
    possible_sums = []
    for num1 in list1:
        for num2 in list2:
            possible_sums.append(num1 + num2)
    
    print(f"Possible sums: {possible_sums}")
    
    # Find the smallest possible sum by checking all possible sums
    return min(possible_sums)