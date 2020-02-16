T = int(input())

for test_case in range(1, T+1):
    scores = list(map(int, input().split()))
    scores = [40 if i < 40 else i for i in scores]

    avg = int(sum(scores)/len(scores))
    print(f'{ test_case } { avg }')