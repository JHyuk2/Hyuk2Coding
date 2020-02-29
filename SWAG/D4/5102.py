# 노드의 거리
'''
3   --- tc
6 5 --- V, E
1 4 --- e1
1 3 --- e2
2 3 --- e3
2 5 --- e4
4 6 --- e5
1 6 --- start, goal
'''

# # 1) 인접리스트 (graph)와 start, goal을 받아서 거리 계산하기.

def bfs_paths(graph, start, goal):
    # 출발점, 현재까지 진행
    queue = [(start, [start])]
    result = []

    while queue:
        # bfs 진행
        n, path = queue.pop(0)

        if n == goal:
            result.append(len(path) -1) 
            print(path)
        else:
            for m in graph[n]:
                if m not in path:
                    queue.append((m, path + [m]))
    return result

# # 2) 인접 리스트 만들기
 
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}     
    # 무방향 그래프 - 양방향 인접 리스트 만들기
    # 1) Vertex 수 만큼 딕셔너리 크기 잡아주기.
    for i in range(1, V+1):
        graph[i] = []
    # 2) 리스트 채워주기
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 3) start, goal
    start, goal = map(int, input().split())

    result = min(bfs_paths(graph, start, goal))
    print(f'#{tc} {result}')