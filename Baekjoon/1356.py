# 유진수

# 1) 숫자를 나누기
#    만약 10이하의 숫자면 NO!
# 2) 나눠진 숫자로 곱해주기

# 문자열로 나누기
N_str = list(input())
num_list = list(map(int, N_str))
length = len(num_list)
res = 'NO'

# 모든 원소를 곱해주는 함수
def mul(temp_list):
    res = 1
    for i in temp_list:
        res *= i
    return res

# 10 미만의 숫자가 들어오면 NO
if length == 1:
    res = 'NO'
else:
    for i in range(1, length):
        left = num_list[:i]
        right = num_list[i:]
        if mul(left) == mul(right):
            res = 'YES'
            break

print(res)