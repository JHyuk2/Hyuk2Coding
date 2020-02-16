# test_case = input()
test_case = '3 17 1 39 8 41 2 32 99 2'
test_case = test_case.split(' ')
result = 0

for t in test_case:
    if (int(t)%2): #홀수
        result += int(t)
    else:
        pass

print(result)