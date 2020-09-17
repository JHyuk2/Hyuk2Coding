'''
input value

3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
'''
def longest_way(pos, steps):
    if pos + k >= n:
        return steps

    tmp_list = [i+pos for i in range(k, 0, -1)] # 갈 수 있는 모든 거리
    for d in tmp_list:
        if d in station_list:
            return longest_way(d, steps+1)
    else:
        return 0

for tc in range(int(input())):
    # k: 최대이동거리, n: 가야하는 거리, m: 정류장의 수
    k, n, m = map(int, input().split())
    station_list = list(map(int, input().split()))

    print(f'#{tc+1} {longest_way(0, 0)}')