T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split())
    price = A if A <B else B
    result = C // price
    print(f'#{test_case} {result}')