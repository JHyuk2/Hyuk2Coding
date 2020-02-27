# castle defense

# 1) combination 구하기
# 2) attack, go

# # 개수에 맞는 콤비네이션 생성
res = []
def combinations(width, elem, current):
    tmp_list = [i for i in range(width)]
    if not elem:        
        res.append(current)
        return
    
    for i in range(len(tmp_list) - elem+1):
        cur_copy = current[:]
        cur_copy.append(tmp_list[i])
        combinations(tmp_list[i+1:], elem-1, cur_copy)

def shoot(enemy, r, D):
    depth = len(enemy)

    for d in range(1, D+1):
        start_x = depth
        start_y = r
        for i in range(2*d -1):
            if i > d-1:
                nx = s
height, width, distance = 5, 5, 5
elem = 3
current = []

combinations(tmp_list, elem, current)
print(res)