# 9 난쟁이
heights = [int(input()) for _ in range(9)]
heights_sum = sum(heights)
flag = 0

for i in range(8):
    for j in range(i+1, 9):
        temp = heights[i] + heights[j]
        if (heights_sum - temp) == 100:
            flag = 1
            break
    if flag :
        break

heights.remove(heights[j])
heights.remove(heights[i])

print(sorted(heights))