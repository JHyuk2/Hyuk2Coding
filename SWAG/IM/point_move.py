p = 1
q = 0
cnt = 0
prime_list = [2]


def is_prime(num):
    start = prime_list[-1]
    for tmp_num in range(start+1, num+1):
        flag = 1
        for p_num in prime_list:
            if flag :
                if tmp_num % p_num == 0:
                    flag = 0
            else:
                break
        else:
            prime_list.append(tmp_num)    
    if num in prime_list:
        return 1
    else:
        return 0
print(is_prime(18))


while q <= 10:
    cnt += 1
    print(p, q, cnt)

    if is_prime(p):
        p += 2
        continue
    else:
        p += q
        q += 2
        continue
    
print(cnt)