# 수도세 출력
# 사용량:W
# A: 리터당 P원
# B: 기본 Q, if 사용량 <R : Q, else: 초과분당 리터당 S

# P Q R S W 순서로 들어옴.

T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = tuple(map(int, input().split()))

    A = W * P
    B = Q if W < R else Q + S*(W-R)
    result = A if B > A else B

    print(f'#{ test_case } { result }')