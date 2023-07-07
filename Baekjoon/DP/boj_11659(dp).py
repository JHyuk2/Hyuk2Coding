import sys

N, T = map(int, sys.stdin.readline().split())

numbers = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i] = numbers[i] + dp[i-1]

for tc in range(T):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[end]-dp[start-1])
