# 배열 최소합 문제

# 1) i번째 줄에서 최소값 선택
# 2) 다음 줄로 넘어가서 선택
# 3) i == n이 되면 계산하고 종료

def arr_min(idx_list, current_sum):
    global data
    print(idx_list, current_sum)
    i = len(idx_list)

    if i == len(data):
        return current_sum
    
    # min을 먼저 찾는 게 아니라, 되는 애들 중에서 min을 찾는다.
    tmp_data = [d for idx, d in enumerate(data[i]) if idx not in idx_list]
    tmp_min = min(tmp_data)
    res = []

    for idx, j in enumerate(data[i]):
        if j == tmp_min and idx not in idx_list:
            current_sum += j
            copy_list = idx_list[:]
            copy_list.append(idx)
            res.append(arr_min(copy_list, current_sum))
            current_sum -= j

    return res

T = int(input())
for tc in range(1, T+1):
    size = int(input())
    data = [list(map(int, input().split())) for _ in range(size)]

    print(arr_min([], 0))