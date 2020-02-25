# 계산기 -3
# 후위표기법 계산 - 스택 이용하면 될거같음

'''
1) 각각 num_stack, oper_stack으로 나누어서 진행
2) '*' => 즉각적으로 계산
3) '(' && ')' => '('를 만날 때까지 스택 계산 진행
4) 마지막까지 가면 종료
'''

# 총 10개 의 tc

def calc():
    n1 = num_stack.pop()
    n2 = num_stack.pop()
    oper = oper_stack.pop()

    if oper =='+':
        return n1+n2
    if oper == '*':
        return n1*n2

for tc in range(1):
    n = int(input())
    data = input() # str으로 처리

    # 준비물
    num_stack = []
    oper_stack = []
    oper = ['+', '*', '(', ')']
    result = 0
    flag = 0
    for d in data:
        # 1) 숫자는 그냥 넘스택에 담기
        if d not in oper:
            num_stack.append(int(d))
            if flag ==1:
                num_stack.append(calc())
                flag = 0
        # 2) 연산자인 경우
        else:
            # 괄호 -> '('를 만날 때까지 계산
            if d == ')':
                # oper_stack.top() != '(':     // [ex => '+']
                while oper_stack[-1] != '(':
                    num_stack.append(calc())        
                # '('를 만났을 때
                else:
                    oper_stack.pop()
            # d == '*'
            elif d == '*':
                flag = 1
                oper_stack.append(d)
                
            # d == '(' or '+'
            else:
                oper_stack.append(d)
    
    # for-else // 괄호는 없지만 계산이 필요한 경우
    else:
        while oper_stack:
            num_stack.append(calc())
    
    print(num_stack[0])
