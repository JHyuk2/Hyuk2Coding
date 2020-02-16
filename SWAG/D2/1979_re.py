
# 한 줄에 각각 몇칸짜리가 들어갈 수 있는지 저장.
def cnt_length(tmp_list):
    j = 0
    result = []
    while j < len(tmp_list):
        cnt = 0
        if tmp_list[j] == 0:
            j+=1
            continue

        else:
            while j < len(tmp_list):
                cnt += 1
                if j+1 < len(tmp_list) and tmp_list[j+1] == 1:
                    j +=1
                else:
                    result.append(cnt)
                    j +=1
                    break
    return result

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    tmp_list = [list(map(int, input().split())) for _ in range(N)]
    rota_tmp = list(zip(*tmp_list))
    result = 0

    for i in range(len(tmp_list)):
        tmp = cnt_length(tmp_list[i]).count(K) + cnt_length(rota_tmp[i]).count(K)
        result += tmp
        
    print('#{} {}'.format(tc, result))