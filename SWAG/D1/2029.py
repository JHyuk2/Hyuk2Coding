T = int(input())

for i in range(T):
    test_case = list(map(int, input().split()))
    a, b = divmod(test_case[0], test_case[1])
    
    print(f'#{i+1} {a} {b}')