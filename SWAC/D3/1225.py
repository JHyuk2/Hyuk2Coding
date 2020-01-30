def cycle(tmp_list):  
    while True: #무한반복
        step = 0    

        for i in range(5):
            step +=1
            tmp = tmp_list[1:]

            if tmp_list[0] - step <= 0:
                tmp.append(0)
                return tmp
            
            else:
                tmp.append(tmp_list[0] -step)
                tmp_list = tmp

for test_case in range(1, 11):
    N = int(input()) # 안씀
    tmp_list = list(map(int, input().split()))
    result = list(map(str, cycle(tmp_list)))
    print(f"#{ test_case } { ' '.join(result) }")