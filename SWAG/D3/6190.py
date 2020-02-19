# 단조 증가

def isDanjo(num):
    tmp_list = []
    a = num
    while num > 0:
        tmp = num%10
        tmp_list.append(tmp)
        num = num // 10

    for i in range(len(tmp_list)-1):
        if tmp_list[i] < tmp_list[i+1]:
            return a, False
        else:
            continue
    return a, True
 

T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 입력받을 개수
    tmp_list = sorted(list(map(int, input().split())), reverse=True) # 높은순서대로 정렬
    
    max_num = -1
    for i in range(len(tmp_list)-1):
        for n2 in tmp_list[i+1:]:
            tmp = tmp_list[i] * n2

            num, TF = isDanjo(tmp)

            if TF:
                if num > max_num:
                    max_num = num
                    
    print(f'#{test_case} {max_num}')