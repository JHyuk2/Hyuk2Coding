
'''
def flatten(hay):
    max_num = max(hay)
    min_num = min(hay)
    cnt = 0

    while max_num != min_num:
        max_idx = hay.index(max_num)
        min_idx = hay.index(min_num)
        hay[max_idx] -= 1
        hay[min_idx] += 1
        max_num, min_num = max(hay), min(hay)
        cnt += 1
    
    return cnt

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    hay = []
    for i in range(N):
        tmp = int(input())
        hay.append(tmp)
    
    result = flatten(hay)

    print(f'#{test_case} {result}')
'''

## 차라리 avg를 구해서 abs값으로 구하는 건 어때

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    hay = []
    for i in range(N):
        tmp = int(input())
        hay.append(tmp)
    
    avg = sum(hay) / N  # 결국 평균값으로 조정해야함.
    differ = [abs(i-avg) for i in hay]
    result = int(sum(differ)/2)

    print(f'#{test_case} {result}')