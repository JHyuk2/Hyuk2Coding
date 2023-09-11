# 요세푸스 문제 0
# 순환 큐를 만들면 베스트
from collections import deque

n, k = map(int, input().split())
if n == 1:
    print(f"<{1}>")
else:
    queue = deque([i+1 for i in range(n)])

    res = []
    while queue:
        # 왼쪽으로 두 칸 회전시키기
        queue.rotate(-2) 
        res.append(queue.popleft())


    print(f'<{", ".join(list(map(str, res)))}>')



# class circularQueue:
#     global n
#     rear = 0
#     front = 0
#     MAX_SIZE = n
    
#     def __init__(self):
#         self.rear = 0
#         self.front = 0
#         self.queue = deque([i+1 for i in range(n)])
        
#     def is_empty(self):
#         if self.rear == self.front:
#             return True
#         return False
    
#     def is_full(self):
#         if (self.rear+1)%self.MAX_SIZE == self.front:
#             return True
#         return False
    
#     def enqueue(self, x):
#         if is_full():
#             return

#         self.rear = (self.rear+1) % (self.MAX_SIZE)
#         self.queue[self.rear] = x


#     def next(self,):
#         pass
