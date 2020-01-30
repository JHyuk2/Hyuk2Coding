'''
1 0 0 0 0 0 2 
0 0 0 0 1 2 0
0 0 1 0 2 0 1
1 0 0 0 0 0 0
0 0 0 1 0 2 0
2 1 2 0 0 0 0
0 0 0 2 0 0 0
'''

## 결국 1을 찾았을 때 같은 줄에서 2를 찾으면 카운트를 하나 올려주면 됨.
for test_case in range(1):
    N = int(input())
    tmp_list = []
    
    ## 1) 배열 생성
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp_list.append(tmp)
    
    rotate_tmp = list(map(list, zip(*tmp_list)))

    ## 2) 각 줄마다 실행
    result = 0
    
    # 만약 1을 찾으면 스위치 켜고, 2에서 끄고, 2가 꺼질때마다 카운트해주면 된다.
    for i in range(N):
        isN, isS = False, False
        for now in tmp_list[i]:
            if now == 1:
                isN = True
            if now == 2 and isN:
                isS = True
            if isN and isS:
                result += 1
                isN, isS = False, False

    print(f'#{test_case+1} {result}')