T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))
    length = abs(N-M)
    max_sum = 0
    
    if N < M:
        for i in range(length+1):
            tmp = list_m[i:i+N]
            tmp_sum = 0
            for j in range(N):
                tmp_sum += list_n[j] * tmp[j]
            max_sum = tmp_sum if tmp_sum > max_sum else max_sum
        
        
    else: # N > M 인 경우
        for i in range(length+1):
            tmp = list_n[i:i+M]
            tmp_sum = 0
            for j in range(M):
                tmp_sum += list_m[j] * tmp[j]    
            max_sum = tmp_sum if tmp_sum > max_sum else max_sum
        
    print(max_sum)