
calendar = {
    '1':31,
    '2':29,
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

# 왜만들었니
week = {
    '0':'월요일',
    '1':'화요일',
    '2':'수요일',
    '3':'목요일',
    '4':'금요일',
    '5':'토요일',
    '6':'일요일',
}

T = int(input())

for test_case in range(1, T+1):
    month, day = map(int, input().split())
    # month 1일때만 0에서 스타트,
    # 2/1 인경우 31+1 만큼 차이남
    
    if month == 1:
        result = (day-1) % 7
    else:
        tmp = 0
        for mon,days in calendar.items():
            if int(mon) < month:
                tmp += days
        tmp += day
        result = (tmp-1)%7
    
    
    print()