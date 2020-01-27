# 회문 찾기
def check_palindrome(text):
    middle = len(text) // 2
    
    for i in range(middle):
        if text[i] == text[-i-1]:
            continue
        else:
            flag = 0
            break
    else:
        flag = 1
    return flag           

def find_palindrome(tmp_list, k):
    cnt = 0

    for i in range(len(tmp_list)):
        # 만약 찾는 회문 길이가 4이면 5번만 루프 가능. (8-4 +1)
        for j in range(len(tmp_list) - k + 1):
            tmp = tmp_list[i][j:j+k]

            if check_palindrome(tmp): # check == 1일경우 회문
                cnt += 1

    return cnt

for test_case in range(10):
    k = int(input()) # 회문의 길이
    temp_list = [] # 입력받을 배열

    for _ in range(8):
        temp = input()
        temp_list.append(temp)

    rotate_temp = list(zip(*temp_list)) # 세로방향 찾기

    result = find_palindrome(temp_list, k) + find_palindrome(rotate_temp, k)
    print(f'#{ test_case +1 } { result }')
    