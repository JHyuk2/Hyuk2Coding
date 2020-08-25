for tc in range(int(input())):
    n = int(input())
    numpad = [list(map(int, input().split())) for _ in range(n)]
    road_sum = [[0]* n  for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 0인 경우
            if i == 0 and j == 0:
                road_sum[i][j] = numpad[i][j]
                continue
            else:
                pre_i = i-1
                pre_j = j-1
                up, left = 10000, 10000

                if pre_i >= 0:
                    up = road_sum[pre_i][j] + numpad[i][j]    
                if pre_j >= 0:
                    left = road_sum[i][pre_j] + numpad[i][j]
                road_sum[i][j] = min(up, left)
    print(f'#{tc+1} {road_sum[n-1][n-1]}')