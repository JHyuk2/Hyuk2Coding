T = int(input())

for test_case in range(1, T+1):
    N, S = map(int, input().split())

    tot = [i+1 for i in range(N)]
    S = list(map(int, input().split()))
    result = [str(i) for i in tot if i not in S]

    real = ' '.join(result)
    print(f'#{ test_case } { real }')  