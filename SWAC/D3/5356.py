'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

T = int(input())

for test_case in range(1, T+1):
    chars = []
    max_len = 0
    for i in range(5):
        tmp = list(input())
        if max_len < len(tmp):
            max_len = len(tmp)
        chars.append(tmp)
    
    # 길이를 맞춰줌
    for char in chars:
        if len(char) < max_len:
            for _ in range(max_len - len(char)):
                char.append('')
    
    # 가로세로 반전
    chars = list(zip(*chars)) 
    result = []
    for c in chars:
        tmp = ''.join(c)
        result.append(tmp)

    print(f'#{test_case} {"".join(result)}')