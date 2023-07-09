E, S, M = map(int, input().split())

# 초기값 설정
E -= 1
S -= 1
M -= 1
year = E

while True:
    if year%15 == E and year%28==S and year%19 == M:
       break 
    year += 15

print(year+1)