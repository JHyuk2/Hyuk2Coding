# 직사각형 네개의 합집합 면적 구하기

board = [[0 for _ in range(100)] for _ in range(100)]
square = [list(map(int, input().split())) for _ in range(4)]

# 색칠공부 끝
for s in square:
    r1, c1, r2, c2 = s
    for x in range(r1, r2):
        for y in range(c1, c2):
            board[y][x] += 1
res = 0
for i in range(len(board)):
    for j in range(len(board)):
        res += 1 if board[i][j] != 0 else 0
print(res)