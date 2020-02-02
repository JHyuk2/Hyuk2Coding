T = int(input())

for test_case in range(1, T+1):
    D, H, M = map(int, input().split())

    D -= 11
    H -= 11
    M -= 11

    if D >= 0:
        H += D*24
        if H>= 0:
            M += 60*H
            if M >= 0:
                result = M
            else:
                result -1
        else:
            result = -1
    else:
        result = -1

    print(f'#{test_case} {result}')