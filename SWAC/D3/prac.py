## 즉, 인덱스가 0~6까지 있으면 0 -> 6 (0+6) -> 1(8, 15) -> 5 -> 2 -> 4 의 순서로 순회해야 한다.
N = 8
middle = N//2 # 3
cnt = 0

for x in range(N):
    for y in range(N):
        print((x,y), end =' ')
    print()

print('---------------------')


for x in range(N):
    ny = 0
    cnt = 0
    for y in range(N):
        print((x ,ny), end =' ')
        if ny < middle:
            cnt +=1
            ny = N-cnt
        else: #nx >= middle
            ny = cnt
    print()

## 이렇게 한 다음 zip으로 가로세로 반전시켜주면 원하는 순서로 이터레이트 시킬 수 있지.