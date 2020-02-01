## ----- 이러면 타임에러 나옴. 다시짜보자.
"""
# 숫자가 들어왔을 때 좌표를 찾는 함수
def find_point(num):
    start = 2
    find_num = 0 
    # 시작은 x+y = 2
    while True:
        for x in range(start):
            for y in range(start):
                if x + y == start:
                    if x > 0 and y > 0:
                        find_num +=1
                        if find_num == num:
                            find_num
        start += 1 

def find_num(point):
    point_x, point_y = point[0], point[1]
    start = 2
    find_num = 0 
    while True:
        for x in range(start):
            for y in range(start):
                if x + y == start:
                    if x > 0 and y > 0:
                        find_num +=1
                        if x == point_x and y == point_y:
                            return find_num                
        start += 1 

def star(num1, num2):
    point1 = find_point(num1)
    point2 = find_point(num2)
    print(point1, point2)
    
    x = point1[0] + point1[0]
    y = point1[1] + point2[1]
    real = (x,y)
    return find_num(real)

T = int(input())

for test_case in range(1, T+1):
    num1, num2 = map(int, input().split())
    result = star(num1, num2)
    print(f'#{test_case} {result}')


"""

#충격 더오래걸림
'''
def find_point(num):
    cross_sum = 2
    start = 1
    end = 1
    tmp = 1
    while True:
        start += tmp
        tmp +=1
        end += tmp
        cross_sum +=1
        if start <= num <= end:
            break
    
    for x in range(1, cross_sum):
        y = cross_sum - x
        if num == start:
            return (x,y)
        start +=1

def find_num(point):
    x = point[0]
    y = point[1]
    cross_sum = x+y
    tmp = 1
    start, end = 1, 1
    
    # 1) cross_sum line을 찾음
    for i in range(cross_sum-2): 
        start += tmp
        tmp +=1
        end += tmp

    # 2) 좌표를 통해 숫자찾기
    start_x = 1
    start_y = cross_sum - start_x

    for i in range(cross_sum -1):
        print(start_x, start_y)
        if start_x == x and start_y == y:
            return start
        else:
            start += 1
            start_x += 1
            start_y -= 1

def star(num1, num2):
    p1 = find_point(num1)
    p2 = find_point(num2)
    
    # 두 포인트의 x, y합
    real_point = tuple(map(sum, zip(p1,p2)))
    return find_num(real_point)

T = int(input())

for test_case in range(1, T+1):
    num1, num2 = map(int, input().split())
    result = star(num1, num2)

    print(f'#{ test_case } { result }')
'''

def find_point(num):
    cross_sum = 2
    find_num = 0 
    # p1_x, p1_y = 0, 0 # num1의 점
    # p2_x, p2_y = 0, 0 # num2의 점
    
    # 시작은 x+y = 2
    while True:
        for x in range(1, cross_sum):
            y = cross_sum - x
            find_num +=1
            if find_num == num:
                return (x, y)
        cross_sum +=1


def find_num(point):
    point_x, point_y = point[0], point[1]
    cross_sum = 2
    find_num = 0 

    while True:
        for x in range(1, cross_sum):
            y = cross_sum - x
            find_num +=1
            if x == point_x and y == point_y:
                return find_num
        cross_sum +=1     

def star(num1, num2):
    p1 = find_point(num1)
    p2 = find_point(num2)

    real_point = tuple(map(sum, zip(p1,p2)))
    return find_num(real_point)

print(star(2, 3))
# T = int(input())

# for test_case in range(1, T+1):
#     num1, num2 = map(int, input().split())
#     result = star(num1, num2)
#     print(f'#{test_case} {result}')
