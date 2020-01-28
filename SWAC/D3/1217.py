
def num_pow(n, p):
    if p == 1:
        return n
    else:
        return n * num_pow(n, p-1)


for test_case in range(10):
    t = int(input()) # test 
    n, power = list(map(int, input().split()))

    result = num_pow(n, power)
    print(f'#{ t } { result }')