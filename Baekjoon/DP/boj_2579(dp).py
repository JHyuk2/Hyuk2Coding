step = int(input())
score_list = [0] + [int(input()) for _ in range(step)]

# 무조건 도착지점을 밟아야 한다.
# 연속해서 3개를 밟진 못한다.

dp = [0 for _ in range(step+1)]

# 층이 2개 이하인 경우
if step <= 2:
    print(sum(score_list))
    
# 계단이 3개 이상인 경우
else : # step >= 3
    dp[1] = score_list[1]
    dp[2] = score_list[1] + score_list[2]

    for i in range(3, step+1):
        dp[i] = max(score_list[i-1]+dp[i-3], dp[i-2]) + score_list[i]
    print(dp[step])