T = int(input())
tmp = []

for i in range(1, T+1):
    if T %i == 0:
        tmp.append(i)

print(' '.join(list(map(str, tmp))))