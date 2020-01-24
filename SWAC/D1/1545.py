# 주어진 숫자부터 거꾸로 출력하기

T = int(input())

for i in range(T+1):
    if i == T:
        print(T-i)
    else:
        print(T - i, end = ' ')