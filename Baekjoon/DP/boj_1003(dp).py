import sys

# [count 0, count 1]
dp = [[0,0] for _ in range(41)]

for tc in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    dp[0][0] = 1
    dp[1][1] = 1
    for i in range(2, num+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(' '.join(map(str, dp[num])))