'''
1 0 0 1 0 0
1 1 1 1 0 0
1 0 0 1 1 0
1 1 0 0 1 0
0 1 0 0 1 0
0 1 0 0 1 0
'''

n = 6
ladder = [list(map(int, input().split())) for _ in range(6)]

#    좌 우 하
dx = [0, 0, 1]
dy = [-1, 1, 0]

start_point = [idx for idx, num in enumerate(ladder[0]) if num == 1] # 시작하는 위치.

for s in start_point:
    y = s
    x = 0
    while y < len(n)-1:
        for i in range(2):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if ladder[tmp_x][tmp_y] == 1:
                while ladder[tmp_x][tmp_y] == 1:
                    x += dx[i]
                    y += dy[i]
                    tmp_x = x + dx[i]
                    tmp_y = x + dy[i]
                else:
                    x += 1
                    break
