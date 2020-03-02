# 정사각형 방
# BFS 사용하는 것 같음.

# 1) 랜덤한 출발점을 지정
'''
3   --- size
<room>
9 3 4 
6 1 5
7 8 2
'''
# # A(ij)는 서로 모두 다른 정수 => room_id --> unique_value

size = int(input())
room = [list(map(int, input().split())) for _ in range(size)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1) 순회한 곳은 하나씩 찍으면서간다.
visited = []

# 2) BFS 시작
def bfs(start_x, start_y, length = 1, tmp = []):
    global size
    flag = 0
    room_num = room[start_x][start_y]
    visited.append(room_num)

    if length == 1:
        tmp = [room_num, length]
    
    for i in range(4):
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        if 0 <= nx < size and 0 <= ny < size and room[nx][ny] == (room_num +1):
            if room[nx][ny] in visited:
                return
            
            flag = 1
            return bfs(nx, ny, length+1, tmp)

    if not flag:
        tmp[1] = length
        return tmp
    
res = []
for i in range(3):
    for j in range(3):
        start_x = i
        start_y = j
        if room[start_x][start_y] in visited:
            continue
        else:
            res.append(bfs(start_x, start_y))
print(res)