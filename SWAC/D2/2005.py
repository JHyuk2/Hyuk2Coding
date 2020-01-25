# 파스칼의 삼각형 구하기

## 2차원 배열로 만든다고 하면..
#            (0, 0) 
#        (1, 0) (1, 1)
#     (2, 0) (2, 1) (2, 2)
# (3, 0) (3, 1) (3, 2) (3, 3)

# 즉 tmp = [[] for _ in range(i)] * 2차원 배열 생성
# 대충 규칙을 파악하자면
# (j==0) or (j == i) 인 경우, 1의 값을 넣는 배열로 설정. 2차원 배열 안에 집어넣는다.
# ex) (3,0) ==> j==0, 1
# ex) (3,3) ==> j==i, 1
# 그 외의 경우 
# ex) (3,1) ==> (2,0) + (2,1) # 즉 (i, j) = (i-1, j-1) + (i-1, j) 로 정의할 수 있음.
# ex) (3,2) ==> (2,1) + (2,2)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    tmp = [[] for _ in range(N)] # (N * none)2차원 배열 생성
    print(f'#{ test_case }')
    for i in range(N):
        for j in range(i+1):
            if (j == 0) or (j == i):
                tmp[i].append(1)
            else:
                tmp[i].append(tmp[i-1][j-1] + tmp[i-1][j])
            
            print(tmp[i][j], end =' ')
        print()
