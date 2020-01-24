T = int(input())

for i in range(T):
    test_case = list(map(int, input().split()))
    print(f'#{i+1} {round(sum(test_case)/len(test_case))}')
    # int로 타입캐스팅을 하면 두 번째 테스트케이스에서 에러 발생