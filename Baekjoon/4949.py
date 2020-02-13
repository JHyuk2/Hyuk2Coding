datas = []

# 데이터 입력받기.
while True:
    tmp = input()
    if tmp == '.':
        break
    datas.append(tmp)

# 결과 담을 통
res = []
for data in datas:
    
    flag = 'yes'
    stack = []
    for d in data:
        # 괄호 스택에 다 때려박기
        if d == '(' or d == '{' or d == '[' :
            stack.append(d)

        # 소괄호 비교
        elif d == ')':
            # is not empty
            if bool(stack):
                if stack.pop() == '(':
                    continue
                else:
                    flag = 'no'
                    res.append(flag)
                    break
            else:
                flag = 'no'
                res.append(flag)
                break

        # 중괄호 비교
        elif d == '}':
            # is not empty
            if bool(stack):
                if stack.pop() == '{':
                    continue
                else:
                    flag = 'no'
                    break
            else:
                flag = 'no'
                res.append(flag)
                break

        # 대괄호 비교
        elif d == ']':
            # is not empty
            if bool(stack):
                if stack.pop() == '[':
                    continue
                else:
                    flag = 'no'
                    res.append(flag)
                    break
            else:
                flag = 'no'
                res.append(flag)
                break
    # 연산 종료 시
    # 스택에 (,{,[ 가 남은 경우
    else:   
        if bool(stack):
            flag = 'no'
        res.append(flag)

for result in res:
    print(result)