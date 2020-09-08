
dist = [
    [2, 1, 0, 0, 0, 0, 2],
    [2, 1, 0, 0, 0, 0, 2]
]

a = list(sum(dist, []))
print(sum(dist, []))

# from collections import deque

# tmp_list = deque([11, 22, 33, 44])

# a = tmp_list.popleft()
# print(a, tmp_list)

# for idx, i in enumerate(tmp_list):
#     if idx == 2:
#         continue
#     print(idx, i)


# from collections import deque
# tmp = deque([1, 2,3,4, 5, 6])
# print(tmp.popleft())
# print(type(tmp))
# set_1 = {1, 2, 3, 4}
# set_2 = {1, 2, 3}

# print(set_1 - set_2)


# steps = 3

# data

# [ 
#     [0, -1, 3]
#     [-1,-1, 2]
#     [0 , *, 1]
# ]

# data
# [ 
#     [4, 3, 2]
#     [3, 2, 1]
#     [4, -1, 0]
# ]

# check
# [ 
#     [1, 1, 1]
#     [1, 1, 1]
#     [1, 0, 1]
# ]

# queue = []

# x = 0
# y = 1
# find_step(0, 1)

# check
# [[1, 1] #             (x-1, y+0)   ||
#  [1, 1] # (x+0, y-1)  (x+0, y+0)   || (x, y+1)
#         # --------------------------
#         #             (x+1, y)
# ]

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
