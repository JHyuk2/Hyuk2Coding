from collections import deque

num = 1000

queue = deque([(num, 0)])

while queue:
    node, count = queue.popleft()

    if node == 1:
        print(node, count)
        break
    
    if node%3 == 0:
        queue.append((node//3, count+1))
    if node%2 == 0:
        queue.append((node//2, count+1))

    
    queue.append((node-1,count+1))