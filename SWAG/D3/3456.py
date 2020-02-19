
T = int(input())

for test_case in range(1, T+1):
    N = list(map(int, input().split()))

    for num in N:
        if N.count(num) %2:
            result = num
            break
        
    print(f'#{ test_case } { result }')
    