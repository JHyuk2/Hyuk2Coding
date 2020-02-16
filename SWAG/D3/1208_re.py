# 테스트케이스 10
# 각 줄의 입력은 입력받는 수 & 값
    
# 덤프 횟수만큼 반복하는데,
# 맥스값, 민값을 구해서 각 자리에 +1 -1 해주면 됨.

for tc in range(10):
    n = int(input())
    d = list(map(int, input().split()))
    
    # 덤프횟수
    for i in range(n):
        # 각 상황에서의 최대최소
        max_num = 0
        min_num = 99999
    
        for idx, num in enumerate(d):
            if num > max_num:
                max_num = num
                max_idx = idx
            if num < min_num:
                min_num = num
                min_idx = idx
        d[max_idx] -= 1
        d[min_idx] += 1
    
    # for문 종료 이후.
    else:
        # 마지막으로 한번 더 max min 찾은 다음 반환.
        max_num = 0
        min_num = 99999
        for idx, num in enumerate(d):
            if num > max_num:
                max_num = num
                max_idx = idx
            if num < min_num:
                min_num = num
                min_idx = idx
        res = d[max_idx] - d[min_idx]
        
    print('#{} {}'.format(tc, res))