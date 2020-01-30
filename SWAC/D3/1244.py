'''
3
123 1
2737 1
32888 2
'''

T = int(input())

for test_case in range(1, T+1):
    a, n = input().split()
    temp_list = list(a)
    cnt = int(n)
    N = len(tmp)

    # 가장 큰 수랑 비교
    max_result = sorted(a, reverse = True) # 최적해
    
    tmp = []
    temp_list_copy = temp_list[:]

    # 1) max값과 원본 비교 후 같은 자리에 있는 건 교체할 필요 없음
    for idx, num in enumerate(temp_list):
        if max_result[idx] == temp_list[idx]:
            tmp.append(idx) # 같은 인덱스에 대해서 저장.
            del temp_list_copy[idx]
            del max_result[idx]
    
    # 2) 남은 것들을 가지고 비교.
    for idx, num in enumerate(tmp_list_copy):
        if temp_list_copy[0]




                
            # 최적해가 아닐 경우




    ## 내가 생각한 방법대로 해보자.
    #    88753
    #    32888 => 2
    # 1) 82838
    # 2) 