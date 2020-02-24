# Digit sum - so ez

'''
3
5
108
588432
'''

def digit_sum(n):
    res = 0

    while n > 0 :
        remain, m = divmod(n, 10)
        res += m
        n = remain

    return res


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    
    while n >= 10:
        n = digit_sum(n)
    
    print(f'#{tc} {n}')