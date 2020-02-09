T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tmp= input()
    
    idx = 0
    cnt = 0
    result = []
    
    while idx < len(tmp):
        if tmp[idx] == '0':
            idx +=1
            continue
            
        if tmp[idx] == '1':
            cnt = 1
            while idx +1 < len(tmp) and tmp[idx+1] == '1':
                idx+=1
                cnt+=1
            else:
                result.append(cnt)
                idx += 1
                
    print(result)