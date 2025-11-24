"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u-v, vertex u comes before v in the ordering.

Note: Topological Sorting for a graph is not possible if the graph is not a DAG.Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u-v, vertex u comes before v in the ordering.

Note: Topological Sorting for a graph is not possible if the graph is not a DAG.

Time Complexity: O(V+E). The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS.
"""

graph={
    5:[2,0],
    4:[0,1],
    3:[1],
    2:[3],
    1:[],
    0:[]
}

visited=set()
stack=[]

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbour in graph[node]:
        dfs(neighbour)
    stack.append(node)
        
for node in graph:
    dfs(node)
    
print(stack[::-1])
