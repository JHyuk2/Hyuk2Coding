T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tmp_list = list(map(int, input().split()))
    result = []
    tmp_res = []

    for idx, num in enumerate(tmp_list):
        if idx == 0:
            tmp_res.append(num)
        else:
            if num > tmp_list[idx-1]:
                tmp_res.append(num)
            else:
                if len(tmp_res) >= 2:
                    result.append(tmp_res)
                tmp_res = [num]
    else:
        if len(tmp_res) >= 2:
            result.append(tmp_res)
    # 긴 줄기들만 담은 result 생성
    res_max = 0
    max_len = 0
    for r in result:
        tmp_len = len(r)
        if tmp_len > max_len:
            max_len = tmp_len
            res_max = sum(r)
        elif tmp_len == max_len:
            res_max = sum(r) if sum(r) > res_max else res_max
                
    print('#{} {} {}'.format(tc, len(result), res_max))