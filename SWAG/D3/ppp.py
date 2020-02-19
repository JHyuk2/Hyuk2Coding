a = 123

tmp = [55, 444, 123, 222, 534]

tmp_list = list(map(lambda x: x-a, tmp[1:4]))
print(tmp_list)
