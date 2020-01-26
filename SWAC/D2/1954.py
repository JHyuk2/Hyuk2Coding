## 먼저 달팽이 모양을 만들자.

N = 4

tmp_list = [[0 for _ in range(N)] for _ in range(N)] # N by N 행렬 생성
# num_list = [i for i in range(1, N*N + 1)]
# print(sorted(num_list, reverse =True).pop()) # 1부터 하나씩 출력

for i in range(N):
    for j in range(N):
        print((i, j), end = ' ')
    print()


cnt, x, y = 1, 0, 0
length = N # => 3
while cnt <=8 : # 더 이상 넣을 숫자가 없을 때까지 반복
    # => 오른쪽방향 이동
    if x == 0 and y == 0: #시작위치
        for k in range(length): # 0, 1 ,2
            tmp_list[x][y+k] = cnt
            cnt += 1 

            if k == length -1:
                y = y+k
                x += 1
                length -= 1
        print(cnt)

    # ↓ 아랫쪽 방향 이동
    elif y == length and x != length: # length = 2
        for k in range(length): # 1, 2, length = 2
            tmp_list[x+k][y] = cnt
            cnt += 1
            if k+1 == length:
                x = x+k
            print(cnt)

    # <- 왼쪽방향
    elif y == length and x == length: 
        for k in range(length): # 0, 1, length = 2
            tmp_list[x][y-(k+1)] = cnt # x =2, y = 2
            cnt += 1
            if k+1 == length:
                y = y-k-1
                length -= 1
            print(cnt, x,y)
    else:
        cnt += 1
    # 위쪽 방향



    

                
print()
for i in range(N):
    for j in range(N):
        print(tmp_list[i][j], end = ' ')
    print()