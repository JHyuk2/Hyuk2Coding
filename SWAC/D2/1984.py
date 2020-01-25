T = int(input())

for test_case in range(1, T+1):
    numbers = list(map(int, input().split()))
    new_list = sorted(numbers)[1:-1] #0번째와 마지막 값은 뺀 리스트.
    result = round(sum(new_list) / len(new_list)) # float값

    print(f'#{ test_case } { result }')