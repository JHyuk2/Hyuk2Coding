## 건물 조망 탐사

T = 10   


for test_case in range(1, T+1):
    a= int(input()) # 결국 이거 안써먹음
    tmp = list(map(int, input().split()))
    new_tmp = [0, 0] + tmp + [0, 0]
    result = 0

    for i in range(2, len(new_tmp)-2): # 양쪽 끝 +-2 를 제외하고 서칭가능
        now_list = new_tmp[i-2:i+3]
        now = now_list[2] 
        
        first = sorted(now_list, reverse=True)[0] # 최고층
        second = sorted(now_list, reverse=True)[1] # 그 다음높이

        if now == first: 
            result += (first-second)
        
    print(f'#{ test_case } { result }')
    