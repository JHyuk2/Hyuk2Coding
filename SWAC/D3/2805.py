'''
14054  =>    0
44250  =>   425
02032  =>  02032
51204  =>   120
52212  =>    2
 
5
'''
T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 사이즈
    crops = []

    # 배열에 집어넣음
    for i in range(N):
        tmp = list(map(int, input())) 
        crops.append(tmp)

    # 중심에서 멀어질수록 원소를 포함할 수 있는 게 적어짐.
    middle = N // 2 # N=5 인 경우, 2번째 인덱스가 중앙
    result = 0

    for x, one_line in enumerate(crops):
        start = abs(x-middle) 
        end = N - abs(x-middle)
        result += sum(one_line[start:end])

    print(f'#{ test_case } { result }')