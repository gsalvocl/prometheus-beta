import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set (Union-Find) data structure."""
    ds = DisjointSet(5)
    
    # Initial state: each element in its own set
    assert ds.find(0) != ds.find(1)
    assert ds.find(2) != ds.find(3)
    
    # Union sets
    assert ds.union(0, 1) == True  # First union should succeed
    assert ds.union(0, 1) == False  # Second union should fail (same set)
    
    # Elements in same set after union
    assert ds.find(0) == ds.find(1)

def test_boruvka_mst_simple_graph():
    """Test Boruvka's algorithm on a simple connected graph."""
    # Simple graph with 4 vertices and 5 edges
    vertices = 4
    edges = [
        (0, 1, 10),   # Edge between 0 and 1 with weight 10
        (0, 2, 6),    # Edge between 0 and 2 with weight 6
        (0, 3, 5),    # Edge between 0 and 3 with weight 5
        (1, 2, 3),    # Edge between 1 and 2 with weight 3
        (2, 3, 4)     # Edge between 2 and 3 with weight 4
    ]
    
    mst = boruvka_mst(vertices, edges)
    
    # Expected total weight of MST
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 13
    
    # Expected MST should have (vertices - 1) edges
    assert len(mst) == 3

def test_boruvka_mst_complex_graph():
    """Test Boruvka's algorithm on a more complex connected graph."""
    vertices = 6
    edges = [
        (0, 1, 4), (0, 2, 3), (1, 2, 1),
        (1, 3, 2), (2, 3, 5), (2, 4, 6),
        (3, 4, 7), (3, 5, 2), (4, 5, 4)
    ]
    
    mst = boruvka_mst(vertices, edges)
    
    # Expected total weight of MST
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 12
    
    # Expected MST should have (vertices - 1) edges
    assert len(mst) == 5

def test_boruvka_mst_error_cases():
    """Test error cases for Boruvka's algorithm."""
    # Test zero vertices
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(0, [(0, 1, 1)])
    
    # Test negative vertices
    with pytest.raises(ValueError, match="Number of vertices must be positive"):
        boruvka_mst(-1, [(0, 1, 1)])
    
    # Test empty edges list
    with pytest.raises(ValueError, match="Graph must have at least one edge"):
        boruvka_mst(3, [])
    
    # Test disconnected graph (should raise an error)
    with pytest.raises(ValueError, match="Graph is not connected"):
        boruvka_mst(4, [(0, 1, 1), (2, 3, 2)])