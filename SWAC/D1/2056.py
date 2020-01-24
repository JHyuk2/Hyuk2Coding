T = int(input())


calendar = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}


for i in range(T):
    test_case = input()
    year = test_case[0:4]
    month = test_case[4:6]
    day = test_case[6:]

    # print(f'{year}{month}{day}')

    if month not in calendar.keys():
        print(f'#{i+1} {-1}')
    else:
        if int(day) not in range(calendar[month] +1):
            print(f'#{i+1} {-1}')
        else:
            print(f'#{i+1} {year}/{month}/{day}')
    