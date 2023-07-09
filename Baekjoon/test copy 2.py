N = int(input())
find_n = int(input())

#     북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작지점 등등 초기화
x, y = N//2, N//2
cnt = 1
map_list = [[0 for _ in range(N)] for _ in range(N)]
map_list[x][y] = cnt
head = 0
length = 0
flag = 1


if find_n == 1:
    temp = (x+1, y+1)
    
while flag:
    if head in [0, 2]:
        length +=1

    for _ in range(length):
        if cnt < N*N:
            cnt +=1
            x = x + dx[head]
            y = y + dy[head]
            map_list[x][y] = cnt
            
            if cnt == find_n:
                temp = (x+1, y+1)
        else:
            flag = 0

    head = (head+1)%4

for i in range(N):
    print(" ".join(map(str, map_list[i])))
print(temp[0], temp[1])