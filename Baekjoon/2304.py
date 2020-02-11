# 애초에 입력받을때 max값이랑 인덱스를 찾으면서 오는게 좋을듯
n = int(input())
max_idx, max_len = 0, 0
d = []

# 1) 최고값을 찾으면서 데이터 입력.
for _ in range(n):
    tmp = list(map(int, input().split()))
    d.append(tmp)
    if tmp[1] > max_len:
        max_len = tmp[1]
        max_idx = tmp[0]

max_point = [max_idx, max_len]

# 2) 데이터를 정렬하고 최고값을 기준으로 좌우를 나눠서 봄.
tmp_list = list(sorted(d, key = lambda x: x[0])) # x[0]을 기준으로 정렬
idx_max_point = tmp_list.index(max_point)

# max기준으로 왼쪽 / 오른쪽을 나눠서 봄
# 오른쪽의 경우 reverse를 해줌 => 가장 바깥쪽에서부터 보기 위함.
# ex) (max_point) (11, 4), (13, 6), (15, 8) -> 인 경우, max를 만나기 전엔 높이 8로 고정되기 때문
left_copy = tmp_list[0:idx_max_point]
right_copy = tmp_list[:idx_max_point:-1]

# 최댓값이 몇 번이 바뀌는지 세는 함수
def max_change(arr, max_point):
    tmp_max = 0
    tmp_change = []
    for i in range(len(arr)):
        if arr[i][1] > tmp_max:
            tmp_max = arr[i][1]
            tmp_change.append(arr[i])
    else:
        tmp_change.append(max_point)

    return tmp_change

lmax_change = max_change(left_copy, max_point)
rmax_change = max_change(right_copy, max_point)

# 전체 면적을 구하는 함수.
def sum_area(max_change_arr):
    tmp_sum = 0
    length = len(max_change_arr)
    for i in range(length):
        if i != length -1:
            tmp_sum += abs(max_change_arr[i][0] - max_change_arr[i+1][0]) * max_change_arr[i][1]
    return tmp_sum

right_sum = sum_area(rmax_change)
left_sum = sum_area(lmax_change)
total = right_sum + left_sum + max_point[1]
print(total)