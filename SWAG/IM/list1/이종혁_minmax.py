T = int(input())

for test_case in range(1, T+1):
    N = int(input()) #개수
    numbers = list(map(int, input().split()))

    max_num = 0
    for idx, num in enumerate(numbers):
        if idx == 0:
            max_num, min_num = num, num
        else:
            if num > max_num:
                max_num = num
            elif num < min_num:
                min_num = num
    result = max_num - min_num

    print(f'#{ test_case } { result }')
        