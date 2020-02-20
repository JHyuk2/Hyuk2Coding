# # 카드게임
# # 1) 가위바위보 함수
# # 2) 그룹 쪼개기
'''
1 -- 가위
2 -- 바위
3 -- 보
'''

# # 1) 가위바위보 - 승자 번호 리턴
def win(p1, p2):
    global data
    if data[p1] == data[p2]:
        return p1
    else:
        return p1 if abs((data[p1]+1) - data[p2])%3 != 0  else p2

# # 2) 그룹 쪼개고 승자 올리기
def half(tmp_group):
    if len(tmp_group) ==2:
        return [win(tmp_group[0], tmp_group[1])]
    
    elif len(tmp_group) == 1:
        return [tmp_group.pop()]
    
    # 길이가 3 이상이면 쪼개고 다시 half 진행
    middle = (len(tmp_group)+1)//2
    tmp_l = [tmp_group[i] for i in range(middle)]
    tmp_r = [tmp_group[i+middle] for i in range(len(tmp_group) - middle)]
    return half(half(tmp_l) + half(tmp_r))

# 실행문
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = list(map(int, input().split()))
    
    # 학생들의 index만 저장한 값.
    tmp = [i for i in range(len(data))]
    result = half(tmp)
    print(f'#{tc} {result.pop() +1}')