from collections import deque
import pprint as pp
from copy import deepcopy

node, edge, pos = map(int,input().split())

graph = [0] + [[] for _ in range(node)]
visited = deepcopy(graph) # 그래프와 영향을 받지 않는 새로운 그래프.

for _ in range(edge):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

# --- dfs (LIFO)
stack = [pos]
visited = [pos]

# method 1)
# while stack:
#     cur = stack.pop()
#     if graph[cur]: #갈 수 있는 지점이 있으면
#         for i in graph[cur]:
#             if i not in visited: 
#                 visited.append(i)
#                 stack.append(i)
#                 break

# method 2)
# dfs_recursive
def dfs(v):
    if graph[v]:
        for i in graph[v]:
            if i not in visited :
                visited.append(i)
                dfs(i)
                break
                
            
# --- bfs (FIFO)
queue = deque([pos])
path = [pos]

while queue:
    cur = queue.popleft()
    if graph[cur]: # 갈 수 있는 노드가 있다면
        for i in graph[cur]:
            if i not in path:
                queue.append(i)
                path.append(i)

dfs(pos)

print(visited)
print(path)