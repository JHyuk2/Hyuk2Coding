#  2 2 123456 123456 ## 삽입
# d 4 4 # 4번째 위치로부터 4개 삭제.

# 1) I, D를 만난 경우 그 앞에서 자르기.
def split_IDA(text):
    cnt = 0
    tmp_list = []

    for idx, t in enumerate(text):
        if idx == 0:
            continue        
        elif idx == len(text)-1:
            tmp = text[cnt:]
            tmp_list.append(tmp.split()) 
        elif t == 'I' or t == 'D' or t == 'A':
            tmp = text[cnt:idx].rstrip()
            tmp_list.append(tmp.split())
            cnt = idx

    for ls in tmp_list:
        if ls[0] == 'I' or ls[0] == 'D':
            ls[1] = int(ls[1]) # 삽입할 위치
            ls[2] = int(ls[2]) # 삽입할 개수.
        else: # ls[0] == 'A'
            ls[1] = int(ls[1])

    return tmp_list

# I, D 에 따라 입력 / 삭제
def ins_del_add(secret_code, order_list): # 둘 다 리스트임
    if order_list[0] == 'I':
        insert_num = order_list[1]
        secret_code = secret_code[:insert_num] + order_list[3:] + secret_code[insert_num:]
    
    elif order_list[0] == 'D':
        del_num = order_list[1]
        del_count = order_list[2]
        
        for _ in range(del_count):
            del secret_code[del_num] # 지워짐.

    else: # order_list[0] = 'A'
        secret_code = secret_code + order_list[2:]
        
    return secret_code
        

# --------------- main func ------------------#

# 테스트 케이스는 10개
for test_case in range(10):
    N = int(input())
    secret_code = input().split()
    order_num = int(input())
    orders = input()

    # 1) orders를 들어온 주문에 맞게 잘라주기
    orders = split_IDA(orders)
    
    for order_list in orders:
        secret_code = ins_del_add(secret_code, order_list)
    

    print(f"#{ test_case +1 } { ' '.join(secret_code[:10]) }")
