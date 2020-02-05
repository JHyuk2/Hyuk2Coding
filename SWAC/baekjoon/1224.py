# 스위치 켜고 끄기

# 스위치개수  n
# 스위치 상태 0 or 1
# 학생 수 100 이하의 자연수 s명
# 네째 줄부터는 학생의 성별(남1 여2) 학생이 받은 숫자  n 이하.

n = int(input()) # 스위치 개수
switch = list(map(int, input().split())) # 상태
s = int(input()) # 학생 수
d = [list(map(int, input().split())) for _ in range(s)] # [sex, num] 순서로 s 개만큼 받음


# 0 < -- > 1
def state_change(state):
    if state == 0:
        return 1
    else:
        return 0

# 여학생
def isPalindrome(switch, num):
    idx = num-1
    i = 1

    while 0 < idx + i <= len(switch)-1 and 0 <= idx - i < len(switch)-1:
        if switch[idx+i] == switch[idx-i]:
            switch[idx+i] = state_change(switch[idx+i])
            switch[idx-i] = state_change(switch[idx-i])
            i += 1
            continue
        else:
            break

    switch[idx] = state_change(switch[idx])                
    return switch

# 남학생
def Multinum_change(switch, num):
    for idx, state in enumerate(switch):
        if (idx+1) % num is 0: # idx => 0부터 시작.
            state = state_change(state)
            switch[idx] = state
    return switch

## 스위치는 한 줄에 1~20개만 나열 가능
# 만약 21번째인 경우, 2번째 줄 첫번째에 나열.

# 바뀌는거까진 확인.
for sex, num in d:
    if sex == 1:
        switch = Multinum_change(switch, num) # 1, 3 투입

    if sex == 2:
        switch = isPalindrome(switch, num) # 2, 3투입


cnt = 1
for idx, state in enumerate(switch):
    if cnt == 20:
        print(state)
        cnt = 1
    else:
        cnt+=1
        print(state, end  = ' ')
