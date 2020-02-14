def DFS(v):
    stack = []
    stack.append(v)
    visited[v] = 1
    print(v, end='-')

    while stack:
        p = v
        for w in G[v]:
            if not visited[w]:
                stack.append(w)
                v = w
                visited[w] = 1
                print(v, end=' ')
                break
        else:
            if p == v:
                v = stack.pop()


import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())

