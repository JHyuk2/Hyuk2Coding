
T = int(input())

for test_case in range(1, T+1):
    text = list(input())
    H = int(input())
    point = list(map(int, input().split()))

    # pset = set(point)
    result = ''
    
    for idx, char in enumerate(text):
        if point.count(idx):
            result += '-'* point.count(idx) + char
        else:
            result += char
    else:
        if point.count(idx+1):
            result += '-'*point.count(idx+1)


    print(f'#{test_case} {result}')