## 이러면 시간초과뜸... 눈물이 나네 ㅠㅠ
# 자리배치

w,h = map(int, input().split())
n = int(input())

dx =[-1,0, 1, 0]
dy =[0, 1, 0, -1]
direction = 0
stage = [[0 for _ in range(w)] for _ in range(h)]

# start_point
x = h -1
y = 0

# 1부터 시작해서 채워나감.
for i in range(1, n+1):
    if i == 1:
        stage[x][y] = i
    else:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if 0 <= nx < h and 0<= ny < w and stage[nx][ny] == 0:
            x += dx[direction]
            y += dy[direction]
        # 벽을 만났거나 다른 숫자를 만나는 경우
        else: 
            direction += 1 # 먼저 1을 더하고
            direction %= 4 # 다시 북쪽으로 방향 초기화
            x += dx[direction]
            y += dy[direction]
            
        stage[x][y] = i
    
pos = [y+1, h-x]
print(pos[0], pos[1])
    # print('------------')
    # for j in range(h):
    #     print(stage[j])

