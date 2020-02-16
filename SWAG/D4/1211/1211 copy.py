# 사다리 타기

# import sys
# sys.stdin = open('C:/Users/dm705/Hyuk2Coding/Hyuk2Coding/SWAC/D4/1211/input.txt')

def climb(start_point, ladder):
    x = start_point
    y = 0
    cnt = 1
    length = len(ladder)
    
    while y < length-1:
        # 오른쪽에 길이 있는 경우
        if 0 <= x+1 < length and ladder[y][x+1] == 1:
            while 0 <= x + 1 < length and ladder[y][x+1] == 1:
                x += 1
                cnt += 1
            # while문 탈출시
            else:
                y += 1
                cnt +=1
        
        # 왼쪽에 길이 있는 경우
        elif 0 <= x-1 < length and ladder[y][x-1] == 1:
            while 0 <= x-1 < length and ladder[y][x-1] == 1:
                x -= 1
                cnt += 1
            else:
                y += 1
                cnt += 1

        
        # 아무것도 없는 경우
        else:
            y += 1
            cnt += 1
    return cnt

for tc in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    # 시작위치 모음
    start_list = [idx for idx, num in enumerate(ladder[0]) if num == 1] 
    m_num = 100000

    for idx, s in enumerate(start_list):
        tmp = climb(s, ladder)
        # print(s, tmp)
        if tmp < m_num:
            m_num = tmp
            result = s
    
    print('#{} {}'.format(tc+1, result))