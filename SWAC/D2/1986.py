# 짝수일 때 더하고, 홀수일 때 뺀 값 구하기.

T = int(input())

for test_case in range(T):
    N = int(input())
    result = 0

    for n in range(1, N+1):
        if n % 2: #n이 홀수일 경우
            result += n
        else:
            result -= n

    print(f'#{ test_case +1 } { result }')