for test_case in range(1, 11):
    num = int(input())
    secret_code = input()
    secret_len = int(input())
    order_code = input()
        
    # 1) order_code 를 I에 맞게 잘라준다.
    new = order_code.split('I')
    real = [i.split() for i in new[1:]]

    # 2) real [0, 1] => int
    for r in real:
        r[0] = int(r[0])
        r[1] = int(r[1])

    secret_code = secret_code.split()

    # 3) 

    for r in real:
        insert_num = r[0]
        secret_code = secret_code[:r[0]] + r[2:] + secret_code[r[0]:]

    print(f"{test_case} {' '.join(secret_code[:10])}")


    '''
    #1 449047 400905 139831 408347 512816 992679 693002 835918 768525 949227
    '''
