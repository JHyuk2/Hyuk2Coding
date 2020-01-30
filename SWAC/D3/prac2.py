tmp = [5,4,2,1,3,1,3]

def swap_num(tmp):
    for i in range(len(tmp) -1):
        if tmp[i] == max(tmp[i:]):
            print('here-1')
            print(tmp[i], max(tmp[i:]))
            if i == len(tmp)-1: #마지막까지 순회했는데 이미 최신인 경우
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
            else:
                continue
        else:
            print('here-2')
            print(tmp[i], max(tmp[i:]))
            max_index = tmp[i:].index(max(tmp[i:]))
            print(max_index)
            tmp[i], tmp[max_index] = tmp[max_index], tmp[i]
    return tmp
        
new_tmp = swap_num(tmp)
print(tmp)