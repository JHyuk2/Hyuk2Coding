T = int(input())

for _ in range(T):
    test_case = input()
    year = test_case[0:3]
    month = test_case[3:5]
    day = test_case[5:]

    print(f'{year}{month}{day}')