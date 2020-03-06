# 가능한 시험 점수
# 부분집합만들기 - 비트마스크 가능할듯

def subset(depth, current_sum = 0):
    res = []
    if depth == len(scores):
        return [current_sum]    
    res += subset(depth+1, current_sum)
    res += subset(depth+1, current_sum + scores[depth])
    return res

T = int(input())
for tc in range(1, T+1):
    d = int(input())
    scores = list(map(int, input().split()))
    tmp = subset(0)
    print(f'#{tc} {len(set(tmp))}')