# GNS-771

T = int(input())
 
for test_case in range(1, T+1):
    i = input() # 일단 인풋

    # 딕셔너리 만들기
    a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    b = [i for i in range(10)]
    tmp_dict = {i[0]:i[1] for i in list(zip(a, b))}

    # 각각을 숫자로 받아서 리스트에 넣어줌
    
    inputs = input()
    tmp_list = [tmp_dict[i] for i in inputs.split()]
    tmp_list.sort() # 순서대로 정렬

    result = ' '.join([key for key, val in tmp_dict.items() for t in tmp_list if t == val]) # 다시 문자로 바꿈
    print(f'#{test_case} {result}')