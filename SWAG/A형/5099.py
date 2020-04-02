# 피자 굽기
'''
3
3 5 
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2

#1 4
#2 8
#3 6
'''

for tc in range(int(input())):
    size, cnt = map(int, input().split())
    cheese_list = list(map(int, input().split()))
    
    # 오븐 시작
    oven = cheese_list[:size]
    remains = cheese_list[size:]
    numbers = [i+1 for i in range(size)]

    # 현재위치
    pos = 0
    while oven.count(0) != len(oven)-1:
        if pos == len(oven):
            pos = 0
        oven[pos] //= 2
        if not oven[pos]:
            if remains:
                size +=1
                oven[pos] = remains.pop(0)
                numbers[pos] = size
        pos +=1
    res = numbers[oven.index(1)]
    print(f'#{tc+1} {res}')