# 단조감소 / 단조증가 함수 찾기.

# 단조 증가&감소 찾는 함수
def find_danjo(arr):
    res = []
    idx = 0
    decre = 0
    incre = 0
    tmp = 0 

    while idx < len(arr):
        # idx == 1인 경우,
        if idx == 0:
            incre +=1
            decre +=1
        # 그 외
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

n = int(input())
arr = list(map(int, input().split()))
