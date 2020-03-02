# 숫자 만들기
# 주어진 카드를 사용하여 만들 수 있는 최대/최소값 구하기
# # Rule
# # 1) 계산은 무조건 왼쪽에서 오른쪽으로.
# # 2) 순열과 조합을 사용한 완전탐색 방법을 사용

def combinations(oper_dict):
    # 모든 연산자 소진시
    if not choices:
        res.append(current_list)
        return
            
    # 연산자가 있을 경우 돌아가면서 순회
    for c in choices:
        cur_copy = current_list[:]
        cur_copy.append(c)
        oper_dict[c] -= 1
        combinations(oper_dict, cur_copy)
        oper_dict[c] += 1 

def calc(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    elif oper == '/':
        if n1 < 0 and n1 % n2:
            return n1 // n2 +1
        else:
            return n1 // n2
        
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    oper_count = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # # 1) 각 연산자와 카운트에 맞는 oper_dict 생성
    opers = ['+', '-', '*', '/']

    # # 2) 중복수열 모든 경우의 수 구하기
    res = []
    combinations(oper_dict, [])
    
    # # 3) 최대/최소값 구하기
    max_val = -999999
    min_val = 999999
    
    for r in res:    
        for idx, num in enumerate(numbers):
            if idx == 0:
                current = num
            else:
                current = calc(current, num, r[idx-1])

        if current < min_val:
            min_val = current
        if current > max_val:
            max_val = current
    result = max_val - min_val

    print(f'#{tc} {result}')