import sys

n = int(input())

# 초기값 설정 및 index error 방지
dp = [0, 1, 2]
dp = dp + [0 for _ in range(n)]

if n > 2:
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

print(dp[n]%10007)