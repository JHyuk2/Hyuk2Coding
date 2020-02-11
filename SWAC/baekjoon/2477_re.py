'''
7
3 20
1 100
4 50
2 160
3 30
1 60

7
3 0
1 160
4 50
2 160
3 50
1 0
'''
# 6방향의 이동을 받음
n = int(input())
ver = []
hor = []
d = [list(map(int, input().split())) for _ in range(6)]
for tmp in d:
    # 남북
    direction = tmp[0]
    length = tmp[1]
    if direction == 4 or direction == 3:
        ver.append(tmp)
    # 동서
    else:
        hor.append(tmp)
max_width = max(hor, key = lambda x: x[1])
max_height = max(ver, key = lambda x: x[1])
# 남북, 인덱스까지 찾았다.
width_idx = d.index(max_width)
height_idx = d.index(max_height)
find_idx = [-1, 1]
find_tmp = []
# 본체에 붙어있는 가장 긴 길이.
for i in find_idx:
    tmp_w = width_idx +i
    tmp_h = height_idx +i
    if tmp_w > 5:
        tmp_w = 0
    if tmp_h > 5:
        tmp_h = 0
    if d[tmp_w] != max_height:
        find_tmp.append(d[tmp_w])
    if d[tmp_h] != max_width:
        find_tmp.append(d[tmp_h])

cut_area_ele = [i for i in d if i != max_width and i != max_height and i not in find_tmp]
max_area = max_width[1] * max_height[1]
cut_area = cut_area_ele[0][1] * cut_area_ele[1][1]
result = (max_area - cut_area) * n
print(result)