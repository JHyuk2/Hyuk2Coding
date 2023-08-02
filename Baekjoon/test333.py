import sys

n = int(sys.stdin.readline())

orders =[]
for _ in range(n):
    orders.append(input().split())

stack = []
for order in orders:
    # push 인 경우
    if len(order)==2:
        stack.append(order[1])
    
    # size인 경우
    elif order[0] == 'size':
        print(len(stack))

    # push, order 가 아닌 경우
    else:
        # 스택이 들어있는 경우
        if stack:
            if order[0] == 'empty':
                print(0)
            # empty 가 아닌 경우
            elif order[0] == 'pop':
                print(stack.pop())
            elif order[0] == 'top':
                print(stack[-1])

        # 스택이 비어있는 경우
        else:
            if order[0] == 'empty':
                print(1)
            else:
                print(-1)  