def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.

    Args:
        arr (list): A sorted list of integers.

    Returns:
        list: A list of integers representing the missing numbers in the range.

    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input array is not sorted in ascending order.

    Examples:
        >>> find_missing_numbers([1, 3, 5])
        [2, 4]
        >>> find_missing_numbers([1, 10])
        [2, 3, 4, 5, 6, 7, 8, 9]
        >>> find_missing_numbers([5, 5, 7])
        [6]
    """
    # Validate input
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Check if the array is sorted in ascending order
    if any(arr[i] > arr[i+1] for i in range(len(arr)-1)):
        raise ValueError("Input array must be sorted in ascending order")
    
    # Find the range of numbers
    min_num = arr[0]
    max_num = arr[-1]
    
    # Create a set of the input array for efficient lookup
    num_set = set(arr)
    
    # Find missing numbers
    missing_numbers = [
        num for num in range(min_num + 1, max_num) 
        if num not in num_set
    ]
    
    return missing_numbers