# Magnetic

'''
----------------N극(1)
1 0 0 0 0 0 0 
0 0 0 0 1 2 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 1 0 0 0
2 0 2 0 0 0 0
0 0 0 2 0 0 0 
----------------S극(2)
'''


'''
이렇게 했을 때의 문제점은, 위에서부터 순회하기 때문에 1이 계속 내려온다는점.
문제가 의도하는바와 맞지 않음.

# def magnetic(tmp_list):
    ## 양쪽이 같이 움직이면 좋겠지만, 한 작업엔 한개씩만 움직일 수 있음.
    # 1) N극에 가까운 N들 움직이기.
    # N = len(tmp_list)

    # for x in range(N):
    #     for y in range(N):
    #         if tmp_list[x][y] == 1 and x+1 == N: # 마지막일 때
    #             tmp_list[x][y] = 0

    #         elif tmp_list[x][y] == 1 and (tmp_list[x+1][y] == 0):
    #             tmp_list[x][y] = 0
    #             tmp_list[x+1][y] = 1

    #         elif (tmp_list[x][y] ==2) and (x ==0):
    #             tmp_list[x][y] = 0

    #         elif (tmp_list[x][y] == 2) and (tmp_list[x-1][y] == 0):
    #             tmp_list[x][y] = 0
    #             tmp_list[x-1][y] = 2

    # return tmp_list # 남아있는 개수.
'''

# for test_case in range(1): #한번만 보고싶음
#     tmp_list = []
#     for _ in range(7):
#         tmp = list(map(int, input().split()))
#         tmp_list.append(tmp)
    
#     after_mag = magnetic(tmp_list)
#     print('-------------------------')
#     for i in range(7):
#         for j in range(7):
#             print(after_mag[i][j], end =' ')
#         print()

# -------------------------------------------------------------------------------------


## 즉, 인덱스가 0~6까지 있으면 0 -> 6 -> 1 -> 5 -> 2 -> 4 의 순서로 순회해야 한다.
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

## 이렇게 한 다음 zip으로 가로세로 반전시켜주면 내가 원하던 순서의 이터레이션이 나온다.
## 그렇다면 애초에 주어진 리스트를 반전한 후 위의 식을 적용하면 되지 않을까?