# 파이썬 개꿀

for test_case in range(10):
    t = int(input()) # 순서
    find_word = input()
    text = input()

    result = text.count(find_word)
    print(f'#{ t } { result }')
    