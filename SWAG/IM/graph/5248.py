'''
3
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
'''

def dfs(num):
    global cnt
    if visited[num]:
        return
    stack = [num]
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = 1
            stack += adj_dict[cur]
            for num in adj_dict[cur]:
                stack += adj_dict[num]
    cnt += 1 


for tc in range(int(input())):
    # 준비물
    cnt = 0
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))
    adj_list = []
    for i in range(m):
        adj_list.append((tmp[i*2], tmp[i*2+1]))
        adj_list.append((tmp[i*2+1], tmp[i*2]))

    adj_dict = {}
    for i in range(1, n+1):
        adj_dict[i] = []

    for adj in adj_list:
        s = adj[0]
        t = adj[1]
        adj_dict[s].append(t)
    
    visited = [0] * (n+1)
    for i in range(1, n+1):
        dfs(i)
    print(f'#{ tc +1 } {cnt} ')


    # print(adj_list, adj_dict)

    # 인접리스트를 표현하고 dfs로 전부 찾는다...?
    
    # 전부 체크된 경우 cnt 해주기?