#  https://www.acmicpc.net/group/practice/view/18210/3

N, M = map(int, input().split())

li_first = []
li_second = []
for idx in range(2*N):
    if idx <N:
        li_first += list(map(int, input().split()))
    else:
        li_second += list(map(int, input().split()))

temp_list = list(map(sum, zip(li_first, li_second)))

for i in range(N):
    for j in range(M):
        idx = M*i + j
        print(temp_list[idx], end=' ')
    print()