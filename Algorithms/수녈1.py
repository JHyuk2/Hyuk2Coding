def f(n, k):
    if n ==k: # 순열 1개 완성
        print(p)
    else:
        for i in range(k): # k개의 원소를 왼쪽부터 탐색
            if u[i] == 0: # 이미 사용한 숫자가 아니면
                u[i] = 1
                p[n] = A[i]
                f(n+1, k) # 다음 자리를 결정하러 이동
                u[i] = 0

A = [1,2,3,4,5]
p = [0] * len(A)
u = [0] * len(A)
f(0, len(A))