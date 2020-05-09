# n개의 컨테이너를 M대의 트럭

for tc in range(int(input())):
    N, M = input().split()
    weights = list(map(int, input().split())) # --- N
    caps = list(map(int, input().split())) # -- M
    weights.sort(reverse=True)
    caps.sort()
    selected = []
    for m in caps:
        cur = 0
        for idx, w in enumerate(weights):
            if w > m:
                continue
            if idx not in selected:
                selected.append(idx)
                break
            else:
                continue
    res = 0
    for s in selected:
        res += weights[s]
    print(f'#{tc+1} {res}')