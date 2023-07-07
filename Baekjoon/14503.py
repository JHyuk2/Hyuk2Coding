# 로봇청소기
# from collections import deque
###  0  1  2  3
###  북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방의 크기
N, M = map(int, input().split())

# 두 번째 입력 : r, c, head
r, c, head = map(int, input().split())

# 지도 생성
# 0: 청소되지 않은 곳
# 1: 벽
map_list = []
for _ in range(N):
    map_list.append(list(map(int, input().split())))

# 1. 현재 칸 청소하기
# 2. 주변 4칸 중 청소되지 않은 칸 없으면
# 2-1. 방향을 유지한 채 후진
# 2-2. 후진할 수 없으면 작동 멈추기
# 3. 주변에 청소되지 않은 빈 칸 있는 경우
# 3-1. 반시계 90' 회전
# 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소 x then 전진 한칸

time = 0

def cleaner(pos, head):
    global time
    global N, M

    x, y = pos
    # 현재 위치가 청소되지 않은 경우 청소
    if map_list[x][y] == 0:
        map_list[x][y] = 1
        time += 1
    
    # 반시계방향으로 회전하면서 청소 안한곳 찾기.
    for i in range(head, head+4):
        head = (i//4) -1
        nx = x + dx[head]
        ny = y + dy[head]

        if nx >= N or ny > M:
            continue
        
        # nx, ny가 있으면 새로운 좌표로 이동해서 청소
        else:
            map_list[nx][ny] = 0
            cleaner((nx, ny), head)
    
    # 한칸 후진        
    else:
        nx = x - dx[head]
        ny = y - dy[head]

        if nx >= N or ny > M:
            return time
        
        elif map_list[nx][ny] == 0:
            cleaner(((nx, ny), head))

    return time

pos = (r,c)

print(cleaner(pos, head))