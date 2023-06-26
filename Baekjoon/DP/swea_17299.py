# 단순히 문자열을 쪼개는 문제.
# 어떻게 보면 간단한 것 같다.

def split_number(concat_num):
    half = len(concat_num) // 2
    ans = int(concat_num[:half]) + int(concat_num[half:])
    if len(concat_num) %2: #길이가 홀수인 경우 두 가지를 비교해야됨
        temp = int(concat_num[:half+1]) + int(concat_num[half+1:])
        if ans > temp: ans = temp
    
    return ans

for tc in range(int(input())):
    print(f"#{tc+1} {split_number(input())}")