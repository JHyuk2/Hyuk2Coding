# 단조감소 / 단조증가 함수 찾기.

# 단조감소 찾는 함수
def find_danjo_decre(arr):
    res = []
    idx = 0

    tmp = []
    while idx < len(arr):
        if idx == 0:
            tmp.append(arr[idx])
        else:
            # 단조 감소인 경우
            if arr[idx-1] >= arr[idx]:
                tmp.append(arr[idx])
                if idx == len(arr)-1:
                    res.append(len(tmp))
            # 여기까지 저장하고 새시작
            else:
                res.append(len(tmp))
                tmp = [arr[idx]]
                if idx == len(arr)-1:
                    res.append(len(tmp))
        # 어떤 작업을 하든 마지막엔 idx+=1
        idx += 1
    return max(res)

def find_danjo_incre(arr):
    res = []
    idx = 0

    tmp = []
    while idx < len(arr):
        if idx == 0:
            tmp.append(arr[idx])
        else:
            # 단조 증가인 경우
            if arr[idx-1] <= arr[idx]:
                tmp.append(arr[idx])
                if idx == len(arr)-1:
                    res.append(len(tmp))
            # 여기까지 저장하고 새시작
            else:
                res.append(len(tmp))
                tmp = [arr[idx]]
                if idx == len(arr)-1:
                    res.append(len(tmp))
        # 어떤 작업을 하든 마지막엔 idx+=1
        idx += 1
    return max(res)

n = int(input())
arr = list(map(int, input().split()))
dc = find_danjo_decre(arr)
di = find_danjo_incre(arr)
result = di if (di > dc) else dc
print(result)