# 가위바위보 승리 판별하기

# 가위:1
# 바위:2
# 보 :3

# a vicdtory  => 1 : 3 / 2 :1 / 3 : 2
# a lose => 3:1 / 1:2 / 2:3
test_case = list(map(int, input().split()))

a = test_case[0]
b = test_case[1]

if a == (b%3)+1: ## 승리할 때를 보면 3으로 나눈 후 +1일 때라는 공통점이 있음.
    print('A')

elif a == b:
    pass

else:
    print('B')