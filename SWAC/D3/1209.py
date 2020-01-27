
# 가로합
def horizontal_list(tmp_list):
    temp = []
    for i in range(len(tmp_list)):
        temp.append(sum(tmp_list[i]))
    return temp

# 세로합
def vertical_list(tmp_list):
    rotate_tmp = list(zip(*tmp_list))
    temp = []
    for i in range(len(tmp_list)):
        temp.append(sum(rotate_tmp[i]))
    return temp    

# 대각합
def diagnoal_list(tmp_list):
    right_sum, left_sum = 0 , 0
    temp = []
    for i in range(len(tmp_list)):
        for j in range(len(tmp_list)):
            if i == j:
                left_sum += tmp_list[i][j]
            elif (i+j) == (len(tmp_list)-1):
                right_sum += tmp_list[i][j]

    temp.append(right_sum)
    temp.append(left_sum)
    return temp


#메인함수
for test_case in range(10):
    t = int(input())

    tmp_list = []
    for _ in range(100):
        tmp = list(map(int, input().split()))
        tmp_list.append(tmp)

    # 가로합
    horizontal = []
    vertical = []
    diagonal = []


    horizontal = horizontal_list(tmp_list)
    vertical = vertical_list(tmp_list)
    diagonal = diagnoal_list(tmp_list)
    result = max(horizontal + vertical + diagonal)
    
    print(f'#{ t } { result }')