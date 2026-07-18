import heapq

def dijkstra(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[source] = 0
    
    pq = [(0, source)]  # (distance, vertex)
    visited = set()
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if u in visited:
            continue
        visited.add(u)
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
                
    return dist, prev

def reconstruct_path(prev, source, target):
    path = []
    node = target
    
    while node is not None:
        path.append(node)
        node = prev[node]
        
    path.reverse()
    
    if len(path) > 0 and path[0] == source:
        return path
    return []

# --- Graph Definition ---
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: [(4, 3)],
    4: [(5, 2)],
    5: []
}

# --- Execution ---
source = 0
dist, prev = dijkstra(graph, source)

# --- Simple Output Printing ---
print("Shortest paths from vertex", source)
print("Vertex | Distance | Path")
print("-" * 30)

for v in range(len(graph)):
    path = reconstruct_path(prev, source, v)
    
    # Format the path array into a readable string (e.g., 0 -> 2 -> 1)
    if path:
        path_str = " -> ".join(map(str, path))
    else:
        path_str = "No path"
        
    # Handle infinite/unreachable distance cases cleanly
    if dist[v] == float('inf'):
        d = "INF"
    else:
        d = dist[v]
        
    print(f"  {v}    |    {d}     | {path_str}")
