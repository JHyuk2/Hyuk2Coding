T = int(input())

for tc in range(1, T+1):
    N = int(input())
    d = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())

    bus = [0 for _ in range(5000)]

    for start, end in d:
        bus[start-1:end] = list(map(lambda x: x+1, bus[start-1:end]))

    result = []
    
    for p in range(P):
        result.append(str(bus[int(input())-1]))

    print("#{} {}".format(tc, ' '.join(result)))