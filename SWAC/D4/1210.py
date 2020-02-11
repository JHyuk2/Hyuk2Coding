# ladder -1

# 1) 2_마지막부터 시작해서 거꾸로 올라간다. ~ start_point 찾기.
# 2) 왼쪽 or 오른쪽 길이 있으면 쭉 따라감. 길이 끝나면 다시 한칸 위로.

for tc in range(1, 11):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = [idx for idx, num in enumerate(ladder[-1]) if num == 2][0]
    x = 99 # 100 - 1
    
    while x > 0:
        # 왼쪽에 길이 있는 경우
        if 0 < y <= 99 and ladder[x][y-1] == 1:
            while 0 < y < 99 and ladder[x][y-1] ==1:
                y -=1
        elif 0 <= y < 99 and ladder[x][y+1] == 1:
            while 0 < y < 99 and ladder[x][y+1] ==1:
                y +=1
        x -= 1
    
    print('#{} {}'.format(tc, y))