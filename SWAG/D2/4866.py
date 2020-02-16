# 괄호검사

T = int(input())
for tc in range(1, T+1):
    data = input()
    stack = []
    flag = 1

    for d in data:
        if d == '(' or d == '{' :
            stack.append(d)
        elif d == ')':
            # is not empty
            if bool(stack):
                if stack.pop() == '(':
                    continue
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
        elif d == '}':
            # is not empty
            if bool(stack):
                if stack.pop() == '{':
                    continue
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
    # (,{ 남은 경우
    else:   
        if bool(stack):
            flag = 0

    print('#{} {}'.format(tc, flag))