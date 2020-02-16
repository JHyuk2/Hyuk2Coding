def isLandable(land, pos, K, H):
    # K : 최고점 - 최저점 <= K
    # H : 본체위치 - 저점 <= H
    
    # 1) 주변에 8칸이 없는 경우(ex 벽에 붙었을 때) => False
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1 ,1, 0, -1, -1, -1]
    
    x = pos[0]
    y = pos[1]
    height = len(land)
    width = len(land[0])
    tmp_list = []
    
    for i in range(8):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        
        if 0 <= tmp_x < height and 0 <= tmp_y < width :
            tmp_list.append(land[tmp_x][tmp_y])
        else:
            return False
        
    low = min(tmp_list) # 최저점
    high = max(tmp_list) # 최고점
    
    # 범위를 벗어났을 때 False
    if high - low > K  or land[x][y] - low >H:
        return False
    
    return True

T = int(input())
    
for tc in range(1, T+1):
    N, M, K, H = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    result = 0
        
    for i in range(len(land)):
        for j in range(len(land[0])):
            if isLandable(land, [i, j], K, H):
                result += 1
                    
    print('#{} {}'.format(tc, result))