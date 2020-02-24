# 최장 증가 부분수열 구하기

'''
2
5
1 3 2 5 4
6
4 2 3 1 5 6
'''

# # pos => index 위치
# # tmp => tmp_data
def prog(pos, tmp):
    global data
    global max_len

    # 마지막 인덱스
    if pos == len(data) -1:
        if len(tmp) > max_len:
            max_len = len(tmp)
        return

    # 비어있는 경우
    if not tmp:
        tmp.append(data[pos])
    
    # 비어있지 않으면 끝까지 반복
    for idx, d in enumerate(data[pos+1:]):
        tmp_copy = tmp[:]
        if tmp[-1] <= d:
            tmp_copy.append(d)
            # print(pos, idx, tmp_copy)
            prog(pos+idx+1, tmp_copy)
        else:
            if pos+idx+1 == len(data)-1:
                if len(tmp) > max_len:
                    max_len = len(tmp)
            continue

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    max_len = 0

    for i in range(len(data)):
        prog(i, [])
    
    print(f'#{tc} {max_len}')