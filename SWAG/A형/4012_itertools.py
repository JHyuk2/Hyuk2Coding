from itertools import combinations

for tc in range(1, 1+int(input())):
    size = int(input())
    synergy = [list(map(int, input().split())) for _ in range(size)]
    tmp = list(combinations(range(size), size//2))
    scores = []
    for i in range(len(tmp)):
        score = 0
        for j in range((len(tmp[i])-1)):
            for k in range(j+1, len(tmp[i])):
                if j != k:
                    score += synergy[tmp[i][j]][tmp[i][k]]
                    score += synergy[tmp[i][k]][tmp[i][j]]
        scores.append(score)
    
    for i in range(len(tmp)//2):
        if i == 0:
            min_score = abs(scores[i] - scores[-i-1])
        else:
            if abs(scores[i] - scores[-i-1]) < min_score:
                min_score = abs(scores[i] - scores[-i-1])
    print(f'#{tc} {min_score}')