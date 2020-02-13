# stack 구현하기

class Stack:
    def __init__(self):
        self.data = []

    def push(self, e):
        self.data.append(e)
    
    def pop(self):
        if not self.empty():
            return self.data.pop()
        else:
            return -1
    
    # 비어있으면 1, 아니면 0
    def empty(self):
        if bool(self.data): 
            return 0
        else:
            return 1

    def size(self):
        return len(self.data)

    # 비어있으면 -1, 아니면 위
    def top(self):
        if not self.empty():
            return self.data[-1]
        else: 
            return -1
            


n = int(input())
orders = [list(input().split()) for _ in range(n)]
stack1 = Stack()

for order in orders:
    # push, 1로 들어온 경우
    if len(order) ==2:
        e = order[1]
        stack1.push(e)
    else:
        if order[0] == 'pop':
            print(stack1.pop())
        if order[0] == 'empty':
            print(stack1.empty())
        if order[0] == 'size':
            print(stack1.size())
        if order[0] == 'top':
            print(stack1.top())






print(n)