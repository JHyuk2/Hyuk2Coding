# MST (minimum spanning tree)
'''
3
2 3
0 1 1
0 2 1
1 2 6
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
#2 13
#3 22
'''

# 1) 사이클이 생기지 않도록한다. - find_set...?
# 2) 가중치의 합이 최소가 되도록 한다.

import heapq as hq

for tc in range(int(input())):
    v, e = map(int, input().split())
    check = [False] * (v+1)
    
    # 인접그래프
    adj_dict = [[] for _ in range(v+1)]
    for i in range(e):
        s, e, w = map(int, input().split())
        adj_dict[s].append((e, w))
        adj_dict[e].append((s, w))

    # heapq 시작점 설정
    q = []
    for e, cost in adj_dict[0]:
        hq.heappush(q, (cost, e))
        check[0] = True

    # 설정
    cost_sum = 0
    while q:
        cost, e = hq.heappop(q)
        if check[e]: continue
        check[e] = True
        cost_sum += cost
        # print(q, cost_sum)
        for y, c in adj_dict[e]:
            hq.heappush(q, (c, y))

    print(f'#{ tc+1 } { cost_sum}')
        