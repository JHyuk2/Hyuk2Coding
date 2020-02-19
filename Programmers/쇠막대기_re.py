# 이러면 1번이 계쏙 에러가남.

def solution(data):
    # 1) 모든 레이저를 L로 바꿈
    data = data.replace('()', 'L',data.count('()'))
    tmp_stack = []
    res = 0

    # 2) ( 가 나오면 1부터 시작.
    for d in data:
        # ( 이 나오면 스택에 1을 쌓는다.
        if d == '(':
            tmp_stack.append(1)
        # L 을 만나면 1씩 더한다.
        elif d == 'L':
            tmp_stack = list(map(lambda x:x+1, tmp_stack))
        # ) 을 만나면 스택에서 팝핑
        else:
            res += tmp_stack.pop()
    return res