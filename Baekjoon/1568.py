import sys

n = int(sys.stdin.readline())

def temp_sum(num):
    return num * (num+1) // 2

res = 0
temp = 1
while n:
    if n >= temp_sum(temp):
        temp += 1
        
    else:
        n -= temp_sum(temp-1)
        res += (temp -1)
        temp = 1

print(res)