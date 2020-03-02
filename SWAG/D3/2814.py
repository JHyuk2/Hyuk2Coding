## DFS 이용한 최장경로 계산.

# # 1) 인접 리스트 생성
# # 2) DFS 탐색

def dfs(v, adj_list):
    stack = [v]
    visited = [False for _ in range(len(adj_list))] # 길이만큼 False


T = int(input())

for tc in range(1, T+1):
    # N: node, M: edges
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    # 빈 인접 리스트
    adj_list = [[] for _ in range(N)]

    # 인접 리스트에 삽입
    for e in edges:
        tmp_e = list(reversed(e))
        adj_list[e[0]].append(e[1])
        adj_list[tmp_e[0]].append(tmp_e[1])
    
    
    
    