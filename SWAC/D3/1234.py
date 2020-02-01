## 공통 제거

def remove_same(text):
    for idx, t in enumerate(text):
        if idx == len(text) - 1:
            break
        
        elif text[idx] == text[idx+1]:
            text = text[:idx] + text[idx+2:]
            break
    
    return text

for test_case in range(1, 11):
    N, num = input().split()

    # 중복제거
    while num != remove_same(num):
        num = remove_same(num)

    print(f'#{ test_case } { num }')