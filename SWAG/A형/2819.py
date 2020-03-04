# 격자판 이어 붙이기.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def lattice(tmp_data, depth = 1):
    if depth == 7:
        res = []
        for i in range(4):
            for j in range(4):
                res += tmp_data[i][j]
        return len(set(res))

    new_tmp = [[[]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            tmp_d = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < 4 and 0 <= ny < 4:
                    for d in tmp_data[nx][ny]:
                        tmp_d.append(data[i][j][0]+d)
            new_tmp[i][j] = list(set(tmp_d))
    return lattice(new_tmp, depth +1)

T = int(input())
for tc in range(1, T+1):
    data = [list(map(list, input().split())) for _ in range(4)]
    print(f'#{tc} {lattice(data)}')
