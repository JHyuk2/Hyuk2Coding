T= int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split())) #충전

    tmp = [1 if i in charge else 0 for i in range(N+1)] # N 길이만큼의 리스트 생성
    ## 0 출발은 의미없음.

    cnt = 0
    stop = 0
    while stop < N-1: #끝까지 가지 않으면 반복
        if 1 in tmp[stop+1:stop+1+K]:
            for k in range(K):
                if tmp[stop+1+k] == 1:
                    a = stop+1+k 
            stop = a # 가장 뒤에 있는 1을 찾아서 이동
            cnt += 1
            if stop + K >= N: #ex stop 8, K = 3, N = 10
                break    

        else: # 1 not in tmp"
            cnt = 0
            break

    print(f'#{test_case} {cnt}')
            
