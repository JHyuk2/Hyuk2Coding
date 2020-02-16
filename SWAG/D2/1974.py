# sudoku

T = int(input())

for test_case in range(1, T+1):
    sudoku = []

    for i in range(9):
        tmp = list(map(int, input().split()))
        sudoku.append(tmp)

    rotate_sudoku = list(zip(*sudoku))


    flag = 1
    # 블럭단위 체크
    for i in range(3):
        for j in range(3):
            check_sum = sum([sum([t for t in tt[j*3:(j+1)*3]]) for tt in sudoku[i*3:(i+1)*3]])
            if check_sum != 45:
                flag = 0
                break

    # 줄 단위 체크
    for i in range(9):
        check_1 = sum(sudoku[i])
        check_2 = sum(rotate_sudoku[i])
        if check_1 !=45 or check_2 !=45:
            flag = 0
            break
    
    print(f'#{ test_case } { flag }')