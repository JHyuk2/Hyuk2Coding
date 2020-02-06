def init_board(size):
    board = [[0]*size for _ in range(size)]
    start = (size//2) -1
    end = start +2
    
    for i in range(start, end):
        for j in range(start, end):
            if i == j:
                board[i][j] = 1
            else:
                board[i][j] = 2
    return board

def flip(board, point, color):
    x, y = point
    board[x][y] = color
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for k in range(8):
        now_x, now_y = x+dx[k], y+dy[k]
        if 0<= now_x < len(board) and 0 <= now_y < len(board) and board[now_x][now_y] == (color%2)+1:
            pre_stone = board[now_x][now_y]
            
            tmp =[]
            flag = False
            while 0 <= now_x < len(board) and 0<=now_y < len(board):
                if board[now_x][now_y] == 0:
                    break

                if board[now_x][now_y] == color:
                    flag = True
                    break
                tmp.append((now_x, now_y))
                now_x += dx[k]
                now_y += dy[k]
                    
            if flag == True:
                for tmp_x, tmp_y in tmp:
                    board[tmp_x][tmp_y] = color
    print('--'*40)         
    for i in range(N):
        print(board[i])
                


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = init_board(N)
    
    for m in range(M):
        x, y, color = map(int, input().split())
        flip(board, (y-1, x-1), color)
        
    cnt_b, cnt_w = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                cnt_b += 1
            elif board[i][j] == 1:
                cnt_w += 1
                
