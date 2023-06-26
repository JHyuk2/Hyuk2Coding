# 중복문제 (1463번)
# 위에거는 dp로 풀었지만 아래는 bfs로 푸는게 더 좋을 것 같다.
## 하지만 걱정했던대로 메모리에러가 나서 다시...
### 생각해보니, 그냥 path랑 len만 이용해서 갈 수 있다...



# from collections import deque

import sys

num = int(sys.stdin.readline())

# 경로를 저장하면서 갈 수 있는 dp가 필요하다.
# [path], counter
dp = [[[1], 0] for _ in range(num+1)]

def flag_check(dp, i, jump):
    if dp[i][1] > dp[i//jump][1] +1:
        return True
    else: # counter가 더 작은 경우
        return False
    
for i in range(2, num+1):
    dp[i][1] = dp[i-1][1] + 1     # counter +1
    dp[i][0] = dp[i-1][0] + [i]   # path check i
    
    if flag_check(dp, i, 3):
        if i%3 == 0:
            dp[i][1] = dp[i//3][1] + 1 # counter +1
            dp[i][0] = dp[i//3][0] + [i]

    if flag_check(dp, i, 2):
        if i%2 == 0:
            dp[i][1] = dp[i//2][1] + 1 # counter +1
            dp[i][0] = dp[i//2][0] + [i]

print(dp[num][1])
print(' '.join(map(str, reversed(dp[num][0]))))


# while queue:
#     cur_path, count = queue.popleft()
#     pos = cur_path[-1]
    
#     if pos == 1:
#         print(count)
#         print(' '.join(map(str, cur_path)))
#         break
    
#     else:
#         count += 1 
#         queue.append([cur_path + [pos-1], count])
#         if pos%3 == 0 : queue.append([cur_path + [pos//3], count])
#         if pos%2 == 0 : queue.append([cur_path + [pos//2], count])