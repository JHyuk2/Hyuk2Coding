# 터렛
import math

def find_longer(r1, r2):
    return max(r1,r2)
    
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    answer = 0 

    # case1) x1=x2, y1=y2, r1=r2
    if x1==x2 and y1==y2 and r1==r2:
        answer = -1
    
    # 무한해가 아닌 나머지 경우
    else:
        longer_r = find_longer(r1, r2)
        
        # case2) distance > longer_radius
        if distance > longer_r:
            if r1+r2 > distance: 
                answer = 2
            elif r1+r2 == distance:
                answer = 1
            else:
                answer = 0
        
        # case3) distance < longer_radius
        else: # 
            if abs(r2-r1) > 2:
                answer = 0
            elif abs(r2-r1) == distance:
                answer = 1
            else: # abs(r2-r1) < 2:
                answer = 2
    print(answer)