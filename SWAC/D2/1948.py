# 날짜 계산하기

T = int(input())

def many_days(month, day):
    calander = {
            '1':31,
            '2':28,
            '3':31,
            '4':30,
            '5':31,
            '6':30,
            '7':31,
            '8':31,
            '9':30,
            '10':31,
            '11':30,
            '12':31,
        }
    
    tmp = 0
    for m1 in range(1, month): 
        for mon, days in calander.items():
            if str(m1) == mon:
                tmp += days
    return tmp+day

for test_case in range(1, T+1):
    month1, day1, month2, day2 = tuple(map(int, input().split()))

    first = many_days(month1, day1)
    second = many_days(month2, day2)
    
    result = second - first + 1
    print(f'#{ test_case } { result }')