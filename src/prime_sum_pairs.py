def is_prime(num):
    """
    Check if a given number is prime.
    
    Args:
        num (int): Number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def unique_prime_sum_pairs(n):
    """
    Generate a list of unique prime numbers that can be obtained 
    by summing pairs of numbers from the range [1, n].
    
    Args:
        n (int): Upper bound of the range to generate pairs from.
    
    Returns:
        list: Sorted list of unique prime numbers from pair sums.
    
    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    # Collect all possible pair sums
    pair_sums = set()
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            pair_sums.add(i + j)
    
    # Filter and collect unique prime sums
    prime_sums = sorted(set(sum_val for sum_val in pair_sums if is_prime(sum_val)))
    
    return prime_sums