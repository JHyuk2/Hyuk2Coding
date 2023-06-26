# def dp(num):
#     if num == 1:
#         return 1
#     if num == 2:
#         return 2
#     if num == 3:
#         return 4
#     else:
#         return dp(num-1) + dp(num-2) + dp(num-3)
    
# for tc in range(int(input())):
#     num = int(input())
#     print(dp(num))

#인덱스에러 조심하자
for tc in range(int(input())):
    num = int(input())
    dp = [0, 1, 2, 4]
    
    if num >3:
        dp = dp + [0 for _ in range(num-2)]
        for i in range(4, num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[num])