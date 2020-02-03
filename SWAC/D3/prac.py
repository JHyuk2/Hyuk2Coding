arr= [[i*5 + j for j in range(1, 6)]for i in range(5)]

print(arr)

#     좌 우 상 하
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0 ]

result = []

for x in range(len(arr)):
    for y in range(len(arr[0])):
        group_sum =0
        for k in range(4):
            tmp_x = x + dx[k] 
            tmp_y = y + dy[k] 
            if (0 <= tmp_x <=4) and (0<= tmp_y <=4) :
                group_sum += abs(arr[x][y] - arr[tmp_x][tmp_y])
        result.append(group_sum)

print(result)