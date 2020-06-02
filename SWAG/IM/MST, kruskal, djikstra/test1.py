# input_data
'''
10
2 1
0 1 10
0 3 5
1 3 2
1 2 1
3 1 3
3 2 9
2 4 4
4 2 6
3 4 2
4 0 7
'''


import heapq as hq

e = int(input()) # edge의 개수
start, end = map(int, input().split()) # 출발, 도착지점 설정

# 방향그래프 입력받기
adj_list = [[] for _ in range(e)]
dist = [-1 for _ in range(e)]
for i in range(e):
    s, e, w = map(int, input().split())
    adj_list[s].append((e, w))

def dijkstra(start, end):
    dist[start] = 0
    q = []
    hq.heappush(q, (dist[start], start))
    while q:
        print(q)
        _, x = hq.heappop(q)
        for y, cost in adj_list[x]:
            if dist[y] == -1 or dist[x] + cost < dist[y]:
                dist[y] = cost + dist[x]
                hq.heappush(q, (dist[x]+cost, y))
    print(f'#dist <{ start }> to <{ end }> : { dist[end] }')

dijkstra(start, end)
print('2020710187, 이종혁')