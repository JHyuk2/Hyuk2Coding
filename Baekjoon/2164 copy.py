from collections import deque
import sys

n = int(sys.stdin.readline())
num_list = [i+1 for i in range(n)]
i = 0
cnt = 1
jump = 0

while True: 
    i += 1
    i %= n
    # 방문 했던 곳이면
    if visited[i]:
        continue
    
    # not visited        
    else:
        jump += 1
        if jump == 2:
            visited[i] = 1
            jump = 0
            cnt += 1
            if cnt == n-1:
                break
        else:
            continue

print(visited.index(0)+1)