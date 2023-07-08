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

# 1. 현재 칸 청소하고 4방향을 둘러보기
def cleaner(pos, head):
    from collections import deque
    global tsime
    global N, M
    queue = deque([])

    x, y = pos
    # 현재 위치가 청소되지 않은 경우 청소
    if map_list[x][y] == 0:
        map_list[x][y] = 1
        time += 1
    
    # 반시계방향으로 회전하면서 청소 안한곳 찾기.
    for i in range(head, head+4):
        cur_head = (i%4) -1
        nx = x + dx[cur_head]
        ny = y + dy[cur_head]
        
        # 벽에 막혀있거나, 0보다 작은 위치는 못감
        if nx >= N or ny >= M or nx < 0 or ny < 0:
            continue
        
        # nx, ny가 있으면 새로운 좌표로 이동해서 청소
        else:
            if map_list[nx][ny] == 0:
                queue.append([(nx, ny), cur_head])

    if queue:
        next_pos, n_head = queue.popleft()
        cleaner(next_pos, n_head)
    
    # 뒤로 한 칸 후진
    else:


# def cleaner(pos, head):
    global time
    global N, M

    if find_dirt:
    
    
    
    # 고개는 유지한 채 한칸 후진
    else:
        nx = x - dx[head]
        ny = y - dy[head]

        # 만약 뒤로 돌아가서 
        if nx >= N or ny > M:        
            if map_list[nx][ny] == 0:
                cleaner(((nx, ny), head))


pos = (r,c)
cleaner(pos, head)
print(time)