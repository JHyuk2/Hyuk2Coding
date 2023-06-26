'''
# tc)1

1111111111111111
1210000000100011
1010101110101111
1000100010100011
1111111010101011
1000000010101011
1011111110111011
1010000010001011
1010101111101011
1010100010001011
1010111010111011
1010001000100011
1011101111101011
1000100000001311
1111111111111111
1111111111111111
'''

# 1) 먼저 start point를 찾는다ㅏ.
# 2) 열린 쪽 길을 동서남북 순서로 탐색한다. 
# 2-1) 열린 길이 있다면 이전 포인트를 기억하고, 다음 방향으로 진행
# 2-2) 길을 진행하다가 막혔다면 다음 포인트로 진행
# 두 가지 방법으로 진행이 가능하다. (BFS, DFS)

def path_finding(path=[pos], pos):
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)
    
    # 진행방향
    forward = [right, down, left, up]

    for x, y in forward:
        next_x = pos[1] + x
        next_y = pos[0] + y
        if maze[next_x, next_y] == '0':
             


for tc in range(int(input())):
    # find start point & make maze
    maze = []
    for i in range(16):
        temp = input()
        if '2' in temp:
            start = (temp.find('2'), i)
        maze.append(temp)

    
