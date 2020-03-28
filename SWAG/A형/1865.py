import sys
sys.stdin = open('input.txt')

def work(depth, v, p=1):
    global max_res
    if p <= max_res:
        return
    if depth == len(v):
        max_res = p
    # depth < len(v)
    else:
        for j in range(len(v)):
            if not v[j]:
                v[j] = 1
                work(depth+1,v, p*(prob[depth][j])/100)
                v[j] = 0
            
T = int(input())

for tc in range(1, T+1):
    staff = int(input())
    prob = [list(map(int, input().split())) for _ in range(staff)] #  n by n 행렬 생성
    max_res = 0
    visited = [0 for _ in range(staff)]
    work(0, visited)
    print(f'#{tc} {max_res*100:6f}')

