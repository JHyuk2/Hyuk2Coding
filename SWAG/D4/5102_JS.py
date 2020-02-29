# 노드의 거리
def node(queue, distance):
    global distances_list
    if G in queue:
        print(visited, queue)
        return distance
    else:
        for q in queue:
            if not visited[q]:
                visited[q] = 1
                if node(graph_dict[q], distance+1):
                    distances_list.append(node(graph_dict[q], distance+1))
                visited[q] = 0
    
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V = 노드, E = 간선
    graph_dict = {}
    for i in range(1, V+1):
        graph_dict[i] =[]
    # E개의 간선
    for _ in range(E):
        V1, V2 = map(int, input().split())
        graph_dict[V1].append(V2)
        graph_dict[V2].append(V1)
    S, G = map(int, input().split()) # S = 시작 노드, G = 도착 노드
    result = 0
    distances_list = []
    visited = [0]*(V+1)
    visited[S] = 1

    node(graph_dict[S], 1)
    if distances_list:
        result = min(distances_list)
    print(distances_list)
    print(f'#{tc} {result}')