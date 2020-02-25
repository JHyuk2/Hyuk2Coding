# Digit sum - 제한시간의 늪...
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    tmp_sum = 0    

    flag = True
    while True:
        if n == 0:
            if tmp_sum >= 10:
                n = tmp_sum
                tmp_sum = 0
            else:
                break
        tmp_sum += n %10
        n //= 10

    print(f'#{tc} {tmp_sum}')
