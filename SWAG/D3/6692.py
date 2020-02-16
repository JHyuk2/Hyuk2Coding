# ps.다슬씨 도망가요

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = []
    
    for i in range(N):
    	p1, x1 = map(float, input().split())
    	result.append((p1, x1))
	
    avg = 0
    for j in result:
        avg +=(j[0] * j[1])
    print(f'#{test_case} {avg:.6f}')