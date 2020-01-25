# 회문

T = int(input())

for test_case in range(T):
    text = input()

    middle = len(text)//2
    flag = 1

    for t in range(middle+1):
        if text[t] == text[-1-t]:
            continue
            
        else:
            flag = 0
            break
        
    print(f'#{ test_case +1 } {flag}')