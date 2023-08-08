# 직사각형 네 개의 합집합 면적 구하기.
# 모든 x좌표, y좌표는 1이상 100이하


# 1) 0으로 가득찬 100 x 100 사이즈 board 만들기
board = [[0 for _ in range(100)] for _ in range(100)]

# 2) 4개의 입력을 받아서 각각 x1, y1, x2, y2 로 받기.
papers = []
for _ in range(4):
    paper = list(map(int, input().split()))
    papers.append(paper)

# 3) 범위 안에 있으면 1로 색칠해주기
for paper in papers:
    x1, y1, x2, y2 = paper

    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

# 4) 색칠된 범위 구하기.
res = 0
for y in range(100):
    res += sum(board[y])
    
print(res)