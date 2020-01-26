T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    temp_list = []

    for n in range(N):
        temp = list(input().split())
        text = temp[0]
        cnt = int(temp[1])
        temp_list.append(text*cnt)
        
    total = ''.join(temp_list) # 전체를 하나로 묶은 text 생성
    print(f'#{test_case}')
    count= 0
    for t in total:
        if count == 10:
            print()
            print(t, end='')
            count =1
            continue
        else:
            print(t, end='')
            count += 1
    print()