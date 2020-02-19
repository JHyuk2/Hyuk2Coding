
# 함수1) 쪼개진 문장들을 한 단어씩 돌아가며 이름인지 살펴보기.
def isName(word):
    for idx, w in enumerate(word):
        if idx == 0:
            if w.isupper():
                continue
            else:
                return False
        else:
            if w.islower():
                continue
            else:
                return False
    return True

 
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    text = input()

    periods = ['.','?','!']
    tmp = []
    start = 0

    # 1) 구두점으로 나눠서 받기 (문장별로)
    for idx, t in enumerate(text):
        if t in periods:
            tmp.append(text[start:idx].strip())
            start = idx+1

    # 2) 문장 스플릿
    text_list = []
    for t in tmp:
        text_list.append(t.split())

    # 3) 각 문장을 순회하며 name 카운트하기.
    result = []
    for line in text_list:
        cnt = 0
        for word in line:
            if isName(word):
                cnt +=1
        result.append(str(cnt))
    
    print('#{} {}'.format(tc, " ".join(result)))