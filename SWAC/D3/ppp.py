tmp = [[i*3+j for j in range(1,4) ]  for i in range(3)]
print(tmp)

tmp_list = list(map(list, zip(*tmp)))


for i in range(3):
    for j in range(3):
        print(tmp[i][j], end = ' ')
    print()

print('-'*30)

for i in range(3):
    for j in range(3):
        print(tmp_list[i][j], end = ' ')
    print()
            
