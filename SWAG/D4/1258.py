# 행렬찾기.

# # 1) 출발점만 찾기
# # 2) 출발점 기준으로 rectangle구하기
# # 3) 형식에 맞게 정렬 후 출력

# # 왼/위쪽이 (벽 or 0)인 경우에만 출발점이 가능
def find_start(matrix):
    length = len(matrix)
    res = []

    for i in range(length):
        for j in range(length):
            up = i-1
            left = j-1
            
            # 양쪽 벽
            if i == 0 and j == 0 and matrix[i][j]:
                res.append([i,j])
            # 위쪽벽 and True
            elif i == 0 and matrix[i][j]:
                if not matrix[i][left] :
                    res.append([i,j])           
            # 왼쪽벽 and True
            elif j == 0 and matrix[i][j]:
                if not matrix[up][j]:
                    res.append([i,j])
            # 벽 없을 때
            else:
                if matrix[i][j] and not matrix[up][j] and not matrix[i][left]:
                    res.append([i, j])
    return res

# 시작점에서 출발, 행렬의 크기를 return
def rectangles(start_points, matrix):
    res = []

    for s in start_points:
        x = s[0]
        y = s[1]
        
        nx = x+1
        ny = y+1
        while nx < len(matrix):
            if matrix[nx][y]:
                nx +=1
            else:
                break
        # 탈출하면 벽을 뚫었거나, 0을 만났거나
        end_x = nx - 1
        while ny < len(matrix):
            if matrix[x][ny]:
                ny += 1
            else:
                break
        # x와 마찬가지.
        end_y = ny -1

        res.append([end_x-x+1, end_y-y+1])        
    return res

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    start_points = find_start(matrix)
    rectangle = rectangles(start_points, matrix)

    # # 행렬 size에 따라 순서 정리
    rectangle.sort(key = lambda x:(x[0]*x[1], x[0]))
    result = ''
    for r in rectangle:
        s1, s2 = list(map(str, r))
        result += s1 + ' '
        result += s2 + ' '
    
    print(f'#{tc} {len(rectangle)} {result.strip()}')