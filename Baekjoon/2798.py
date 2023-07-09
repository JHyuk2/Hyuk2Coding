# 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
flag = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        # 중간에서 가지치기
        if cards[i] + cards[j] > M:
            continue
        
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if temp > M:
                continue
            else:
                if res < temp:
                    res = temp
        if res == M:
            flag = 1
            break
    if flag:
        break

print(res)


