def solve_knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing the maximum value and the selected items
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not weights or not values:
        return 0, []
    
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")
    
    if any(w < 0 for w in weights) or any(v < 0 for v in values):
        raise ValueError("Weights and values must be non-negative")
    
    if capacity < 0:
        raise ValueError("Knapsack capacity must be non-negative")
    
    n = len(weights)
    
    # Initialize dynamic programming table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dynamic programming table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]], 
                    dp[i-1][w]
                )
            else:
                # Current item too heavy, skip it
                dp[i][w] = dp[i-1][w]
    
    # Track selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
    
    # Return max value and list of selected item indices
    return dp[n][capacity], list(reversed(selected_items))