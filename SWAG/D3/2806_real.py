# Queen 문제
import copy

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


# 모든 줄에 Q가 있을 때
def isAll_Q(arr):
    N = len(arr)
    result = []

    for i in arr:
        tmp = True if 'Q' in i else False
        result.append(tmp)
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
    return tmp_copy

# 배열이 주어졌을 때, 몇 개의 겹치지 않는 Q가 가능한지 찾는다.
def queen(arr, depth):
    
    # 1) 값이 전부 대입될 수 있는 상태인지 확인.
    # 만약 한 줄이라도 모두 False인 경우 0을 리턴.
    if not check_True(arr):
        return 0

    # 모든 라인에 Q가 있을 때.
    elif isAll_Q(arr):
        return 1

    else:
        # 여기서도 shallow copy를 하게 되면, 다음 이미 변형된 new_arr을 만나게 된다.
        N = len(arr)
        result = 0
        for j in range(N):
            if arr[depth][j] == True:
                arr_copy = copy.deepcopy(arr)
                new_arr = turn(arr_copy, [depth, j])
                tmp = queen(new_arr, depth+1)
                result += tmp
        return result
    
    
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    # tmp_list = [[True]*4]*4 ## 왜인지 이렇게하면 안됨.
    tmp_list = list([True for _ in range(N)] for _ in range(N))
    result = 0
    depth = 0
    
    # tuple을 사용하면 값을 바꿀 수 없다.
    # 때문에 mutable값을 허용하면서 새로운 객체를 생성하는 deepcopy를 사용한다.
    for i in range(len(tmp_list)):
        new_tmp = copy.deepcopy(tmp_list)
        new_tmp = turn(new_tmp, [0,i])
        result += queen(new_tmp, depth+1)
  
    print('#{} {}'.format(test_case, result))