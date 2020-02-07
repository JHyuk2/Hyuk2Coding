# 사다리 타기


# 사다리 맵, 시작위치를 받아서 카운트를 반환
def go(ladder, pos):
    #    좌 우 하
    dx = [-1, 1, 0]
    dy = [0, 0, 1]
    x = pos[1] 
    y = pos[0]
    length = len(ladder)
    cnt = 1

    while y < length: # 끝까지 가지 않았다면 반복
        for i in range(2):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            # 좌우에 길이 있다을 때
            if 0 <= tmp_x < length and 0 <= tmp_y < length and ladder[tmp_y][tmp_x] == 1:
                print('방향전환 ^^')
                # 벽을 만나거나 0을 만나지 않는다면 계속 가라.
                while 0 <= x < length and 0 <= y < length and ladder[y][x] ==1:
                    x += dx[i]
                    y += dy[i]
                    cnt +=1
                    print(y, x, cnt)
                # 만약 다음 자리가 벽이나 0이 있다면 dx[i], dy[i]만큼 돌아간 후, 아래로 이동해라
                print('▲▲▲▲▲▲▲▲▲▲ ------  deleted')
                x += dx[2] - dx[i]
                y += dy[2] - dy[i]
                print(y, x, cnt)

        # 좌우에 길이 없다면 아래로 가라
        else:
            x += dx[2]
            y += dy[2]
            cnt += 1
            print(y, x, cnt)

    return cnt


T = int(input())

for tc in range(1, T+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]                
    start_pos = [idx for idx, num in enumerate(ladder[0]) if num == 1] # 시작하는 x좌표의 위치
    m_cnt = 10000
    
    result_list = []
    for s in start_pos:
        if s == 99:
            pos = [0, s]
            cnt = go(ladder, pos)
            result_list.append((s, cnt))

            if cnt < m_cnt:
                m_cnt = cnt
                result = s
    print(result_list)
    # print(result, result_list)