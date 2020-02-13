# 반복문자 지우기

T = int(input())

for tc in range(1, T+1):
    data = input()
    stack = []

    for d in data:
        # is empty
        if not bool(stack):
            stack.append(d)
        else:
            if stack[-1] == d:
                stack.pop()
            else:
                stack.append(d)

    print('#{} {}'.format(tc, len(stack)))