import sys
'''
7 8 
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''
sys.stdin = open('input.txt')
N, M = map(int, input().split())
M = [[0 for _ in range(N)] for _ in range(N)] # 인접 행렬 초기화
G = [[] for _ in range(N)] # 인접 리스트 초기화

for _ in range(E):
    f, t = map(int, input().split())
    
    # 양방향 인접 행렬 만들기
    M[f][t] = M[t][f] = 1

    # 인접 리스트 만들기.
    G[f].append(t)
    G[t].append(f)

def DFS(v, G):
    stack = [v]
    visited = [False for _ in range(len(graph))]

    while stack:
        start = stack.pop()

        for i in graph(start):
            if visited(i) == False:
                stack.append(i)
                visited[i] = True
                break
        else:
            stack.pop()



print(M)
print(G)