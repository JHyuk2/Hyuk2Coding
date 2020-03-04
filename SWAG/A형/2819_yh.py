def dfs(x,y,res,cnt) :
    global count
    count += 1
    if cnt == 7 :
        result.add(res)
        return
    else :
        for dx, dy in (0,1),(0,-1),(1,0),(-1,0) :
            nx,ny = x+dx, y+dy
            if 0 <= nx < 4 and 0 <= ny < 4 :
                dfs(nx,ny,res+board[nx][ny],cnt+1)
T = int(input())

for t in range(1, 1+T) :
    count = 0
    board = [list(input().split()) for _ in range(4)]
    result = set()
    for i in range(4) :
        for j in range(4) :
            dfs(i,j,board[i][j],1)
    fin = set(result)
    print(f'#{t} {len(fin)}')
    print(count)