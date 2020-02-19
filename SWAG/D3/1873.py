face = {
    'L':'<',
    'R':'>',
    'U':'^',
    'D':'v',
    }

barrier = ['*','#','-']

def shoot(field, tank):
    global face 
    global barrier

    # position & face
    tx = tank[0] # tank_x 
    ty = tank[1] # tank_y
    now = field[tx][ty]
    
    # 왼쪽 탐색
    if now == '<':
        for i in range(ty-1, -1, -1): 
            if field[tx][i] == '#':
                break
            elif field[tx][i] =='*':
                field[tx][i] = '.'
                break
            else:
                continue

    # 오른쪽 탐색
    elif now == '>':
        for i in range(ty+1, len(field[tx])):
            if field[tx][i] == '#':
                break
            elif field[tx][i] =='*':
                field[tx][i] = '.'
                break
            else:
                continue

    # 아랫쪽 탐색
    elif now == 'v': 
        for i in range(tx+1, len(field)): 
            if field[i][ty] == '#':
                break
            elif field[i][ty] =='*':
                field[i][ty] = '.'
                break
            else:
                continue

    # 윗쪽 탐색    
    elif now == '^':
        for i in range(tx-1, -1, -1): 
            if field[i][ty] == '#':
                break
            elif field[i][ty] =='*':
                field[i][ty] = '.'
                break
            else:
                continue
    # print('-----shoot-----')
    # print(field)
    return field

def move(field, tank, command):
    global barrier

    # pos
    tx = tank[0] 
    ty = tank[1]

    # 방향설정, next 찾기
    if command == 'U':
        field[tx][ty] = '^'
        nx, ny = (tx-1, ty)
    elif command == 'D':
        field[tx][ty] = 'v'
        nx, ny = (tx+1, ty)
    elif command == 'L':
        field[tx][ty] = '<'
        nx, ny = (tx, ty-1)
    elif command == 'R':
        field[tx][ty] = '>'
        nx, ny = (tx, ty+1)

    # 못움직임
    # 맵밖으로 나가질 때
    if nx == len(field) or ny == len(field[tx]) or ny == -1 or nx == -1: 
        nx, ny = tx, ty 
    
    # encounter a barrier
    elif field[nx][ny] in barrier:
        nx, ny = tx, ty
    
    # next == '.' 인 경우
    else: 
        field[tx][ty], field[nx][ny] = field[nx][ny], field[tx][ty] # 탱크위치도 바꿔줌

    tank = (nx,ny)
    # print('----move-----')
    # print(field)
    return field, tank

T = int(input())

for test_case in range(1, T+1):
    height, width = map(int, input().split())
    field = []

    # 필드 입력받으면서 탱크 찾고
    for i in range(height):
        tmp = list(input())
        for j in face.values():
            if j in tmp:
                tank = (i,tmp.index(j)) # 탱크위치
        field.append(tmp)
    
    command_cnt = int(input())
    command_list = input() # 커맨드 받음.


    for command in command_list:
        if command == 'S':
            field = shoot(field, tank)

        else: # command UDLR
            field, tank = move(field, tank, command)
    
    for idx, f in enumerate(field):
        field[idx] = ''.join(f)
    field = '\n'.join(field)

    print(f'#{ test_case } { field }')