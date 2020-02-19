for test_case in range(1, 11):
    tc = int(input())

    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    
    cross_down, cross_up = 0, 0
    horizon, vertical = [], []
    result =[]
    
    for x in range(100):
        horizon_tmp, vertical_tmp = 0, 0
        for y in range(100):
            if x==y:
                cross_down += arr[x][y]
            if x+y == 100-1:
                cross_up += arr[x][y]
            horizon_tmp += arr[x][y]
            vertical_tmp += arr[y][x]
        horizon.append(horizon_tmp)
        vertical.append(vertical_tmp)

    else: # 루프 종료 후
        result.append(cross_down)
        result.append(cross_up)
    
    # 사실 이러면 연산시간만 늘어남 그냥 다 더하고 한번에 max 찾아도 상관없음
    result.append(max(horizon))
    result.append(max(vertical))
    
    print(f'#{tc} {max(result)}')
    