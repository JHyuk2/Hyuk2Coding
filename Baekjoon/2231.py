# 분해 합

'''
    규칙을 구해야겠네.
    1) 한자리수 자연수인 경우
    - 불가능, 즉 고려해야 할 범위가 아니다.

    2) N이 두 자릿 수 자연수
    - M + divmod(M, 10) == N을 만족하는 두 자릿수.
    - 여기부터 구해보면 어떨까?

    3) N이 세 자릿 수 이상인 경우
    - 가장 쉬운 접근법은, m자리 수의 숫자라고 둘 때, 9*m 만큼 작은 범위에서부터 모두 구해보는 방법.
    3-1)
    - 맨 앞자리 숫자를 a라고 둘 때, a + 9*(m-1) 만큼의 범위만큼이 최대거리라고 볼 수 있겠다.
'''


def assemble(num):
    tmp = list(map(int, str(num))) # str으로 바꿔지면 자릿수별로 쪼개기 쉽다.
    tmp_sum = sum(tmp) # map함수를 통해 int로 바꿔준 후
    return num + tmp_sum

# main 함수

# N의 가장 작은 생성자를 구하는 게 목표이기 때문에, 구해지는 경우 거기서 종료
N = int(input())
l = len(str(N))
res = 0

if l < 1:
    pass

else:
    distance = (l-1) * 9 + int(str(N)[0]) - 1
    min_num = N - distance
    if min_num < 10:
        min_num = 10 
    for i in range(min_num, N):
        if N == assemble(i):
            res = i
            break
print(res)