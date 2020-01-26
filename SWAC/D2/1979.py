# N by N 행렬
# 길이가 K인 단어가 들어갈 수 있는 자리 모두 찾기.

'''
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''

def puzzle_counter(puzzle, find_num):
    N = len(puzzle)

    # 1) 각 길이만큼 담을 수 있는 딕셔너리 생성
    count_dict = {
        str(i):0 for i in range(1, N+1) # 1, 2, ..., N
    } 
    
    # 퍼즐은 i * j의 2차원 배열
    for i in range(N):
        for j in range(N):
            length = 0
            if j == 0 and puzzle[i][j] == 1: # 벽에 붙어서 출발하는 경우,
                for k in puzzle[i]:
                    if k == 1:
                        length +=1
                        continue
                    else: # k ==0
                        count_dict[str(length)] += 1
                        break
                else: # 벽에 닿았을 때.
                    count_dict[str(length)] += 1

            else: # j >= 1인 경우
                if puzzle[i][j] == 1 and puzzle[i][j-1] == 0: # 왼쪽이 막힌 상태일 때
                    for k in range(N-j):
                        if puzzle[i][j+k] == 1:
                            length += 1
                            continue
                        else:
                            count_dict[str(length)] += 1
                            break
                    else:
                        count_dict[str(length)] += 1

    return count_dict[str(find_num)]

T = int(input())

for test_case in range(1, T+1):
    N, k = tuple(map(int, input().split()))
    puzzle = [[] for _ in range(N)]

    # 1) 배열 생성 및 값 입력
    for n in range(N):
        puzzle[n] = list(map(int, input().split()))

    # 2) 카운팅을 위한 가로세로 반전 퍼즐 생성
    reversed_puzzle = list(zip(*puzzle)) 

    real = puzzle_counter(puzzle, k)
    rv = puzzle_counter(reversed_puzzle, k)
    
    print(f'#{ test_case } {real + rv}')