n, k = map(int, input().split())
cel = list(map(int, input().split()))
# while len(cel) != n:
#     cel += list(map(int, input().split()))
    
if n == k:
    print(sum(cel))

else:
    now = sum(cel[:k])
    tmp_max = now
    for i in range(k, len(cel)):
        now += (cel[i] - cel[i-k])
        if now > tmp_max:
            tmp_max = now
        
    print(tmp_max)