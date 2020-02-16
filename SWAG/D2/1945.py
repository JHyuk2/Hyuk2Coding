# N = power(2, a) * power(3, b) * power(5, c) * power(7, d) * power(11, e)

T = int(input())

for test_case in range(1, T+1):
    num = int(input())
    numbers = [2, 3, 5, 7, 11]
    cnt_list = []

    while num != 1:
        for n in numbers:
            cnt = 0
            while (num%n) == 0:
                cnt +=1
                num /=n
            # while문이 끝났을 때,
            cnt_list.append(cnt)
    
    print(f'#{ test_case } { " ".join(list(map(str, cnt_list))) }')