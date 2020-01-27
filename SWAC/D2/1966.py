# 너무쉬운데..?

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    numbers = sorted(list(map(int, input().split())))
    result = ' '.join(list(map(str, numbers)))

    print(f'#{ test_case } { result }')