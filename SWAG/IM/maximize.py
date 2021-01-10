'''
5,7,3,7,4,6,3,4

5,5,3,1,3,3,4,5
7,2,5,9,1,10,9,9,4,4,9,1
4,5,1,10,7,8,3,10,8,3,4,1,12,1,4,10,5,1,2,4,11
7,4,8,4,6,6,4,2,10,5,9,12,8,8,9,5,5,1,1,11,9,12,9,4,5
'''

from itertools import combinations

input_list = list(map(int, input().split(',')))
sorted_numset = sorted(list(set(input_list)))
print(f'sorted_numset : {sorted_numset}')

test_list = []
for i in range(1 << len(sorted_numset)):
    bit = i
    tmp = [0 for _ in range(len(sorted_numset))]
    if bit != 0:
        for j in range(len(sorted_numset)):
            if (1 & bit >> j) == 0:
                continue
            tmp[j] = 1
    
    selected = []        
    for idx in range(len(tmp)):
        if tmp[idx]:
            if len(selected) == 0:
                selected.append(sorted_numset[idx])
            
            # 비어있지 않으면
            else:
                if selected[-1] - sorted_numset[idx] == -1:
                    break
                else:
                    selected.append(sorted_numset[idx])
    if selected:
        test_list.append(selected)

max_result = 0
res_list = list()

for tl in test_list:
    tmp_sum = 0
    for elem in tl:
        tmp_sum += (elem * input_list.count(elem))
    if tmp_sum > max_result:
        max_result = tmp_sum
        res_list = tl

print(max_result, res_list)