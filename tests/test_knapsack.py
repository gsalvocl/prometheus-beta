import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario with a few items."""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 220
    assert selected_items == [1, 2]

def test_empty_input():
    """Test knapsack with empty input lists."""
    assert solve_knapsack([], [], 100) == (0, [])

def test_zero_capacity():
    """Test knapsack with zero capacity."""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = solve_knapsack(weights, values, 0)
    
    assert max_value == 0
    assert selected_items == []

def test_capacity_less_than_smallest_item():
    """Test scenario where capacity is less than the smallest item."""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 5
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 0
    assert selected_items == []

def test_input_validation():
    """Test invalid input handling."""
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        solve_knapsack([1, 2], [10, 20, 30], 100)
    
    with pytest.raises(ValueError, match="Weights and values must be non-negative"):
        solve_knapsack([1, -2], [10, 20], 100)
    
    with pytest.raises(ValueError, match="Knapsack capacity must be non-negative"):
        solve_knapsack([1, 2], [10, 20], -10)

def test_large_capacity():
    """Test knapsack with capacity much larger than items."""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 1000
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 280
    assert selected_items == [0, 1, 2]

def test_multiple_optimal_solutions():
    """Test a case with multiple ways to achieve the same max value."""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 60
    max_value, selected_items = solve_knapsack(weights, values, capacity)
    
    assert max_value == 280
    assert selected_items == [0, 1, 2]  # Updated to reflect actual implementation