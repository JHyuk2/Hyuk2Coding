# 삼각형을 만들기 위해선 세 개의 직선이 필요함

# 1) 간선 3개가 조합되는 모든 경우의수를 찾고,
# 2) 포인트의 (start, end) 노드의 중복을 제거했을 때 원소가 3개이면 삼각형
#     ex) (1,3) / (2,3) / (1,2) ==> (1, 2, 3) 

# 여기서 같은 간선을 의미하는 (1,3) / (3,1) 은 중복해서 입력받지 않기 때문에 별도의 처리과정은 X
def isTriangle(line_combination):
    tmp = []
    for i in line_combination:
        tmp += i
    if len(set(tmp)) == 3:
        return True
    else:
        return False

import copy
# 모든 경우의수를 다 뽑는 함수
def tri_combination(arr, N):
    # 루프시 마지막값.
    loop_length = len(arr) - N + 1
    # Base_case
    if N == 0:
        return []

    
    result = []
    for idx, num in enumerate(arr[:loop_length]): 
        res=[]
        arr_copy = copy.deepcopy(arr)
        tmp = arr_copy.pop(idx) 
        new_arr = arr_copy[idx:]
        res += tri_combination(new_arr, N-1)
        result += [tmp]+res
        
    return result

arr = [1,2,3,4]
N = 2

print(tri_combination(arr, N))
# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split()) # 노드 / 간선 수
#     lines = [[i for i in map(int, input().split())] for _ in range(M)]

# lines = [[1,2], [2,3], [3,1]]
# print(isTriangle(lines))
