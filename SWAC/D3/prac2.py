tmp = list('377275')
max_result = sorted(tmp, reverse=True)

tmp_same = []
tmp_copy = tmp[:]
max_copy = max_result[:]

print(tmp_copy)
print(max_copy)

for idx, num in enumerate(tmp):
    if max_result[idx] == tmp[idx]:
        tmp_same.append((idx, num))
        del tmp_copy[idx]
        del max_copy[idx]


print(tmp_copy, max_copy)
print(tmp_same[1][0])
for i in range(len(tmp_same)):
    tmp_copy.insert(tmp_same[i][0], tmp_same[i][1])
print(tmp_copy)