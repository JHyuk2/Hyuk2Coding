T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    tmp= input()
    cnt = 0
    tmp_list = []
     
    for t in tmp:
        if t == '0':
            if cnt is 0:
                continue
            else:
                tmp_list.append(cnt)
                cnt = 0
                continue
        if t == '1':
            cnt += 1
    else:
        tmp_list.append(cnt)
         
    print('#{} {}'.format(tc, max(tmp_list)))