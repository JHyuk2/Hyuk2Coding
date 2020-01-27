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


t1 = 'abba'
t2 = 'aba'
t3 = 'baba'
t4 = 'cbacb'
t5 = 'bcb'

tmp = list(map(check_palindrome, [t1, t2, t3, t4, t5]))
print(tmp)