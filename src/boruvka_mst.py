from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to efficiently track connected components.
    """
    def __init__(self, vertices: int):
        """
        Initialize the Disjoint Set with given number of vertices.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item: int) -> int:
        """
        Find the root of the set that an item belongs to with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: int, y: int) -> bool:
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful (sets were different), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

def boruvka_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree.
    
    :param vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is (u, v, weight)
    :return: List of edges in the minimum spanning tree
    :raises ValueError: If graph is not connected or invalid input
    """
    # Validate input
    if vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        raise ValueError("Graph must have at least one edge")

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Track number of components
    components = vertices
    
    while components > 1:
        # Track cheapest edges for each component in this round
        cheapest = [None] * vertices
        
        # Find cheapest edge for each component
        for u, v, weight in edges:
            # Find roots of the current edge's vertices
            set_u = ds.find(u)
            set_v = ds.find(v)
            
            # Skip if in same set (same component)
            if set_u == set_v:
                continue
            
            # Update cheapest edge for components if applicable
            if cheapest[set_u] is None or weight < cheapest[set_u][2]:
                cheapest[set_u] = (u, v, weight)
            
            if cheapest[set_v] is None or weight < cheapest[set_v][2]:
                cheapest[set_v] = (u, v, weight)
        
        # Add cheapest edges to MST
        for cheap_edge in cheapest:
            if cheap_edge is not None:
                u, v, weight = cheap_edge
                
                # If not in same set, union and add to MST
                if ds.union(u, v):
                    mst.append((u, v, weight))
                    components -= 1
        
        # If no edges were added, graph is not connected
        if not mst:
            raise ValueError("Graph is not connected")
    
    return mst