# 당근수확 4

# 1) 한 쪽의 범위를 구하는 함수
# 2) 돌리고 1 반복

def harvest(farm):
    length = len(farm[0])
    middle = length // 2 # 루프 회수
    crops = 0
    
    for i in range(middle):
        start_point = i+1
        end_point = length - start_point
        for j in range(start_point, end_point):
            crops += farm[i][j]
    return crops

def rotate(farm):
    farm = list(zip(*farm[::-1]))
    return farm

T = int(input())

for tc in range(1, T+1):
    size= int(input())
    farm = [list(map(int, input().split())) for _ in range(size)]
    
    result = []
    for i in range(4): # 동서남북.
        tmp = harvest(farm)
        result.append(tmp)
        farm = rotate(farm)
    
    print('#{} {}'.format(tc, max(result) - min(result)))