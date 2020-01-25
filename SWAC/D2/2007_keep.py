## 이 풀이법은 최대 마디를 구하는 방법인데, test_case에 부합하지 않는다.

# T = int(input())

# for test_case in range(T):
#     text = input()

#     for i in range(10): ## 마디의 최대길이가 10이기 때문에 10까지만 루프.
#         if text[i+1:].count(text[0:i+1]) >=2:
#             continue
#         else:
#             tmp = text[0:i]
#             break
#     else:
#         tmp = text[0:i+1]

#     print(f'#{i+1} {tmp}')

# # -------------------------------------------------------------------------

## test_case에서는 최소 마디를 구하고 싶은 모양인가보다.
# 즉 마디를 구하는 함수를 이용해서 다시 마디를 구하고, 또 마디를 구해서 count = 1인 return하는 재귀함수를 사용하면 어떨까
# 푸는 방법은 맞았지만, 메모리 에러가 발생한다.

# T = int(input())

# def find_repeat(text, cnt):
#     max_range = 10 if len(text) > 10 else len(text) # 마디의 최대길이 지정.

#     for i in range(max_range):
#         if text[i+1:].count(text[0:i+1]) >=cnt:
#             continue
#         else:
#             tmp = text[0:i]
#             break
#     else: # 마디 길이가 max일 때도 카운트가 2인 경우 => 즉 마디길이는 10인 경우
#         tmp = text[0:i+1] # 10에서 잘라줌.

#     if len(tmp) == 1: ## 반복되는 마디가 없는 경우
#         return text # 텍스트 전체를 반환.
#     else:
#         return tmp # 반복되는 마디가 있는 경우 마디 반환

# for test_case in range(T):
#     text = input()
#     repeat = find_repeat(text, 2) # 전체 마디 기준으론 count 2 이상인 것들 중,
# #    print(repeat)
#     while repeat != find_repeat(repeat,1): # 그 마디를 기준으로 또다시 count가 세어지는 것들.
#         repeat = find_repeat(repeat,1)

#     print(f'#{test_case + 1} {repeat}')

# ### 더 효율적인 코드가 필요하다.

# # -------------------------------------------------------------------------
## 마디(r)을 기준으로, text안에 6번 이상 나온다면 적어도 최대마디 10 안에서도 반복되는 마디가 있다는 뜻.
## 즉 count >=6 인 경우엔 range 10 안에서 반복되는 것이 있는지를 찾고,
## 6 > count >=3 인 경우에서만 일반적인 마디찾기를 진행하면 된다.

# T = int(input())
# ABCABCABCABCABCABCABCABCABC
# for test_case in range(T):
#     text = input()
#     tmp = ''
#     for i in range(10): ## 마디의 최대길이가 10이기 때문에 10까지만 루프.
#         if text[:].count(text[0:i+2]) >=6:
#             sliced_text = text[:10]
#             for j in range(len(sliced_text)): # 자른 문자열의 최대길이만큼만 루프
#                 if sliced_text[j+1:].count(sliced_text[0:j+1]) >=1:
#                     print(sliced_text[j+1:], sliced_text[0:j+1])
#                     continue
#                 else:
#                     tmp = sliced_text[0:j]
#                     break
#             break

#         elif text[i+1:].count(text[0:i+1]) >= 2:
#             continue
#         else:
#             tmp = text[0:i]
#             break
#     else:
#         tmp = text[0:i+1]

#     print(f'#{test_case+1} {tmp}')

## 결론만 말하자면...뭔가 잘 안나옴. 가장 문제는 'ABCABCABC'의 경우, 'ABC' 가 한 마디인데, ABCA까지 뽑아버리는게 문제.


# # -------------------------------------------------------------------------

## 처음으로 돌아가서..

# def loopfinder(text):
#     if len(text) < 10:
#         max_loop = len(text)
#     else:
#         max_loop = 10

#     for i in range(max_loop):
#         if i == 0:
#             continue
#         elif text[i+1:].count(text[:i+1]) > 1: #
#             continue
#         else: ## loop를 벗어났을 때
#             if i == 1: # 즉 하나의 마디도 없는 경우
#                 tmp = text # 텍스트 그 자체가 마디임.
#                 break
#             else: # i >1 인 경우 (즉 마디가 있는 경우)
#                 tmp = text[:i]
#                 break
#     return tmp

# T = int(input())

# for i in range(T):
#     test_case = input()
#     temp = loopfinder(test_case)
#     while test_case != temp:
#         temp = loopfinder(temp)

#     print(temp)

## 이렇게 풀면 런타임에러...

# -------------------------------------------------------------------------################

def loopfinder(text):
    if len(text) < 10:
        max_loop = len(text)
    else:
        max_loop = 10

    for i in range(max_loop):
        if i == 0:
            continue
        elif text[i+1:].count(text[:i+1]) > 1: #
            continue
        else: ## loop를 벗어났을 때
            if i == 1: # 즉 하나의 마디도 없는 경우
                tmp = text # 텍스트 그 자체가 마디임.
                break
            else: # i >1 인 경우 (즉 마디가 있는 경우)
                tmp = text[:i]
                break
    return tmp


T = int(input())

for i in range(T):
    test_case = input()
    temp = loopfinder(test_case)
    while test_case != temp:
        temp = loopfinder(temp)

    print(temp)
