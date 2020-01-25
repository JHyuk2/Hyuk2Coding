# N by N 행렬
# 길이가 K인 단어가 들어갈 수 있는 자리 모두 찾기.

'''
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''

T = int(input())

for test_case in range(1, T+1):
    N, k = tuple(map(int, input().split()))
    temp_list = [[] for _ in range(N)]

    # 1) 배열 생성 및 값 입력
    for n in range(N):
        temp_list[n] = list(map(int, input().split()))

    # 2) 단어의 최대길이 n에 따라 몇 개의 단어가 들어갈 수 있는지 count
    count_dict = {
        str(i):0 for i in range(2, N+1) # 2, 3, 4, 5
    }

    
    # 0의 바로 오른쪽에서만 출발 가능하다. but, len =1 인경우는 불가능하다.
    for i in range(N):
        for j in range(N):
            k = N-j
            if j==0 and (temp_list[i][j] == 1): # 가로 search 가능한 경우
                count = sum(temp_list[i][j:k])
            elif (temp_list[i][j-1] == 0) and (temp_list[i][j] == 1): 
                count = sum(temp_list[i][j:k])
                
                if count != 1:
                    count_dict[str(count)] += 1
            elif (temp_list[i][j] == 1) and (temp_list[i-1][j]==0 or i==0) : # 세로 search 가능한경우