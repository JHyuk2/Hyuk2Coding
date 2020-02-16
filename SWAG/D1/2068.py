"""
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

"""
T = int(input())

for i in range(T):
    test_case = list(map(int, input().split()))
    print(f'#{i+1} {max(test_case)}')