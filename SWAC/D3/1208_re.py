# 테스트케이스 10
# 각 줄의 입력은 입력받는 수 & 값
    
for test_case in range(10):
    dump = int(input()) # 평탄화 가능회수 입력받음
    tmp_list = list(map(int, input().split())) 
    cnt = 0
	max_num, min_num = 0, 0
    

            
    for i in range(dump):
        ## 맥스값 찾기.
        for idx, num in enumerate(tmp_list):
            if num > maxnum:
                max_num = num
                max_idx = idx
            elif num < minnum:
                min_num = num
                min_idx = idx

        tmp_list[min_idx] += 1
        tmp_list[max_idx] -= 1
        result = tmp_list[max_idx] - tmp_list[min_idx]
    
    
    print(f'#{ test_case +1 } { result }')