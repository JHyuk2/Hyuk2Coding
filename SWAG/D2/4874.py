# forth

def calc(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    # 나눗셈은 항상 나누어 떨어진다는 조건이 있기 때문에, int값으로 리턴
    elif oper == '/':
        return n1 // n2
    # oper == '.'
    else:
        return 

T = int(input())

for tc in range(1, T+1):
    data = list(input().split())
    oper = ['+', '-', '*', '/']
    stack = []
    flag = 1

    # # 1) 숫자를 만났을 때 스택에 넣기
    for idx, d in enumerate(data):
        if d.isdecimal():
            stack.append(int(d))

        # # 1-1) 연산자 or .인 경우
        else:
            # # 1-2) 숫자 둘 + 연산자 조합
            if d in oper and len(stack) >= 2:
                n2 = stack.pop() # 뒤
                n1 = stack.pop() # 앞
                stack.append(calc(n1, n2, d))
            
            # # 1-3) 숫자 하나 + 연산자
            elif d in oper and len(stack) <2:
                flag = 0
            
            # # 2) '.'을 만났을 때 ~ 마지막
            elif d == '.':
                # # 2-1) 비정상
                if flag == 0 or flag and len(stack) >1:
                    result = 'error'

                # # 2-2) 정상
                elif flag:
                    result = stack.pop()
    print(f'#{tc} {result}')