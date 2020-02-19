def sigma(n):
    return 0 if n == 0 else 1 if n == 1 else n + sigma(n-1)


def find_num(point):
    x = point[0]
    y = point[1]
    p_sum = x+y
    start = sigma(p_sum-2)+1
    differ = x-1 # start_x = 1, x = n에서 n-1만큼을 뺀 값.
    return start + differ
    
def find_point(num):
    tmp = 1
    while num > sigma(tmp):
        tmp += 1
    # 루프를 탈출하게 되면 tmp = x + y -1 값이 된다.
    start_num = sigma(tmp-1)+1
    start_x = 1
    start_y = tmp
    differ = num - start_num
    result = [start_x + differ, start_y - differ]
    return result

def star(n1, n2):
    p1 = find_point(n1)
    p2 = find_point(n2)
    x_sum = p1[0] + p2[0]
    y_sum = p1[1] + p2[1]
    return find_num([x_sum, y_sum])

## 실행문
T = int(input())

for tc in range(1, T+1):
    n1, n2 = map(int, input().split())
    print('#{} {}'.format(tc, star(n1, n2)))