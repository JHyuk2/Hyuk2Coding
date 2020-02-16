T = int(input())
result = 1
tmp =[1]

for i in range(T):    
    result *= 2
    tmp.append(result)
    
print(' '.join(list(map(str, tmp))))