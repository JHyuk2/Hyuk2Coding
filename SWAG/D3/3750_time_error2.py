# Digit sum - so ez

'''
3
5
108
588432
'''


T = int(input())

for tc in range(1, T+1):
    # 인풋할 때 자릿수로 나눠서 받고, int -> sum
    n = sum(list(map(int, input())))

    # 자리수별로 나눠서 다시 합치기 반복    
    while n >= 10:
        n = sum(map(int, list(str(n))))

    print(f'#{tc} {n}')