# from pprint import pprint
# import sys
# sys.stdin = open('input.txt')

# T = int(input())
T = 1

for tc in range(1, T+1):
    # N = int(input()) # 8
    # d = list(map(int, input().split())) # [1, 2, 3, 4, 5, 1, 2, 3]
    N = 8
    d = [1, 2, 3, 2, 3, 4, 1, 2, 3]
    # d = [1, 2, 3, 4, 5, 1, 2, 3]
    print(d, '- 각 구역별 고구마')
    long_julgi = [] # 긴 줄기
    Goguma = [] # 긴 줄기당 고구마 개수
    cnt = 0 # 긴 줄기의 길이
    g_cnt = 0 # 고구마 더하기
    for i in range(1, N):
        if d[i-1] < d[i]: # 1 2 3 4 5 1 2 3
            cnt += 1
            g_cnt += d[i-1]
        else:
            g_cnt += d[i-1]
            long_julgi.append(cnt)
            Goguma.append(g_cnt)
            cnt = 0
            g_cnt = 0
    else:
        g_cnt += d[-1]
    long_julgi.append(cnt)
    Goguma.append(g_cnt)
    print(long_julgi, Goguma)
    result = list(map(list, zip(long_julgi, Goguma)))
    print(result, 'zipping 했음')


    # for aa in result:
    #     for bb in aa:
    #         if aa[0] == 
    break