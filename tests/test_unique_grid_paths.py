import pytest
from src.unique_grid_paths import find_shortest_grid_path

def test_simple_grid_path():
    grid = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_grid_path(grid)
    assert len(path) == 5  # Minimum path is 5 steps in a 3x3 grid
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_grid_with_obstacles():
    grid = [
        ['.', '.', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_grid_path(grid)
    assert len(path) == 5
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)
    # Ensure path avoids obstacles
    for x, y in path[1:-1]:
        assert grid[x][y] != 'O'

def test_single_cell_grid():
    grid = [['.']]
    path = find_shortest_grid_path(grid)
    assert path == [(0, 0)]

def test_large_grid():
    grid = [['.'] * 10 for _ in range(10)]
    path = find_shortest_grid_path(grid)
    assert len(path) == 19  # Minimum path in 10x10 grid
    assert path[0] == (0, 0)
    assert path[-1] == (9, 9)

def test_grid_with_multiple_paths():
    grid = [
        ['.', '.', '.'],
        ['.', 'O', '.'],
        ['.', '.', '.']
    ]
    path = find_shortest_grid_path(grid)
    assert len(path) == 5
    assert path[0] == (0, 0)
    assert path[-1] == (2, 2)

def test_start_or_end_blocked():
    grid1 = [
        ['O', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    grid2 = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', 'O']
    ]
    
    with pytest.raises(ValueError, match="Start or end cell is blocked"):
        find_shortest_grid_path(grid1)
    
    with pytest.raises(ValueError, match="Start or end cell is blocked"):
        find_shortest_grid_path(grid2)

def test_no_path_exists():
    grid = [
        ['.', 'O', '.'],
        ['O', 'O', '.'],
        ['.', '.', '.']
    ]
    with pytest.raises(ValueError, match="No path exists"):
        find_shortest_grid_path(grid)

def test_empty_grid():
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        find_shortest_grid_path([])
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        find_shortest_grid_path([[]])