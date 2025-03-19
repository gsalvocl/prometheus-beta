def two_sum(nums, target):
    """
    Find two indices in an array that add up to a target sum.

    Args:
        nums (list): A list of integers to search through
        target (int): The target sum to find

    Returns:
        list: A list of two indices where the corresponding values add up to the target
              Returns an empty list if no such indices are found

    Raises:
        TypeError: If input is not a list or target is not an integer
        ValueError: If list contains non-integer elements
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check that all elements are integers
    if not all(isinstance(num, int) for num in nums):
        raise ValueError("All list elements must be integers")

    # Create a dictionary to store complement values and their indices
    complement_dict = {}

    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # If the complement exists in the dictionary, we found a match
        if complement in complement_dict:
            return [complement_dict[complement], i]
        
        # Store the current number's index
        complement_dict[num] = i
    
    # If no solution is found, return an empty list
    return []