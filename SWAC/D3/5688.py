T = int(input())

for tc in range(1, T+1):
    N = int(input())

    flt_x = N**(1/3)
    int_x = round((N**(1/3)), 6)

    if abs(flt_x-int_x) < 10**-5:
        result = int_x

    else:
        result = -1
    
    print('#{} {}'.format(tc, result))
        