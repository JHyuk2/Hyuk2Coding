# 정사각형 방

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tmp = []
cnt = 0
def go(start_x, start_y, flag = 1):
    global cnt
    global min_tmp
    global length
    global tmp
    
    cnt += 1
    length += 1
    room_num = room[start_x][start_y]
    visited[start_x][start_y] = 1
    
    # 첫 번째 room 검사
    if flag==1:
        min_tmp = room_num
        tmp = [room_num]

    # 재귀함수 진행중 (- room이 2개 이상)
    else:
        if room_num < min_tmp:
            min_tmp = room_num
        tmp.append(room_num)

    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]
        if 0 <= nx < size and 0 <= ny < size and abs(room[nx][ny] - room_num) == 1 and not visited[nx][ny]:
            # # 방이 2번째 이상인 경우, flag = 0으로 바꿔서 진행
            go(nx, ny, flag = 0)
  
T = int(input())

for tc in range(1, T+1):
    size = int(input())
    room = [list(map(int, input().split())) for _ in range(size)]
    visited = [[0]*(size) for _ in range(size)] # n*n
    min_tmp = 0
    res_min = 99999
    res_len = 0

    for i in range(size):
        for j in range(size):
            length = 0
            if visited[i][j]:
                continue
            min_tmp = room[i][j]
            go(i, j)
            
            if length > res_len:
                res_min = min_tmp
                res_len = length
            elif length == res_len:
                res_min = res_min if res_min < min_tmp else min_tmp

            print(min_tmp, tmp)

    print(f'#{tc} {res_min} {res_len}')
