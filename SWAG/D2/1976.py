T = int(input())

for test_case in range(1, T+1):
    hour1, min1, hour2, min2 = tuple(map(int, input().split())) # 각 값을 튜플로 받음
    
    now_h = hour1 + hour2
    now_m = min1 + min2

    if now_m >= 60:
        now_m -= 60
        now_h += 1

    if now_h >= 13: # 1~12까지의 정수만 허용
        now_h -= 12

    print(f'#{ test_case } { now_h } { now_m }')
    