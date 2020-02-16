# 1) pos(리스트 위의 한 점) 기준으로 가로세로 length만큼의 합을 구하는 함수.

def cross_sum(fla_list, pos):
    x = pos[0]
    y = pos[1]
    length = fla_list[x][y]
    if length == 0:
        return 0
    
    #    북 동 남 서
    dx =[-1, 0, 1, 0 ]
    dy =[0, 1 , 0, -1]
    result = 0
    
    # 네 방향을 살펴보는데,
    for i in range(4):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        tmp_sum = 0
        # length번 만큼 반복하는데, 만약 tmp_x, tmp_y가 벽을 넘어가면 실행하지 않아야함.
        # 양쪽 끝값은 각각 0 ~ N-1, 0~M-1 => N = len(fla_list), M = len(fla_list[0])
        for j in range(length):
            if 0<= tmp_x <len(fla_list) and 0 <= tmp_y < len(fla_list[0]):
                tmp_sum += fla_list[tmp_x][tmp_y]
                tmp_x += dx[i]
                tmp_y += dy[i]
                continue
            # 범위를 넘어가는 경우
            else:
                result += tmp_sum # 일단 확인용.
                break
        
        # for문이 break를 만나지 않고 끝난 경우
        else:
            result += tmp_sum
    
    # 마지막으로 pos의 값을 더해줌
    result += fla_list[x][y]
    return result

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fla_list = [list(map(int, input().split())) for _ in range(N)]
    res_max = 0
    
    for i in range(N):
        for j in range(M):
            tmp_max = cross_sum(fla_list, [i, j])
            if tmp_max > res_max:
                res_max = tmp_max
    
    print('#{} {}'.format(tc, res_max))