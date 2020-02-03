# Queen 문제

# 한 줄에 Q or T가 하나씩은 존재하는지 확인
def check_True(arr):
    N = len(arr)
    result = []
    for i in arr:
        result.append(any(i))
    if all(result) :
        return True
    else:
        return False

# Q의 좌표를 받았을 때 가로,세로,대각을 False로 만드는 함수
def turn(tmp, pos):
    tmp_copy = list(tmp)
    x = pos[0]
    y = pos[1]

    for i in range(len(tmp_copy)):
        if i == x:
            tmp_copy[i] = [False]*len(tmp_copy)
        else:
            for j in range(len(tmp_copy)):
                if j == y or (j-i == y-x) or (i+j == x+y):
                    tmp_copy[i][j] = False
        tmp_copy[x][y] = 'Q'
    return tmp_copy, tmp


# 배열이 주어졌을 때, 몇 개의 겹치지 않는 Q가 가능한지 찾는다.
def queen(arr):
    
    # 1) 값이 전부 대입될 수 있는 상태인지 확인.
    # 만약 한 줄이라도 모두 False인 경우 0을 리턴.
    if not check_True:
        return 0 
    N = len(arr)

    # 2) 
    result = 0
    for x in range(N):
        arr_copy = arr[:]
        arr_copy = turn(arr_copy[])
        # 2-1) 만약 첫째 줄에 Q가 있는 경우, 건너뜀
        if 'Q' in arr[x]:
            continue
        # 2-2) 모두 False인 경우는 없다. (check_True), 다음 줄에서 Q를 찾아서 위치와 함께 던져줌.
        else:
            for y in range(N):
                if arr[x][y] == True:
                    arr_copy = arr[:] # 복사
                    new_arr = queen(turn(arr_copy, [x,y]))
                else: #False인 경우
                    continue

    # 다 통과했을 때
    return 1
for test_case in range(1):
    # tmp_list = [[True]*4]*4 ## 왜인지 이렇게하면 안됨.
    tmp_list = list([True for _ in range(4)] for _ in range(4))
    result = 0
    result = queen(tmp_list)
    print(result)

