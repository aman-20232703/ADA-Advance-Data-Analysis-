"""
Prim’s algorithm is a Greedy algorithm like Kruskal's algorithm. This algorithm always starts with a single node and moves through several adjacent nodes, in order to explore all of the connected edges along the way.

The algorithm starts with an empty spanning tree.
The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included.
At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of the edge to the set containing MST. 
A group of edges that connects two sets of vertices in a graph is called Articulation Points (or Cut Vertices) in graph theory. So, at every step of Prim’s algorithm, find a cut, pick the minimum weight edge from the cut, and include this vertex in MST Set (the set that contains already included vertices).

Working of the Prim's Algorithm
Step 1: Determine an arbitrary vertex as the starting vertex of the MST. We pick 0 in the below diagram.
Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
Step 3: Find edges connecting any tree vertex with the fringe vertices.
Step 4: Find the minimum among these edges.
Step 5: Add the chosen edge to the MST. Since we consider only the edges that connect fringe vertices with the rest, we never get a cycle.
Step 6: Return the MST and exit
"""

import heapq

def prim(n,adj):
    visited = [False] * n
    min_heap = [(0,0)]  #weight,node
    cost = 0
    mst =[]

    while min_heap:
        weight,u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        cost += weight

        for v,w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap,(w,v))
                mst.append((u,v,w))

    return mst,cost

adj = {
    0: [(1, 4), (2, 3)],
    1: [(0, 4), (2, 1), (3, 2)],
    2: [(0, 3), (1, 1), (3, 4)],
    3: [(1, 2), (2, 4)]
}
n = 4

mst, cost = prim(n, adj)
print("MST edges:", mst)
print("Total cost:", cost)