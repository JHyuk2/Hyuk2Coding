#     좌 상 하 우 => 반대 방향으로 찾아주면 됨.

def search(board, pos, direction):
    # pos  현재 위치
    now_x = pos[0]
    now_y = pos[1]
    
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    dir_dict = {
        'right':0,
        'down':1,
        'up':2,
        'left':3,
    }

    # 여기서 direction 0은 왼쪽을 의미
    tmp_x = now_x + dx[dir_dict[direction]]
    tmp_y = now_y + dy[dir_dict[direction]]
    cnt = 0
    flag = 1

    while 0 <= tmp_x < len(board) and 0 <= tmp_y < len(board):
        if flag == 0:
            break
        
        # ----- 출력 진행사항 확인용 ----- # -> 주석처리된 print문장 실행
        # print(board[now_x][now_y], (now_x, now_y), board[tmp_x][tmp_y], (tmp_x, tmp_y))

        # # 1) 현재 위치에 0이 들어가 있는 경우
        if board[now_x][now_y] == 0 :
            if board[tmp_x][tmp_y] == 0:
                tmp_x += dx[dir_dict[direction]]
                tmp_y += dy[dir_dict[direction]]
                
                # # 1-1) 해당 라인에 숫자가 없으면 break
                if tmp_x == len(board) or tmp_y == len(board):
                    flag = 0
                continue

            # # 1-2) 해당 라인에 숫자가 있을 경우, 0과 자리교체
            else:
                # print('here')
                board[now_x][now_y], board[tmp_x][tmp_y] = board[tmp_x][tmp_y], board[now_x][now_y]
                search(board, [now_x, now_y], direction) # 위치 바꾼 후 다시 search
                break

        # # 3) 현재 자리가 0이 아닌경우
        else: 
            if board[tmp_x][tmp_y] == 0:
                tmp_x += dx[dir_dict[direction]]
                tmp_y += dy[dir_dict[direction]]
                # print('tmp ++ and loop')
                # # 3-1) 마찬가지로 끝까지 서치 후 break
                if tmp_x == len(board) or tmp_y == len(board):
                    flag = 0
                    # print('flag = 0')
                continue

        # # 3-2) search 중 같은 숫자를 발견한 경우 mearge
            else:
                if board[now_x][now_y] == board[tmp_x][tmp_y]:
                    # print('double and delete')
                    board[now_x][now_y] *= 2
                    board[tmp_x][tmp_y] = 0
                    break
        # # 3-3) search => 현재 숫자와 다른게 나온 경우 break
                else:
                    break
    return board


T = int(input())

for tc in range(1, T+1):
    n, direction = input().split()
    n = int(n)
    board = [list(map(int, input().split())) for _ in range(n)]
    
    if direction == 'up':
        for i in range(len(board)):
            for j in range(len(board)):
                search(board, [i,j], direction)
        # # 오른쪽에서부터 검사  
    if direction == 'right':
        for i in range(len(board)):
            for j in range(len(board)-1, -1, -1):
                search(board, [i,j], direction)
    
    if direction == 'down':
        for i in range(len(board)-1, -1, -1):
            for j in range(len(board)):
                search(board, [i,j], direction)

    if direction == 'left':
        for i in range(len(board)):
            for j in range(len(board)):
                search(board, [i, j], 'left')

    print('#{}'.format(tc))
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = ' ')
        print()

"""
# search(tmp, [3,3], 'right')
# for i in range(len(tmp)):
#     print(tmp[i])
# print('----'*30)
# search(tmp, [3,2], 'right')

# for i in range(len(tmp)):
#     print(tmp[i])
"""