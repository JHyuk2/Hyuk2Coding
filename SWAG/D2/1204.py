# 최빈값 찾기.

T = int(input())

for test_case in range(1, T+1):
    i = int(input()) # 일단 문제에 있으니 그냥 받자
    scores = list(map(int, input().split())) # 1000명의 점수를 입력받음.
    
    scores_dict = {
        str(i):0 for i in set(scores)
    }
    
    ## set은 기본적으로 오름차순 정렬된다.
    most_common = 0

    for sc in set(scores):
        scores_dict[str(sc)] += scores.count(sc)
        if scores.count(sc) > most_common: 
            most_common = scores.count(sc)

    ## 여기까지 했다면 각 딕셔너리 값과 최빈값의 빈도수가 같이 구해짐
    result = 0

    for key, val in scores_dict.items():
        if val == most_common:
            if int(key) > result:
                result = int(key)

    print(f'#{ test_case } { result }')
