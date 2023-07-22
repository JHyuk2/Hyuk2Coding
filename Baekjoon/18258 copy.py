class custom_queue:
    def __init__(self, command =None, n=0):
        from collections import deque 
        self.command = command
        self.queue = deque()
        self.temp = 0

    def push(self, n:int):
        self.queue.append(n)

    def pop(self):
        try:
            self.res = self.queue.popleft()
        except:
            self.res = -1
        print(self.res)
        
    def front(self):
        if len(self.queue):
            print(self.queue[0])
        else:
            print(-1)
    
    def back(self):
        if len(self.queue):
            print(self.queue[-1])
        else:
            print(-1)

    def size(self):
        print(len(self.queue))

    def empty(self):
        print(0 if len(self.queue) else 1)
    
    # action
    def action(self, command=None, temp = 0):
        self.command = command
        self.temp = temp

        if self.command == 'push':
            return self.push(self.temp)
        if self.command == 'pop':
            return self.pop()
        if self.command == 'front':
            return self.front()
        if self.command == 'back':
            return self.back()
        if self.command == 'empty':
            return self.empty()
        if self.command == 'size':
            return self.size()
            

n = int(input())

temp_queue = custom_queue()
for _ in range(n):
    temp = input().split()
    cmd = temp[0]
    # push command
    if len(temp) == 2:
        n = temp[1]
        temp_queue.push(n)
    
    # push가 아닌 경우
    else:    
        temp_queue.action(cmd)