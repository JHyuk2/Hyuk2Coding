
T = int(input())

for test_case in range(1, T+1):
    N = input() ## 원본
    tmp = '0'
    cnt = 0
    
    for n in N:
        if n != tmp:
            tmp = n
            cnt +=1

    print(f'#{ test_case } { cnt }')
    