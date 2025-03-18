from typing import List, Tuple
from collections import deque

def find_shortest_grid_path(grid: List[List[str]]) -> List[Tuple[int, int]]:
    """
    Find the shortest path from top-left to bottom-right corner of a grid.
    
    Args:
        grid (List[List[str]]): A 2D grid where:
            '.' represents an empty cell
            'O' represents a blocking cell
            '#' (optional, for final path visualization)
    
    Returns:
        List[Tuple[int, int]]: A list of coordinates representing the shortest path
        
    Raises:
        ValueError: If the grid is invalid or no path exists
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    rows, cols = len(grid), len(grid[0])
    
    # Check if start or end is blocked
    if grid[0][0] == 'O' or grid[rows-1][cols-1] == 'O':
        raise ValueError("Start or end cell is blocked")
    
    # Possible movement directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Track visited cells and paths
    visited = [[False] * cols for _ in range(rows)]
    parent = [[None] * cols for _ in range(rows)]
    
    # BFS queue
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        current_row, current_col = queue.popleft()
        
        # Reached bottom-right corner
        if current_row == rows - 1 and current_col == cols - 1:
            # Reconstruct path
            path = []
            while current_row is not None:
                path.append((current_row, current_col))
                current_row, current_col = parent[current_row][current_col] or (None, None)
            return list(reversed(path))
        
        # Try all four directions
        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc
            
            # Check bounds, not visited, and not blocked
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                not visited[new_row][new_col] and 
                grid[new_row][new_col] != 'O'):
                
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[new_row][new_col] = (current_row, current_col)
    
    # No path found
    raise ValueError("No path exists between start and end")