'''
7
3 30
1 60
3 20
1 100
4 50
2 160
'''
N = int(input())
elem = [list(map(int, input().split())) for _ in range(6)]
w = [l for d, l in elem if d == 2 or d == 1]
h = [l for d, l in elem if d == 3 or d == 4]
max_w = 0
max_w_idx = 0
max_h = 0
max_h_idx = 0
for idx, (d, l) in enumerate(elem):
    if d in (1, 2) and l > max_w:
        max_w = l
        max_w_idx = idx    
    elif d in (3, 4) and l > max_h:
        max_h = l
        max_h_idx = idx 
tot_area = max_w * max_h
find_idx = [-1, 1]

for i in range(2):
    check_w = elem[max_h_idx + find_idx[i]][1]
    if check_w != max_w:
        cut_w = max_w - check_w
        break
for i in range(2):
    check_h = elem[max_w_idx + find_idx[i]][1]
    if check_h != max_h:
        cut_h = max_h - check_h
        break    
cut_area = cut_w * cut_h
result = N * (tot_area - cut_area)
print(result)