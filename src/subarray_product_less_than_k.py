def count_subarrays_with_product_less_than_k(nums, k):
    """
    Count the number of subarrays where the product of elements is less than k.
    
    Args:
        nums (list): Input array of integers
        k (int): Product threshold
    
    Returns:
        int: Number of subarrays with product less than k
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    # Handle edge cases
    if k <= 1:
        return 0
    
    count = 0
    n = len(nums)
    
    for i in range(n):
        product = 1
        for j in range(i, n):
            # Multiply the current element to the running product
            product *= nums[j]
            
            # If product becomes >= k, stop this inner loop
            if product >= k:
                break
            
            # If product is less than k, increment count
            count += 1
    
    return count