n = 66
temp_sum = 0
temp = 1 
while n > temp_sum:
    temp_sum += temp
    temp += 1

if n == temp_sum:
    print(temp-1)
else:
    print(temp-2)