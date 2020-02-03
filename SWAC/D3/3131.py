# input 없음

max_num = 20 # 100만
prime_num = [2,3,5,7]

tmp = [False] + [True for _ in range(2, max_num-1)] # 100만개의 0을 만들고

for idx, isPrime in enumerate(tmp):
    num = idx+1
    if num==1:
        continue
    else:
        print(num, isPrime)
        if isPrime: #prime num일 경우
            
            # tmp[(idx+1)::(idx+1)] = [False] * (len(tmp)-(idx+1)//(idx+1))
            print(tmp)

        elif not isPrime:
            prime_num.append(idx+1)
print(prime_num)