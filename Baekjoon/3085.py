# 사탕 게임

# 모든 교환은 오른쪽 or 아래쪽으로만 이루어진다고 가정한다.
# index out of range error 조심하기
# 만약 교환 중 입력받은 길이 N이 길이가 되는 경우 break

n = int(input())

# 그리드 생성
grid = []
for i in range(n):
    grid.append(list(input()))

flag = 0
result = 0

# 가로방향 탐색
def horizontal_search(y, x):
    global n
    left = 0
    right = 0
    
    # 왼쪽 서치
    for nx in range(x, -1, -1):
        if grid[y][x] == grid[y][nx]:
            left += 1
        else:
            break
    
    # 오른쪽 서치
    for nx in range(x, n):
        if grid[y][x] == grid[y][nx]:
            right += 1
        else:
            break
    # 시작지점이 두번 더해졌기에 한 번 빼줌
    return left + right -1

# 세로방향 길이 탐색
def vertical_search(y, x):
    global n
    up = 0
    down = 0

    # 북쪽 서치
    for ny in range(y, -1, -1):
        if grid[y][x] == grid[ny][x]:
            up += 1
        else:
            break
    # 남쪽 서치
    for ny in range(y, n):
        if grid[y][x] == grid[ny][x]:
            down += 1
        else:
            break
    return up + down -1


# 가장 긴 길이 완전탐색
def find_maxlen(y, x):
    global n
    max_len = 0
    for y in range(n):
        for x in range(n):
            if max_len == n:
                return n
            horizontal = horizontal_search(y, x)
            vertical = vertical_search(y, x)
            longer = max(horizontal, vertical)
            if max_len < longer:
                max_len = longer     
    return max_len

# 인접한 칸이 다른 사탕이 있는지 찾기
# 우리는 오른쪽과 아랫쪽만 탐색할거임.
def changable(y, x):
    global result
    global n
    dy = [1, 0]
    dx = [0, 1]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        # index error 피하기
        if ny < n and nx < n:
            if grid[y][x] != grid[ny][nx]:
                # 위치 바꾸고 길이계산
                grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
                temp = find_maxlen(y, x)
                if result < temp:
                    result = temp
                # 다시 되돌려주기
                grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
    return



for y in range(n):
    if flag:
        break
    for x in range(n):
        changable(y, x)
        if result == n:
            flag = 1
            break
print(result)