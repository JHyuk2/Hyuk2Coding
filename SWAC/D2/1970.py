T = int(input())

for test_case in range(1, T+1):
    money = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []


    for m in change:
        n, remain = divmod(money, m)
        result.append(n)
        money = remain
    
    result = ' '.join(list(map(str, result)))
    print(f'#{ test_case }\n{ result }')