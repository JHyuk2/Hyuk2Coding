from collections import deque
import sys

queue = deque()

for _ in range(int(sys.stdin.readline())):
    temp = sys.stdin.readline().split()
    cmd = temp[0]
    # cmd == push
    if len(temp) == 2:
       queue.append(temp[1])
    
    # cmd != push
    else:
        if cmd == 'front':
            print(queue[0] if len(queue) else -1)
        elif cmd == 'back':
            print(queue[-1] if len(queue) else -1)
        elif cmd == 'pop':
            try:
                print(queue.popleft())
            except:
                print(-1)
        elif cmd == 'size':
            print(len(queue))
        
        # cmd == 'empty'
        else:
            print(0 if len(queue) else 1)


