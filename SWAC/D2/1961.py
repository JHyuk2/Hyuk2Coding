def rotate(tmp_list):
    new_tmp = list(zip(*reversed(tmp_list)))
    return new_tmp

def int_to_str(tmp_list):
    result = []
    for tmp in tmp_list:
        tmp = list(map(str, tmp))
        result.append(tmp)
    return result
"""
1 2 3
4 5 6
7 8 9

 90 180 270
------------
741 987 369
852 654 258
963 321 147 


6 9 4 7 0 5
8 9 9 2 6 5
6 8 5 4 9 8
2 2 7 7 8 4
7 5 1 9 7 9
8 9 3 9 7 6
"""


T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    tmp_list = []
    
    # 2차원 배열 생성
    for n in range(N):
        tmp = list(map(int, input().split()))
        tmp_list.append(tmp)

    rotate_1 = int_to_str(rotate(tmp_list)) # 90도 회전
    rotate_2 = int_to_str(rotate(rotate_1)) # 180
    rotate_3 = int_to_str(rotate(rotate_2)) # 270 

    print(f'#{ test_case }')
    for i in range(N):
        print(''.join(rotate_1[i]), ''.join(rotate_2[i]) , ''.join(rotate_3[i]))