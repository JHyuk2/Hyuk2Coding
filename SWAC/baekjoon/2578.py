'''
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
'''

# 숫자가 들어오면 해당 숫자를 0으로 체크
def numcheck(arr, num):
    for line in arr:
        if num in line:
            line[line.index(num)] = 0

# 현재 상태의 빙고줄 확인
def find_bingo(arr):
    length = len(arr)
    cnt = 0
    dia_down = 0
    dia_up = 0

    for i in range(length):
        tmp = 0
        # 가로빙고
        if sum(arr[i]) == 0:
            cnt += 1

        # 세로빙고
        for j in range(length):    
            tmp += arr[j][i]
            # 대각비교를 위함 
            if i == j:
                dia_down += arr[i][j]
            if i + j == length-1:
                dia_up += arr[i][j]

        if tmp == 0:
            cnt += 1    
    # 대각빙고
    if dia_up == 0:
        cnt += 1
    if dia_down == 0:
        cnt += 1
        
    return cnt


# 빙고
call = []
bingo_board = [list(map(int, input().split())) for _ in range(5)]
for _ in range(5):
    call += list(map(int, input().split()))
bingo = 0
times = 0

for c in call:
    times += 1
    numcheck(bingo_board, c)
    bingo = find_bingo(bingo_board)
        
    if bingo >=3:
        break

print(times)