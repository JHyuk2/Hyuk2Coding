
mouem = 'aeiou'

T = int(input())

for test_case in range(1, T+1):
    char = list(input())

    text = ''
    for c in char:
        if c in mouem:
            text += ''  

        else:
            text += c

    print(f'#{ test_case } { text }')
    