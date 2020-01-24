# 중간값 구하기.

N = int(input())
test_case = list(map(int, input().split())) # N객만큼의 입력값을 받음
middle = N // 2 ## 홀수기 때문에 middle값은 항상 한 개만 존재.
print(sorted(test_case)[middle])