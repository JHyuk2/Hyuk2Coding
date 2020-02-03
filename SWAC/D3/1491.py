
tc = int(input())

for test_case in range(1, tc+1):
    N, A, B = map(int, input().split())

    start_num = int(N**0.5)
    tmp, end_num = start_num, start_num

    while tmp * end_num <= (start_num)**2:
        end_num += 1
    
    result = []
    for R in range(start_num, start_num+2):
        for C in range(R,end_num):
            if R == (start_num +1) and C == (R+1):
                break
            else:
                tmp = A * abs(R-C) + B*abs(N - R*C)
                result.append(tmp)
    print('#{} {}'.format(test_case, result[0]))