# 파리퇴치

# N * N 사이즈가 입력 ( 15 >= N >= 5)
# M * M 사이즈의 파리채 (M >= 2)
# 최대 파리 수 30

T = int(input()) # 테스트 케이스 개수

for test_case in range(T):
    N, M = input().split() # 먼저 튜플로 받아옴.
    N, M = int(N), int(M) # typecasting
    tmp = [[] for _ in range(N)] # N만큼의 배열을 만들어줌.

    # 배열에 값 넣어주기
    for n in range(N):
        tmp[n] = [i for i in list(map(int, input().split()))]

    length = N-M +1 # 파리채의 길이가 M일 때 가능한 루프의 길이는 N-M만큼이 될 것임.
    max_val = 0
    # print('-'*10)

    for i in range(length):      # N=5, M=2인 경우, 0~4 순회               
        for j in range(length):  # 0 ~ 4 순회, 즉 우리는 차원을 줄일 예정
            result = 0           # 순회하기 전 result 초기화
            for k in range(M):   # 그리고 (i, j) == (0, 0)기준, 필요한 합계는 4개. (0, 0), (0, 1), (1, 0), (1, 1) 
                result += sum(tmp[i+k][j:j+M])
            if result > max_val:
                max_val = result
        #     print(result, end = ' ')
        # print()
    print(f'#{ test_case+1 } {max_val}')

# print문을 모두 주석처리