'''
1
7 1 2 3 4 5 6 3
5
0 0 0 0 0
0 1 2 0 0
3 6 3 0 0
0 5 4 0 0 
0 0 0 0 0
'''
T = int(input())

for tc in range(1, T+1):
    find_num = list(input().split())
    size = int(input())
    data  = [list(map(int, input().split())) for _ in range(size)]
    adj_list = [[] for _ in range(7 + 1)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # # 1) 인접 리스트 생성
    for i in range(size):
        for j in range(size):
            if data[i][j] !=0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < size and 0 <= ny < size and data[nx][ny] != 0:
                        adj_list[data[i][j]].append(data[nx][ny])

    print(adj_list)
    # # 2) 