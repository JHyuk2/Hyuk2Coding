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
    next_x, next_y = 0, 0

    while next_y != length-1: # 끝까지 가지 않았다면 반복
        # 변수 선언

        for i in range(2):
            next_x = x + dx[i]
            nexy_y = y + dy[i]

            # 좌우에 길이 있다을 때
            if 0 <= next_x < length and 0 <= nexy_y < length and ladder[next_x][next_y] == 1 :
                # 벽을 만나거나 0을 만나지 않는다면 계속 가라.
                while next_x != length-1 and next_x != 0 and ladder[next_x][next_y] is not 0:
                    next_x += dx[i]
                    next_y += dy[i]
                    cnt +=1
                    print(next_x, next_y)
                    

                # 만약 다음 자리가 벽이나 0이 있다면 dx[i], dy[i]만큼 돌아간 후, 아래로 이동해라
                print('here')
                next_x += dx[2] - dx[i]
                next_y += dy[2] - dy[i]
                print('-'*30)
                print(next_x, next_y)
                cnt +=1

            # 좌우에 길이 없다면 아래로 가라
            else:
                next_x += dx[2]
                next_y += dy[2]
                cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    ladder = [list(map(int, input().split())) for _ in range(100)]                
    start_pos = [idx for idx, num in enumerate(ladder[0]) if num == 1] # 시작하는 x좌표의 위치
    m_cnt = 0

    for s in start_pos:
        pos = [0, s]
        cnt = go(ladder, pos)
        if cnt > m_cnt:
            m_cnt = cnt
            result = s

    print(result)