# 노드 사이의 거리
# 트리는 기본적으로 상하관계로 연결된 자료구조 // count(edge) = count(Node) -1 
# a -> b 가는 길이 반드시 한 개만 존재  (dfs를 써서 찾아도 최단거리 측정 가능)  -- 이진트리여도 동일함
'''
4 2 --- Node, find_n
2 1 2 --- edge_1, weight_1
4 3 2 --- edge_2, weight_2
1 4 3 --- edge_3, weight_3
1 2 --- route_1
3 2 --- route_2
'''

# # 1) 인접 리스트 생성
# # 2) dfs 구현
# # 3) 출발점 -> 도착점 거리 계산

# 1) 인접리스트 생성
Node, find_n = map(int, input().split())
# 1-1) 인접리스트 번호에 맞게 생성
adj_list = [[] for _ in range(Node +1)]
# 1-2) 엣지 입력 - 노드, 가중치 묶어서 진행
for _ in range(Node-1):
    n1, n2, weight = map(int, input().split())
    adj_list[n1].append((n2, weight))
    adj_list[n2].append((n1, weight))
# 1-3) 찾을 길 설정
routes = [list(map(int, input().split())) for _ in range(find_n)]

# 2) dfs 구현
def dfs(start_node, end_node):
    # use adj_list
    # list => heap 메모리 참조 변수 => global 필요 X

    stack = [start_node]
    visited = [False for _ in range(len(adj_list))]
    visited[0] = True
    visited[start_node] = True
    
    # 모든 길이 연결되어있다는 가정 하에, end_node에 도착시 루프 종료
    while stack[-1] != end_node:
        current = stack[-1]
        for adj in adj_list[current]:
            if not visited[adj[0]]:
                visited[adj[0]] = True
                stack.append(adj[0])
                break
        else:
            stack.pop()
    else:
        return stack

print('-------------')

# 3) 거리 계산
def distance(route):
    res = 0

    for i in range(len(route)-1):
        fr = route[i]
        to = route[i+1]
        for j in adj_list[fr]:
            if j[0] == to:
                res += j[1]
    return res

# 확인
for route in routes:
    tmp = dfs(route[0], route[1])
    print(tmp)
    print(distance(tmp))