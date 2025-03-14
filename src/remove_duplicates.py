def remove_duplicates(numbers):
    """
    Remove duplicate values from a list of integers while preserving the original order.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list with duplicates removed, maintaining the original order.

    Raises:
        TypeError: If the input is not a list.
        
    Time Complexity: O(n), where n is the length of the input list
    Space Complexity: O(n) to store unique elements
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    # Use a set to track seen elements while preserving order
    seen = set()
    unique_list = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_list.append(num)

    return unique_list