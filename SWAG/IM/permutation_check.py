from itertools import permutations

input_list = input().split(',')
permute_list = list(permutations(input_list, len(input_list)))

res = 0
res_list = list()

for tmp_list in permute_list:
    cnt = 0
    for i in range(len(input_list)):
        if tmp_list[i] > input_list[i]:
            cnt += 1
    if cnt > res:
        res = cnt
        res_list = tmp_list

print(f'result: {res}')

'''
3,1,2
4,4,4,4,3,4
2,6,7,1,6,5,6,6,3,1
3,6,8,6,1,7,1,6,5,7,4,6
3,6,5,7,6,8,6,8,1,10,9,8,7,7,1,8,7
'''