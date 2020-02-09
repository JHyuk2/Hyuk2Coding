# 당근수확 2
import math

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    move = 0
    quotient, remains = 0, 0
    
    for idx, num in enumerate(tmp):
        num += remains
        quotient, remains = divmod(num, M)
        if idx == len(tmp)-1:
            quotient = math.ceil(num/M)
        move += quotient * (idx+1) * 2
    
    print('#{} {}'.format(tc, move))
