# 이러면 1번이 계쏙 에러가남.

def solution(data):
    # 1) 모든 레이저를 L로 바꿈
    data = data.replace('()', 'L',data.count('()'))
    stack = []
    tmp_stack = []
    res = 0
    cnt = 0

    # 2) 일단 모두 스택에 담은 후, )를 만나면 stack에서 (가 나올때까지 다 꺼낸다.
    # 도중에 나오는 L은 모두 tmp_stack에 담아놓는다.

    for d in data:
        # 스택이 비어있을 땐, L이 들어와도 안받음.
        if not bool(stack):
            if d == 'L':
                continue

        # 일단 다 때려넣는다.
        if d != ')':
            stack.append(d)

        # 오른쪽인 경우 (를 만날 때까지 다 뽑는다.
        else:
            while True:
                tmp = stack.pop()
                if tmp == '(':
                    cnt = len(tmp_stack)
                    res += cnt+1
                    # 꺼낸 L 다시 넣어줌.
                    stack += tmp_stack
                    tmp_stack = []
                    break
                else:
                    tmp_stack.append(tmp)
    return res