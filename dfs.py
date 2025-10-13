graph={
    'a':['b','d'],
    'b':[],
    'c':[],
    'd':['e','g'],
    'e':['c'],
    'f':[],
    'g':['f']
}

# using BFS
def BFS(graph,source):
    queue=[]
    queue.append(source)
    
    while queue:
        node=queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            queue.append(neighbour)
            
print("BFS Graph:")
BFS(graph,'a')
print("\n")

# using DFS
def DFS(graph, source):
    stack=[]
    stack.append(source)
    
    while stack:
        node=stack.pop(-1)
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)
            
print("DFS Graph:")
DFS(graph,'a')
print("\n")



queue=['a']
list=[]
    
while queue:
    node=queue.pop(0)
    list.append(node)
    for neighbour in graph[node]:
        queue.append(neighbour)
            
print("BFS Graph:")
print(list)
print("\n")


# using Adjacency matrix
def add_edge(mat,i,j):
    mat[i][j]=1
    mat[j][i]=1
    
def display(mat):
    for row in mat:
        print(" ".join(map(str,row)))
        
if __name__ == "__main__":
    v=4
    mat=[[0]*v for _ in range(v)]
    
    row=[
    add_edge(mat,1,2),
    add_edge(mat,0,1),
    add_edge(mat,2,1),
    add_edge(mat,0,2),
    ]
print("Adjacency matrix:")
display(mat)

# graph colouring
from collections import deque
def is_bipartite(graph):
    color = {node: -1 for node in graph}
    
    for start in graph:
        if color[start] == -1:  # not yet colored
            queue = deque([start])
            color[start] = 0  # start with color 0
            
            while queue:
                node = queue.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        queue.append(neighbour)
                    elif color[neighbour] == color[node]:
                        return False, {}
    
    return True, color

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

is_bip, coloring = is_bipartite(graph)

if is_bip:
    print(" Graph is Bipartite")
    print("Coloring:", coloring)
else:
    print("Graph is NOT Bipartite")




# ✅ Graph is Bipartite
# Coloring: {0: 0, 1: 1, 2: 0, 3: 1}
