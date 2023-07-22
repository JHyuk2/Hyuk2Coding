'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

from collections import deque

com = int(input())
n = int(input())
graph = [[] for _ in range(com+1)]
check = [0 for _ in range(com+1)]
queue = deque([1])

for _ in range(n):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 1번째 컴퓨터로부터 시작
while queue:
    temp = queue.popleft()
    
    # 이미 들렀던 곳이면 건너가라
    if check[temp] :
        continue
    
    # 들렀던 곳이 아니면
    else:
        check[temp] = 1
        queue += graph[temp]

print(sum(check)-1)