# sol_1 -> 스택
from collections import deque
def solution(prices):
    prices = deque(prices)
    res = []
    
    for i in range(len(prices)):
        now = prices.popleft()
        cnt = 0
        for j in prices:
            if j>=now:
                cnt +=1
            else:
                res.append(cnt +1)
                break
        else:
            res.append(cnt)
            
    return res

# 스택 사용이 시간이 더 빠르다.
# sol_2 -> 완전탐색
'''
def solution(prices):
    res = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[j] >= prices[i]:
                cnt +=1
                continue
            else:
                res.append(cnt+1)
                break
        else:
            res.append(cnt)
    
    return res
'''