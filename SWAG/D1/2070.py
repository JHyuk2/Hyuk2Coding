""" 
- 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

test_case
3
3 8 
7 7 
369 123 
"""

T = int(input())

for i in range(T):
    test_case = list(map(int, input().split()))
    a = test_case[0]
    b = test_case[1]

    if a>b:
        result = '>'
    elif a<b:
        result = '<'
    else: #a ==b
        result = '='

    print(f'#{i+1} {result}')