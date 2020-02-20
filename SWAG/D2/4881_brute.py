# 배열 최소합 문제

# 완 전 탐 색
'''
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
'''

def arr_min(idx_list, current_sum):
    global min_sum
    global data
    
    i = len(idx_list)
    if current_sum > min_sum:
        return
        
    if i == len(data):
        if min_sum > current_sum:
            min_sum = current_sum
            return current_sum
        return

    for idx, j in enumerate(data[i]):
        if idx in idx_list:
            continue
        else:
            current_sum += j
            copy_list = idx_list[:]
            copy_list.append(idx)
            arr_min(copy_list, current_sum)
            current_sum -= j

T = int(input())
for tc in range(1, T+1):
    size = int(input())
    data = [list(map(int, input().split())) for _ in range(size)]
    min_sum = 9999999

    arr_min([], 0)
    print(f'#{tc} {min_sum}')