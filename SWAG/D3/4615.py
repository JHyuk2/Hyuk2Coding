# 흰돌 1 검은돌 2
# 3 2 1 => (3,2) 흰돌
# 처음엔 흑부터 시작함.

# 줄바꿈 출력용
print()
 
size = 4
 
# 초기 보드 생성
def init_board(size):
    board = [[0 for _ in range(size)] for _ in range(size)]
    start = (size // 2) -1
    end = start + 2
    
    for i in range(start, end):
        for j in range(start, end):
            if i == j: 
                board[i][j] = 1
            else:
                board[i][j] = 2
    return board

board = init_board(size)

for i in range(size):
    for j in range(size):
        print(board[i][j], end = ' ')
    print()

print('------------------------------')
def flip(board, point, color):
    #point ==> (0, 1)
    #color ==> 2
    x, y = point
    
    # 방향설정
    #    상[왼 가 오] / 중[왼 오] / 하[왼 가 오]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1] 
    dy = [-1, 0, 1, -1, 1, -1, 0, 1 ]
    for x in range(len(board)):
        for y in range(len(board)):
            for i in range(8):
                if 0 <= x + dx[i] < len(board) and 0<= y + dy[i] < len(board):
                    tmp_x = x + dx[i]
                    tmp_y = t + dy[i]
                    pre_stone = board[tmp_x][tmp_y]
                # 벽으로 막힌 경우는 건너뛴다.
                else:
                    continue
                    
                if not pre_stone: # 돌이 없는 자리는 뒤집을 수 없다.
                    if pre_stone != color: # 이전이 같은 컬러인 경우 뒤집지 않는다.
                        tmp = []                                                
                        while pre_stone != color or pre_stone != 0: # 
                            tmp.append([(now_x, now_y) for now_x, now_y in pre_stone])
                            next_x = tmp_x + dx[i]
                            next_y = tmp_y + dy[i]
                            pre_stone = board[next_x, next_y]
                            # 1) 벽을 만날동안 같은색을 못찾았을 경우.
                            if not 0<= next_x < len(board) or not 0<=next_y < len(board):
                                tmp = []
                                break
                                
                        if not len(tmp) : # tmp가 비어있지 않으면
                            for this_x, this_y in tmp:
                                board[this_x][this_y] = color
    return board


for i in range(size):
    for j in range(size):
        print(board[i][j], end = ' ')
    print()

print('------------------------------')