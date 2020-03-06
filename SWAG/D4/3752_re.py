T = int(input())
for tc in range(1, T+1):
    d = int(input())
    scores = list(map(int, input().split()))
    res = {0}
    for s in scores:
        tmp = []
        for r in res:
            tmp.append(s+r)
        res = res.union(set(tmp))
    print(f'#{tc} {len(set(res))}')