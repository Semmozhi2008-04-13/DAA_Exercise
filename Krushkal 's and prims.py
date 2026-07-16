import heapq
import time

# ==========================================
# 1. KRUSKAL'S ALGORITHM IMPLEMENTATION
# ==========================================
class UnionFind:
    def __init__(self, vertices):
        # Initialize parent pointers where each vertex is its own set
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        # Find path compression
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        
        if root1 != root2:
            # Attach smaller rank tree under root of higher rank tree
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def kruskal(vertices, edges):
    # Sort all edges by weight in non-decreasing order
    sorted_edges = sorted(edges, key=lambda item: item[2])
    uf = UnionFind(vertices)
    mst = []
    
    print("\n--- Kruskal's Processing Steps ---")
    for u, v, w in sorted_edges:
        # Check if including this edge creates a cycle
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            print(f"[Kruskal] Added Edge: {u} - {v} | Weight: {w}")
            
            if len(mst) == len(vertices) - 1:
                break
                
    return mst

# ==========================================
# 2. PRIM'S ALGORITHM IMPLEMENTATION
# ==========================================
def prim(vertices, edges, start_vertex):
    # Build an adjacency list mapping for easy neighbor lookups
    adj_list = {v: [] for v in vertices}
    for u, v, w in edges:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w)) # Graph is undirected
        
    key = {v: float('inf') for v in vertices}
    parent = {v: -1 for v in vertices}
    in_mst = {v: False for v in vertices}
    
    key[start_vertex] = 0
    # Min-priority queue storing elements as (weight, vertex)
    pq = [(0, start_vertex)]
    mst_edges = []
    
    print("\n--- Prim's Processing Steps ---")
    while pq:
        w, u = heapq.heappop(pq)
        
        if in_mst[u]:
            continue
            
        in_mst[u] = True
        # If it's not the root vertex, add to the record trace
        if parent[u] != -1:
            mst_edges.append((parent[u], u, w))
            print(f"[Prim] Added Edge: {parent[u]} - {u} | Weight: {w}")
            
        for v, weight in adj_list[u]:
            if not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))
                
    return mst_edges

# ==========================================
# INTERACTIVE DRIVER EXECUTION CODE
# ==========================================
if __name__ == "__main__":
    print("=== CS5303 DAA Lab | MST Algorithms ===")
    print("Kruskal's vs. Prim's Minimum Spanning Tree Analysis\n")
    
    # 1. Interactive Inputs
    vertices_input = input("Enter all Vertices separated by space (e.g., A B C D): ").split()
    
    print("\nEnter your edges in the format: u v weight (Type 'done' to finish)")
    print("Example line: A B 4")
    
    edges = []
    while True:
        edge_str = input("Edge: ").strip()
        if edge_str.lower() == 'done':
            break
        try:
            u, v, w = edge_str.split()
            edges.append((u, v, int(w)))
        except ValueError:
            print("Invalid input format! Use: vertex1 vertex2 weight")
            
    if not vertices_input or not edges:
        print("Error: Graph missing vertices or edges.")
        exit()
        
    start_node = vertices_input[0]
    
    # 2. Performance Tracking Profiling
    # Kruskal Execution
    start_time = time.perf_counter()
    kruskal_mst = kruskal(vertices_input, edges)
    kruskal_duration = (time.perf_counter() - start_time) * 1000
    
    # Prim Execution
    start_time = time.perf_counter()
    prim_mst = prim(vertices_input, edges, start_node)
    prim_duration = (time.perf_counter() - start_time) * 1000
    
    # 3. Formatted Lab Report Output Table
    print("\n================ COMPILATION SUMMARY ================")
    print(f"Kruskal's MST Total Cost: {sum(w for _, _, w in kruskal_mst)}")
    print(f"Prim's MST Total Cost:    {sum(w for _, _, w in prim_mst)}")
    print("-" * 53)
    print(f"{'Algorithm':<15} | {'Execution Time (ms)':<20} | {'Edges Selected'}")
    print("-" * 53)
    print(f"{'Kruskal':<15} | {kruskal_duration:<20.4f} | {len(kruskal_mst)}")
    print(f"{'Prim':<15} | {prim_duration:<20.4f} | {len(prim_mst)}")
    print("=====================================================")
