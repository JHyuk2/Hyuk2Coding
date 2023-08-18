# 숫자 야구
from itertools import combinations

for _ in range(int(input())):
    num, strike, ball = input().split()
    
    # strike > 정확히 맞춘 자리
    # ball > 자리는 틀렸지만 있는 숫자.
    strike = int(strike)
    ball = int(ball)
    

    # case 1) 전체탐색으로 111~999까지 쭉 탐색 ==> 너무 비효율적
    # case 2) 경우의 수로 나눠서.    
    num_split = list(num)

    # 먼저 스트라이크 갯수부터 비교
    # strike == 0이 아닌 경우에는?
    comb = list(combinations(num_split, strike))
    print(comb)
    