# sheep세기 문제...

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    numbers = [i for i in range(10)] # 0~9
    cnt = 0

    while numbers != [] : # 비어있지 않으면 계속 반복
        cnt +=1
        tmp = [int(s) for s in str(cnt * N)] # 1234 => 1,2,3,4 로 나눔
        
        for t in tmp:
            if t in numbers:
                numbers.remove(t)
        
    print(f'#{ test_case } { cnt * N }')