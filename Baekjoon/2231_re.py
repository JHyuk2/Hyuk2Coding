# 분해합
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