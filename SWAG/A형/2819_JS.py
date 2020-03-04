dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_number(n, x, y, num):
    if n == 6:
        if num not in result:
            result.append(num)
        else:
            return
            
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx in range(4) and ny in range(4):
            get_number(n+1, nx, ny, num+matrix[nx][ny])

T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(str, input().split())) for _ in range(4)]
    result = []
    for i in range(4):
        for j in range(4):
            temp = matrix[i][j]
            get_number(0, i, j, temp)
    print(f'#{tc} {len(result)}')