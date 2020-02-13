# 이러면 1번이 계쏙 에러가남.

def solution(data):
    # 1) 모든 레이저를 L로 바꿈
    data = data.replace('()', 'L',data.count('()'))
    tmp_stack = []
    res = 0

    # 2) ( 가 나오면 1부터 시작.

    for d in data:
        if d == '()':
            tmp_stack.append(1)
        elif d == 'L':
            tmp_stack = list(map(lambda x:x+1, tmp_stack))
        else:
            res += tmp_stack.pop()
    return res