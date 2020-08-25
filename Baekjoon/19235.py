# 불꽃카리스마 모노미도민호우

# 입력 - 첫째 줄: 블록을 놓는 횟수 
# t=1 (1x1); t=2 (1x2); t=3 (2x1)

# 출력 | 첫째줄 -  점수; 둘째 줄 - green, blue zone 남은 블럭

for _ in range(int(input())):
    sizes = [None, [(0, 0)], [(0, 0), (0, 1)], [(0, 0), (1, 0)] # 각 사이즈에 맞게 범위를 설정
    t, x, y = list(map(int, input().split()))

    # red 칠해질 좌표
    red_zone = []
    for red_x, red_y in sizes[t]:
        red_zone.append([red_x + x, red_y + y])
        