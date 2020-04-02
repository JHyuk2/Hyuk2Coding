# 탈주범 검거
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 터널에 따른 진행경로
tunnel = {
    1:[0,1,2,3], # 상하좌우
    2:[0,2], # 상하
    3:[1,3], # 좌우
    4:[0,1], # 상우
    5:[1,2], # 하우
    6:[2,3], # 하좌
    7:[0,3], # 상좌
}

# 방향을 받았을 때 진행 가능한지
passable = {
    0: [1,2,5,6], # 상
    1: [1,3,6,7], # 우
    2: [1,2,4,7], # 하
    3: [1,3,4,5], # 좌
}

# 1) 시작점으로부터 bfs
# 2) 갈 수 있는 방향들에 대해서 next_pos 찾고,
# 3) passable인 경우 진행 - 한번 간 길은 0로 만들어서 못돌아가게 하자

'''
1    
5 6 2 1 4      
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
'''

def bfs(time, current):
    global cnt
    # 현재위치와 path를 저장해서 진행
    queue = [(current, [current])]
    
    while queue:
        before = queue[-1]
        pos, path = queue.pop(0)        
        x = pos[0]
        y = pos[1]

        if not visited[x][y]:
            visited[x][y] = 1
            cnt += 1
        
        if len(path) == time:
            continue
        
        # 가능한 진행경로들을 nx, ny로 찾고
        for i in tunnel[data[x][y]]:
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <len(data) and 0 <= ny < len(data) and data[nx][ny] in passable[i] and (nx, ny) not in path:
                queue.append(((nx, ny), path + [(nx, ny)]))

T = int(input())
for tc in range(1, T+1):
    N, M, x, y, time = map(int, input().split())
    # R, C => 시작_x, 시작_y //
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    start = (x, y)

    bfs(time, start)
    
    print(cnt)
    for i in range(N):
        print(data[i])

    print('--------------------')    
    for i in range(N):
        print(visited[i])