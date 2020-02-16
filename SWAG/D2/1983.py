# 조교 채점!

# 총점 = 중간(35) 기말(45) 과제(20)
# 평점은 A+, A0, A- / B+, B0, B- / C+, C0, C- / D0 (10단계로 구분)
# 학생이 N명일 경우, 각 평점은 N/10명까지만 줄 수 있음.

# 1) 모든 학생 N명의 총점을 구한다.
# 2) 학생번호 K와 총점을 연결한 dictionary를 구현한다
# 3) 모든 총점이 정렬된 list를 하나 만든다.
# 4) 학생번호 k dictionary.value값에 list의 인덱스(rank)와 학점을 입력한다
# 5) 총 인원 N 명 기준으로
#    idx < N/10 : A+, N/10 <= idx < (2*N)/10 :A0.... 이런식으로 매칭시킬 수 있다.
 
T = int(input())

for test_case in range(T):
    N, k = tuple(map(int, input().split())) ## 각각을 int로 나눠서 입력받음.
    temp = []

    for student_num in range(1, N+1): # k 시작값을 1로 받기 때문에 range조정
        middle, final, task = list(map(int, input().split()))
        total = round((middle * 0.35) + (final*0.45) + (task*0.2), 3) ## 소수 셋째 자리에서 반올림.
        temp.append((total, student_num)) 
    
    ## 참고로 튜플은 정렬이 가능하다.
    
    temp = sorted(temp, reverse = True) ## 내림차순 정렬
    # 그 후, temp의 idx를 통해 비교하면 편하다.
    for idx, t in enumerate(temp):
        score, s_num = t
        if s_num == k:
            tmp = idx

    if tmp < (N/10):
        result = 'A+'
    elif tmp < (2*N)/10:
        result = 'A0'
    elif tmp < (3*N)/10 :
        result = 'A-'
    elif tmp < (4*N)/10 :
        result = 'B+'
    elif tmp < (5*N)/10 :
        result = 'B0'
    elif tmp < (6*N)/10 :
        result = 'B-'
    elif tmp < (7*N)/10 :
        result = 'C+'
    elif tmp < (8*N)/10 :
        result = 'C0'
    elif tmp < (9*N)/10 :
        result = 'C-'
    else:
        result = 'D0'

    print(f'#{ test_case +1 } { result }')