import copy
import sys

V, Edge = map(int,input().split())
# 두 가지 접근법이 있다.

# 1. 인접행렬로 만들기. (2중 배열)
M = [[0 for _ in range(V)] for _ in range(V)] 
G = [[] for _ in range(V)]
# G = {node: [] for node in range(V)} # 이제 연결된 값을 넣으면 된다.
# {node: [e1, e2]}
F = []

for _ in range(Edge):
    f, t = map(int, input().split())

    # 1. 인접행렬
    # [[]]
    M[f][t] = M[t][f] = 1  # 양방향이기 때문에.
    
    # 2. 인접 리스트
    # {f: [t1, t2]}
    G[f].append(t)
    G[t].append(f)

    # 3. Edge 리스트
    F.append([f, t])
    F.append([t, f])


for i in range(len(F)):
    for j in range(len(F)):
        A, B = F[i]
        C, D = f[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue
        if not M[B][C]:
            continue
        for E in G[D]:
            if E == A or E == B or E ==C  or E ==D:
                continue
            print(1)
            sys.exit(0) ## 종료코드 0 # 브레이크문을 여러개 뚫어야 할 때....

print(0)
            
print(M) # 맵
print(G) # 연결된 아크
print(F) # 엣지