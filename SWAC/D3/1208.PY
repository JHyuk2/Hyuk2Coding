# 테스트케이스 10
# 각 줄의 입력은 입력받는 수 & 값

def flatten(input_list): # 평탄화 작업 한번.
    high = max(input_list)
    low = min(input_list)
    
    high_idx = input_list.index(high)
    low_idx = input_list.index(low)
    flag = 1
    result = high-low
    if (result) > 1:
        input_list[high_idx] -= 1
        input_list[low_idx] += 1

    elif (result) <= 1:
        if abs(input_list.count(high) - input_list.count(low)) % 2: # 평탄화 가능한 게 1임.
            result = 1 #멈춰야됨
            flag = 0            
        else: # 
            result = 0
    
    result = max(input_list)-min(input_list)
    return input_list, flag, result
    
for test_case in range(10):
    dump = int(input()) # 평탄화 가능회수 입력받음
    tmp_list = list(map(int, input().split())) 
    cnt = 0

    for i in range(dump):
        cnt +=1
        tmp_list, flag, result = flatten(tmp_list)
        if flag == 0:
            break
    
    print(f'#{ test_case +1 } { result }')