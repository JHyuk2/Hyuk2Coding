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

# 100 x 100 size

for test_case in range(10):
    n = int(input())
    temp_list = [] # 입력받을 배열
    
    # 배열생성됨
    for _ in range(100):
        temp = input()
        temp_list.append(temp)

    rotate_temp = list(zip(*temp_list)) # 세로방향 찾기

    # 찾는 길이를 줄여나가면서 서치하다가, 하나라도 걸리면 out?
    result = 0

    for k in range(100, 0, -1):
        cnt1 = find_palindrome(temp_list, k)  # 0이 아니라면
        cnt2 = find_palindrome(rotate_temp, k)
        result += (cnt1+cnt2)
        
        if result != 0:
            break

    print(f'#{ test_case +1 } { k }')