n = int(input())
temp = list(map(int, input().split()))

def find_max_dec(temp):
    res = 1
    length = 1
    for i in range(1, len(temp)):
        if temp[i-1] - temp[i] <= 0:
            length += 1
        else:
            if res < length:
                res = length
            length = 1
    # for문이 끝난 경우
    if res < length:
        res = length 
    return res
        
def find_max_inc(temp):
    res = 1
    length = 1
    for i in range(1, len(temp)):
        if temp[i-1] - temp[i] >= 0:
            length += 1
        else:
            if res < length:
                res = length
            length = 1
    
    if res < length:
        res = length
    return res


inc_len = find_max_inc(temp)
dec_len = find_max_dec(temp)
print(max(inc_len, dec_len))

