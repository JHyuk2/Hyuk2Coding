# 미로의 거리
'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

#1 5
#2 5
#3 0
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(destination, queue):
    length = len(maze)
    result = 0
    
    while queue:
        cur = queue.pop(0)
        start = cur[0] # [x, y]
        path = cur[1] # [[x1, y2], [x2, y2], [x3, y3]...]

        if start == destination:
            if result == 0:
                result = len(path)-2
            elif len(path)-2 < result:
                result = len(path)-2
            continue

        for i in range(4):
            nx = start[0] + dx[i]
            ny = start[1] + dy[i]
            
            if 0 <= nx < length and 0 <= ny < length and maze[nx][ny] !='1':
                if [nx, ny] not in path:
                    n_path = path + [[nx, ny]]             
                    queue.append(([nx, ny], n_path))
    return result

for tc in range(int(input())):
    size = int(input())
    maze = [list(input()) for _ in range(size)]

    # start_point, end_point 찾기
    for i in range(size):
        for j in range(size):
            if maze[i][j] == '3':
                destination = [i, j]
            elif maze[i][j] =='2':
                start_point = [i, j]

    queue = [(start_point, [start_point])]
    res = dfs(destination, queue)
    print(f'#{tc+1} {res}')
