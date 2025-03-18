def spaghetti_sort(arr):
    """
    Implement the spaghetti sort algorithm.
    
    Spaghetti sort (also known as the selection sort algorithm) works by:
    1. Finding the minimum element in the unsorted portion of the list
    2. Swapping it with the first unsorted element
    3. Repeating until the entire list is sorted
    
    Args:
        arr (list): A list of comparable elements to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy of the input list to avoid modifying the original
    sorted_arr = arr.copy()
    
    # Perform spaghetti sort
    for i in range(len(sorted_arr)):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, len(sorted_arr)):
            # Compare and update minimum index
            try:
                if sorted_arr[j] < sorted_arr[min_idx]:
                    min_idx = j
            except TypeError:
                raise ValueError("List contains elements that cannot be compared")
        
        # Swap the found minimum element with the first unsorted element
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr