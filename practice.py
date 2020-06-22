# input
# (1, 3), (3, 6), (2, 5), (3, 8), (4, 1), (4, 5), (7, 2), (6, 4), (4, 7)
# 10, 6, 2, 1, 4, 3, 5, 7, 2, 4, 1, 7, 6, 5, 3, 6, 4, 7, 5, 3, 5, 1, 4, 6

# import re

# N = int(input())
tmp = ''
input_data = input()
for i in input_data:
    if i not in ['(', ')', ',']:
        tmp += i

tmp_list = tmp.split()
print(tmp_list)

# data = []
# for i in range(len(tmp)//2):
#     data.append((tmp[2*i], tmp[2*i+1]))


# graph = {i:[] for i in range(N+1)}
# for d in data:
#     a, b = d
#     print(a, b)
#     graph[a].append(b)
#     graph[b].append(a)

# def find_max(N, graph):
#     max_num = 0
#     res_num = 0
#     for i in range(N+1):
#         res = []
#         for j in graph[i]:
#             res += graph[j]
#             print(res)
#         if len(set(res)) > max_num:
#             max_num = len(set(res))
#             res_num = i
#     return res_num

# print(find_max(N, graph))