from copy import deepcopy

arr = [1 for _ in range(5)]
arr_copy = deepcopy(arr)

# 어떻게 해도 원본이 바뀐다.

def list_trans(tmp_list):
    tmp_list[1] = 0
    return tmp_list

arr2 = list_trans(arr_copy)
print(arr)
print(arr2)
print(arr_copy)