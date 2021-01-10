# 간단하게, palindrome check 함수를 만들고, 조합으로 index 뽑아내는 방법 있음
from itertools import combinations

def is_palindrome(string):
    middle = len(string) // 2

    for i in range(middle):
        top = i
        bot = -i-1
        if string[top] == string[bot]:
            pass
        else:
            return 0
    else:
        return 1

# 조합으로 로 두 개 선택하는 방법. ## 근데 지금은 필요없음.
def find_longest(input_str):    
    combi_list = list(combinations([i for i in range(len(input_str))], 2))
    max_length = 1
    result_list = list()

    for tmp_list in combi_list:
        start = tmp_list[0]
        end = tmp_list[1] + 1 # exclusive range이기 때문에 +1
        if is_palindrome(input_str[start:end]):
            if len(input_str[start:end]) > max_length:
                max_length = end - start
                result_list = [start, end-1]
    return max_length, result_list


'''
예제코드
ex) 3,2,8,1,4,1,6,8,3,4,5,6,4,3

# 1~5
7,2,7,2,2,7,7,2,2,5
8,12,3,9,8,3,4,9,11,1,12,9,11,1,8
19,10,14,11,10,10,9,2,7,7,2,6,9,9,14,19,2,9,11,6
6,17,25,2,13,17,20,24,6,20,14,25,2,24,14,2,14,24,25,18,25,2,25,17,20
8,30,8,33,8,31,16,1,40,16,21,24,30,32,21,1,33,21,16,11,31,8,16,1,40,31,21,33,11,31
'''

# 실행 코드
input_str = input()
input_list = input_str.split(',')
length = len(input_list)
# 비트 & 시프트연산자 활용
res = []
for i in range(1 << length):
    bit = i
    tmp = [0 for _ in range(length)]
    if bit !=0:
        for j in range(length):
            if (1 & bit >> j) == 0:
                continue
            tmp[j] = 1
    res.append(tmp)

max_length = 1
max_list = list()
max_str = ''

for tmp_list in res:
    tmp_str = []
    for idx, flag in enumerate(tmp_list):
        if flag:
            tmp_str.append(input_list[idx]) 
            
    if is_palindrome(tmp_str):
        if len(tmp_str) > max_length:
            max_length = len(tmp_str)
            max_list = tmp_list
            max_str = tmp_str

print(max_length, max_list, max_str)