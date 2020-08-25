'''
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

#1 2
#2 4
#3 10
'''
import heapq as hq

for tc in range(int(input())):
    v, e = map(int, input().split())
    # 방향그래프
    adj_list = [[] for _ in range(e+1)]
    dist = [-1 for _ in range(e+1)]

    for i in range(e):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))
    
    dist[0] = 0
    q = []
    hq.heappush(q, (dist[0], 0))
    while q:
        _, x = hq.heappop(q)
        for y, cost in adj_list[x]:
            if dist[y] == -1 or dist[x] + cost < dist[y]:
                dist[y] = cost + dist[x]
                hq.heappush(q, (dist[x]+cost, y))
    print(f'#{ tc+1 } { dist[v] }')