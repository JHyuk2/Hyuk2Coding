# boj
from collections import deque

start, end = map(int, input().split())
# 10만까지 입력 가능하니까, 그냥 10만까지 늘려버림.
visited = [0 for _ in range(100001)]
time = 0

# 시작위치랑 0초를 넣어줌.
queue = deque([(start, time)])

# 조건을 충족할 때까지 반복
while queue:
    pos, cur_time = queue.popleft()
    if pos == end:
        print(cur_time)
        break

    if not visited[pos]:
        visited[pos] = 1

        for n_pos in [pos-1, pos+1, pos*2]:
            if (0 <= n_pos < 100001) and not visited[n_pos]:
                queue.append((n_pos, cur_time+1))
    else:
        continue
    
