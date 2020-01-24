#tmp = 'KOREAKOREAKOREAKOREAKOREAKOREA'

T = int(input())

for test_case in range(T):
    text = input()

    for i in range(10):
        if text[i+1:].count(text[0:i+1]) >=2:
            continue
        else:
            tmp = text[0:i]
            break
    else:
        tmp = text[0:i+1]

print(tmp)