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

# 맨 윗줄에서만 실행함.
def queen(arr):
    print('---'*20)
    print('start_queen')
    if check_True(arr) == False:
        print('False in line', arr)
        return 0
    
    result = 0
    N = len(arr)

    for i in range(N):
        if 'Q' in arr[i]:
            print('jump', i)
            continue
        elif not any(arr[i]) : # All false인 경우
            print('All_False: ', arr[i])
            return 0
        else:
            for j in range(N):
                print(i, j, arr[i][j])
                if arr[i][j] == True:
                    print('~~~here~~~')
                    print(f'arr: {arr}')
                    arr_copy, arr = turn(arr, (i,j))
                    print(f'arr_copy: {arr_copy}')
                    result += queen(arr_copy)
                    print(arr)
                    # print(f'new_arr: {new_arr},  result: {result}')
            else:
                break
    else:
        print('result +1')
        return 1
    
    print(f'result: {result}')
    return result


            

for test_case in range(1):
    # tmp_list = [[True]*4]*4 ## 왜인지 이렇게하면 안됨.
    tmp_list = list([True for _ in range(4)] for _ in range(4))
    result = 0
    result = queen(tmp_list)
    print(result)

'''
머리가 안돌아간다.. 다음에 풀자
'''
