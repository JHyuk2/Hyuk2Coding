# tmp = [1,2,3,4,5,6]

# if tmp.pop() == 6: # 비교할 때 pop을 써도 연산이 된다!!!
#     print(tmp)

n = int(input())
for _ in range(n):
    stack = []
    data = list(input())
    flag = 'YES'

    for d in data:
        if d == '(':
            stack.append(d)
        else:
            if bool(stack):
                stack.pop()
                continue
            
            else:
                flag = 'NO'
                break
    else:
        if bool(stack):
            flag = 'NO'
            
    print(flag)