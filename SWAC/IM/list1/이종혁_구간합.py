T = int(input())

## 이웃한 M개의 합...이었네?
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    
    for i in range(len(numbers)-M+1):
        tmp_sum = sum(numbers[i:i+M])
        if i == 0:
            max_sum, min_sum = tmp_sum, tmp_sum
        else:
            if tmp_sum > max_sum:
                max_sum = tmp_sum
            elif tmp_sum < min_sum:
                min_sum = tmp_sum

    result = max_sum - min_sum
    print(f'#{test_case} {result}')