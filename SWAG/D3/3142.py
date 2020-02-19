
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 뿔, M:동물
    twin = N - M
    uni = M - twin

    print(f'#{test_case} { uni} {twin}')
    