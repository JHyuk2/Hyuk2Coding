# N, M, K (오는 손님, M초의 시간으로 K개의 붕어빵을 만든다.)
# 손님이 오는 시간 리스트

T = int(input())

for test_case in range(1, T+1):

    N, M, K = map(int, input().split())       # 손님 수, M초당 K개
    waiting = sorted(list(map(int, input().split()))) # 손님 오는 시간_오는순서대로 받기 위해 오름차순

    for idx, time in enumerate(waiting):
        now = K * (time // M) # 현재 보유량
        if now < idx+1: # 지금까지 온 손님 수 (idx+1)
            result = 'Impossible'
            break
    else:
        result = 'Possible'

    print(f'#{ test_case } { result }')