# 요리사
# 1) 조합 만들기 - size에 따라 자동생성
def combinations(size, foods=[]):
    cnt_food = len(foods)
    loop_start = foods[-1]+1 if foods else 0
    loop_end = size//2 + cnt_food +1  
    res = []
    if cnt_food == size //2:
        res += [foods]
        return res
    for i in range(loop_start, loop_end):
        res += combinations(size, foods+[i])
    return res

for tc in range(1, 1+int(input())):
    size = int(input())
    synergy = [list(map(int, input().split())) for _ in range(size)]
    tmp = combinations(size)
    scores = []
    # 2) 각 조합별로 score구하기 - 결과를 확인은 주석문 실행!
    for i in range(len(tmp)):
        score = 0
        # print(tmp[i])
        # print('--------')
        for j in range((len(tmp[i])-1)):
            for k in range(j+1, len(tmp[i])):
                if j != k:
                    # print(tmp[i][j], tmp[i][k])
                    score += synergy[tmp[i][j]][tmp[i][k]]
                    score += synergy[tmp[i][k]][tmp[i][j]]
        scores.append(score)
    
    # 3) 최소 차이 구하기.
    for i in range(len(tmp)//2):
        if i == 0:
            min_score = abs(scores[i] - scores[-i-1])
        else:
            if abs(scores[i] - scores[-i-1]) < min_score:
                min_score = abs(scores[i] - scores[-i-1])
    print(f'#{tc} {min_score}')