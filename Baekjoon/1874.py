# stack 수열


max_num = 0
flag = 1 # res = NO check
res = list()
num_list = list()

for _ in range(int(input())):
    cur_num = int(input()) # 현재 입력값
    
    # push 연산이 필요한 경우
    if cur_num > max_num :
        for i in range(max_num+1, cur_num+1):
            res.append('+')
            num_list.append(i)
        else:
            res.append('-')
            max_num = num_list.pop()

    # pop 연산이 필요한 경우
    else:
        if cur_num in num_list:
            tmp = num_list.pop()
            res.append('-')

            while tmp != cur_num:
                tmp = num_list.pop()
                res.append('-')
            
        # if cur_num not in num_list // pop 을 할 수 없을 때
        else: 
            flag = 0
            break

if flag:
    for op in res:
        print(op)
else:
    print('NO')