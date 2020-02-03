tc = int(input())

for test_case in range(1, tc+1):
    N, M = map(int, input().split())
    arr = []
    
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    print(arr)
    result = []
    
    for x in range(N-M+1):
        for y in range(N-M+1):
            group_sum = 0
            for j in range(M):
               tmp = arr[x+j][y:y+M] 
               group_sum += sum(tmp)
            
            result.append(group_sum)
    
    print('#{} {}'.format(test_case, max(result)))