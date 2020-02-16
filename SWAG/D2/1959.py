T = int(input())

for test_case in range(1, T+1):
    xxx = input() ## 실수로 밑에서 fir, sec 정해버림
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    first = B if len(B) >= len(A) else A # 더 긴 리스트
    second = A if first == B else B # 짧은 리스트
    length = len(first) - len(second)
    result = []

    for i in range(length+1):
        tmp = 0
        for j in range(len(second)):
            tmp += first[j+i] * second[j]
        result.append(tmp)

    print(f'#{ test_case } { max(result) }')