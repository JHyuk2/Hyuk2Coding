#  https://www.acmicpc.net/group/practice/view/18210/3

papers = []
canvas = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(int(input())):
    papers.append(tuple(map(int, input().split())))

top = 0

for j, i in papers:
    left = j
    right = j+10
    bottom = i
    up = i+10
    
    if up > top:
        top = up

    for idx in range(bottom, up):
        canvas[idx][left:right] = [1 for _ in range(10)]

cnt = 0
for idx in range(top):
    cnt += sum(canvas[idx])

print(cnt)