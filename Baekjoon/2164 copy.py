from collections import deque

n = int(input())
temp = deque([i+1 for i in range(n)])

while len(temp) > 1:
    temp.popleft()
    temp.append(temp.popleft())

if len(temp) == 2:
    print(temp[1])

else:
    print(temp[0])