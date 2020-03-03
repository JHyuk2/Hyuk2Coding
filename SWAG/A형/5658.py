# 보물상자 비밀번호
T = int(input())

for tc in range(1, T+1):
    length, rank = map(int, input().split())
    div_len = length // 4
    d = input()
    data = []

    for i in range(1, div_len+1):
        tmp = d[i:] + d[:i]
        for j in range(4):
            d_tmp = tmp[j * div_len : (j+1)*div_len]
            data.append(int(d_tmp, 16))
    res = sorted(list(set(data)), reverse = True)[rank-1]

    print(f'#{tc} {res}')