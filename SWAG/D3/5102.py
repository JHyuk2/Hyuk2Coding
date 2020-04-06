# 노드의 거리

'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
1 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
'''

for tc in range(int(input())):
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

