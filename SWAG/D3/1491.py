import math

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())

    # 최대로 가능한 마지막 순서
    max_a = int(math.sqrt(N))
    res = 999999999

    for i in range(1, max_a+1):
        max_b = N//i
        for j in range(i, max_b+1):
            tmp = A * abs(i-j) + B*(N-i*j)
            if tmp < res:
                res = tmp
    print(f'{tc} {res}')