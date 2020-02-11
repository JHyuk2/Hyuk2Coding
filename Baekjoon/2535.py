# 수 이어가기

num = int(input())

def connected_num(n, i = 1):
    global num
    if n == 1:
        return num
    elif n == 2:
        return i
    else:
        return connected_num(n-2, i) - connected_num(n-1, i)
result_list = []

# 나올 수 있는 모든 결과물들 result_list에 때려박음.
max_len = 0
for i in range(1, num+1):
    n = 1
    tmp_list = []
    while connected_num(n, i) >= 0:
        tmp_list.append(connected_num(n, i = i))
        n += 1
    
    # max_len값 찾아주기.
    if len(tmp_list) > max_len:
        max_len = len(tmp_list)

    # 모든 결과값 일단 result 에 입력.
    result_list.append(tmp_list)

# result 중 len이 max_len인 것 중 가장 먼저 오는 것 출력.
for result in result_list:
    if len(result) == max_len:
        print(max_len)
        print(' '.join(map(str, result)))
        
