stairs = int(input())

dp = [[0 for j in range(i+1)] for i in range(stairs+1)]
tri_list = [0]

for i in range(stairs):
    tri_list.append(list(map(int, input().split())))

# 첫 dp초기화
dp[1] = tri_list[1] # dp[1][0] = tri_list[1][0]

# dp[2][0] = dp[1][0] + tri_list[2][0]
# dp[2][1] = dp[1][0] + tri_list[2][1]
# dp[3][0] = dp[2][0] + tri_list[3][0]
# dp[3][1] = max(dp[2][0] + tri_list[2][1], dp[2][1] + tri_list[2][1])
# dp[3][2] = dp[2][1] + tri_list[3][2]

for i in range(2, stairs+1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i-1][j] + tri_list[i][j]
        elif i-j == 1:
            dp[i][j] = dp[i-1][j-1] + tri_list[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri_list[i][j]

print(max(dp[stairs]))