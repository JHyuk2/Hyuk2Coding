#  https://www.acmicpc.net/group/practice/view/18210/3

N = int(input())

cnt = 0
res = 0
flag = 0

while True:
    # N < 3인경우
    if N < 3:
        if N == 0:
            break
        else : # N%3
           flag = 1
           break
    # N >= 3
    if str(N)[-1] in '05':
        cnt += N//5
        break
    else:
        N -= 3
        cnt +=1

# Check flag
if flag :
    res = -1
else:
    res = cnt
print(res)