# lotto first place = [1, 3, 30, 33, 36, 39]
# bonus = 12

import random

# 1, 2, 3, 4, 5 place
count_dict = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
}

first_place = set([1, 3, 30, 33, 36, 39])
trial = 0
bonus = 12

for _ in range(10000000):
    trial += 1
    temp = set(random.sample(range(1, 46), 6))
    cnt = first_place & temp # intersection
    if len(cnt) == 6:
        count_dict['1'] += 1
    elif len(cnt) == 5:
        if 12 in temp:
            count_dict['2'] += 1
        else:
            count_dict['3'] += 1
    elif len(cnt) == 4:
        count_dict['4'] += 1

print(f'total_trial = {trial}, place_count = {count_dict}')