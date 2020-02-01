n = 72
a = 84497
b = '33788'

tmp = list(b)
print(tmp)
j = 0
j = tmp.index(max(tmp))


max_result = sorted(tmp, reverse = True)
temp_same =[]
temp_differ = []

for idx, num in enumerate(tmp):
    if tmp[idx] == max_result[idx]:
        temp_same.append((idx, num))

    else:
        temp_differ.append(num)

print(temp_same)
print(temp_differ)

# 이렇게하면 딱 됨.
# temp_differ.insert(temp_same[0][0], temp_same[0][1])

print(temp_differ)
temp_differ.insert(4, '9')
print(temp_differ)
tt = []
for t in tt:
    print('hello')