## 먼저 달팽이 모양을 만들자.

def snail_run(step, direction, now_x, now_y, snail): # idx_now는 
    num = snail[now_x][now_y] # (0, 0) = 1
    
    # 오른쪽 방향일 때
    if direction == 0:
        if step == len(snail):
            for s in range(1, step): # if step==5: loop 4 / if step= 3: 
                num += 1 
                snail[now_x][now_y+s] = num
            new_x = now_x
            new_y = now_y + step -1
        else:
            for s in range(1, step+1): # if step==5: loop 4 / if step= 3: 
                num += 1 
                snail[now_x][now_y+s] = num
            new_x = now_x
            new_y = now_y + step
    
    # 아래 방향일 때
    elif direction == 1:
        for s in range(1, step+1): # if step == 4: loop 3
            num += 1
            snail[now_x+s][now_y] = num
        new_x = now_x + step
        new_y = now_y

    # 왼쪽 방향일 때
    elif direction == 2:
        for s in range(1, step+1): # if step == 4: loop 3
            num += 1
            snail[now_x][now_y-s] = num 
        new_x = now_x
        new_y = now_y - step

    # 위로 올라갈 때
    elif direction == 3:
        for s in range(1, step+1): # if step == 3: loop 2
            num += 1
            snail[now_x-s][now_y] = num 
        new_x = now_x - step
        new_y = now_y

    # direction >= 4인 경우
    else: 
        direction = 0
        return snail_run(step, direction, now_x, now_y, snail)


    direction += 1

    return new_x, new_y, snail, direction



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    snail = [[1 for _ in range(N)] for _ in range(N)] # 4 by 4행렬

    step = N
    direction = 0
    x, y = 0, 0


    for step in range(N, 0, -1):
        
        if step == N:
            new_x, new_y, snail, direction = snail_run(step, direction, 0, 0, snail) # 한 번만 반복
            
        else: # step !=N
            for _ in range(2):
                new_x, new_y, snail, direction = snail_run(step, direction, new_x, new_y, snail) # 두 번씩 반복
            
    print(f'#{test_case}')
    for i in range(N):
        for j in range(N):
            print((snail[i][j]), end = ' ')
        print()

        