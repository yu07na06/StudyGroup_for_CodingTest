# 동작 X...
# 디버깅 필요...

N,M,V=map(int,input().split())
graph=[[0]*(N+1) for i in range(N+1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = graph[node2][node1] = 1


def BFS(graph, start_node):
    q = []
    visited = []

    q.append(start_node)
    
    while q:

        node = q.pop(0)
        if node not in visited:
            visited.append(node)
            q.extend(graph[node])
    
    return visited

def DFS(graph, start_node):
    stack = []
    visited = []

    stack.append(start_node)
    while stack:
        node = stack.pop()
        print(node)
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited

print(DFS(V, '1'))
print(BFS(V, '1'))

# graph = {
#     'A': ['B'],
#     'B': ['A', 'C', 'H'],
#     'C': ['B', 'D'],
#     'D': ['C', 'E', 'G'],
#     'E': ['D', 'F'],
#     'F': ['E'],
#     'G': ['D'],
#     'H': ['B', 'I', 'J', 'M'],
#     'I': ['H'],
#     'J': ['H', 'K'],
#     'K': ['J', 'L'],
#     'L': ['K'],
#     'M': ['H']
# }
# print(BFS(graph, 'A'))
# print(DFS(graph, 'A'))

