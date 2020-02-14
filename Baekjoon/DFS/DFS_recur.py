def DFS(v):
    visited[v] = 1
    print(v, end='-')

    for w in G[v]:
        if not visited[w]:
            DFS[w]

            