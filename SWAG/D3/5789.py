T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    tmp = [0 for _ in range(N)]
    
    num = 0
    for _ in range(Q):
        num += 1
        L, R = map(int, input().split())
        tmp[L-1:R] = [num]*(R-L+1)

        
    tmp = [str(i) for i in tmp]
    print(f'#{ test_case } { " ".join(tmp) }') 