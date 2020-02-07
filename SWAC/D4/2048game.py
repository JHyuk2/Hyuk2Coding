def slide(board, direction):
    # 상우하좌 => 검색방향은 반대로
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    tmp_x, tmp_y = 0, 0
    length = len(board)
    
    # 위에서부터 검사, 첫 번째 인덱스에 값이 없는 경우, 아래에서 끌고온다.
    if direction == 'up': 
        for i in range(length):
            flag = True
            for j in range(length):
                # 빈 칸인 경우
                tmp_x = j+1
                if board[j][i] == 0: # 맨 위부터 검사. 비어있으면 벽까지 찾아서 값이 있을 경우 바꿔줌. 없으면 이번 줄은 넘어감.
                    tmp_x = j + 1
                    while tmp_x < length:
                        if board[tmp_x][i] != 0:
                            board[j][i], board[tmp_x][i] = board[tmp_x][i], board[j][i]        
                            break
                        tmp_x += 1
                        if tmp_x == length-1:
                            flag = False
                    if flag == False:
                        break         
                
                # 빈 칸이 아닌 경우
                if tmp_x < length and board[tmp_x][i] != 0 and board[tmp_x][i] == board[j][i]:
                    print('here', (j,i), board[j][i], (tmp_x,i), board[tmp_x][i])
                    board[j][i] *= 2
                    board[tmp_x][i] = 0
                elif board[tmp_x] == 0:
                    tmp += 1
                

    elif direction == 'right':
        
        print('right')
    elif direction == 'down':
        print('down')
    elif direction == 'left':
        print('elft')
    


board = [
    [4, 8, 2, 4, 0],
    [4, 4, 2, 0, 8],
    [8, 0, 2, 4, 4],
    [2, 2, 2, 2, 8],
    [0, 2, 2, 0, 0],
]

slide(board, 'up')
for i in range(5):
    print(board[i])