test = int(input())
def mat_sum(n, idx_x, idx_y, result, total):
    if result[0] < total:
        print(idx_x, idx_y, total)
        return
    # 끝까지 갔을 때
    if idx_x == n:
        print(idx_x, idx_y, total)
        # result값에 들어온 게 없다면 비교
        if len(result) == 0:
            result.append(total) 

        # result와 total값을 비교
        elif total < result[0]:
            result[0] = total
        total = 0

    # 진행중인 경우
    else:
        tmp_y = [i for i in range(n) if i not in idx_y]
        for j in tmp_y:
            idx_y.append(j)
            total += mat[idx_x][j]
            mat_sum(n, idx_x+1, idx_y, result, total)
            idx_y.pop()
            total -= mat[idx_x][j]

for tc in range(1,test+1):
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    result = [999999]
    idx_x = 0
    idx_y = []
    total = 0
    mat_sum(n, idx_x, idx_y, result, total)
    print(f'#{tc} {result[0]}')