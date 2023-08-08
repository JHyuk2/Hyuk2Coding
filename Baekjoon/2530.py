# 인공지능 시계
h, m, s = map(int, input().split())
sec = int(input())

# 시간 더해주기.
s += sec

# 60초 => 1분, 60으로 나누고 남은 시간은 초로 되돌려줌. 
add_m = s // 60
s = s % 60
m += add_m

# 1분 -> 1시간으로 변환해서 더해주기, 남은 시간은 분으로
add_h = m // 60
m = m % 60
h += add_h

# h는 0~23시. (24로 나눈 나머지)
h %= 24

print(h, m, s)