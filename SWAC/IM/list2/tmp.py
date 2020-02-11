from itertools import zip_longest


T=int(input())
for tc in range(1, T+1):
    res = ''
    words = [list(input()) for _ in range(5)]
    # print(words)
    a = list(zip_longest(*words, fillvalue=' ' ))
    print(a)
    for tmp_tuple in a:
        for char in tmp_tuple:
            if char != ' ':
                res += char
    print(res)

