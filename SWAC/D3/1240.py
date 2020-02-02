num_code = {
    "0001101":0,
    "0011001":1,
    "0010011":2,
    "0111101":3,
    "0100011":4,
    "0110001":5,
    "0101111":6,
    "0111011":7,
    "0110111":8,
    "0001011":9,
}

T = int(input())

for test_case in range(1,T+1):
    height, width = map(int, input().split())
    secret_code =[]

    for _ in range(height):
        tmp = input()
        secret_code.append(tmp)

    result = []
    for h in range(height):
        w = 0
        if '1' not in secret_code[h]:
            continue
        else:
            while w < width-6:
                tmp_code = secret_code[h][w:w+7]
                if tmp_code in num_code:
                    if result == []:
                        for j in range(1, 3):
                            if secret_code[h][w+j:w+j+7] in num_code and secret_code[h][w+56] == 1:
                                w += j
                                tmp_code = secret_code[h][w:w+7]
                    result.append(num_code[tmp_code])
                    w += 6
                else:
                    w += 1 
            break
    
    #check
    if len(result) == 8:
        odd = [num for idx, num in enumerate(result[:7]) if not idx%2]
        even = [num for idx, num in enumerate(result[:7]) if idx%2]
        check = result[7]

        isSecret = True if (sum(odd) * 3 + sum(even) + check) %10 ==0 else False

        if isSecret: #True인 경우
            print(f'#{test_case} {sum(result)}')
        else:
            print(f'#{test_case} {0}')
        