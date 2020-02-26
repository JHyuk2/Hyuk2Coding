# castle defense

# 1) combination 구하기
# 2) attack, go

# # 개수에 맞는 콤비네이션 생성
res = []
def combinations(tmp_list, elem, current):
    if not elem:        
        res.append(current)
        return
    
    for i in range(len(tmp_list) - elem+1):
        cur_copy = current[:]
        cur_copy.append(tmp_list[i])
        combinations(tmp_list[i+1:], elem-1, cur_copy)


tmp_list = [1,2,3,4,5]
elem = 3
current = []

combinations(tmp_list, elem, current)
print(res)