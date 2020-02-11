
# 마주보는 눈끼리 이어주는 함수
def dice_mapping(dice):
    tmp = [[dice[0], dice[5]], [dice[1], dice[3]], [dice[2], dice[4]]]
    return tmp

# 아래 주사위의 위로 향하는 눈이 i인 경우, 위의 주사위의 윗눈을 구해주는 함수
def lookup(below_num, mapping_dice):
    # 윗면
    for d in mapping_dice:
        if below_num in d:
            up = d[:]
            up.pop(up.index(below_num))

    # 옆면
    remains = [i for i in range(1, 7) if i not in (up + [below_num])]
    return up[0], max(remains)

# dice
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
mapped_dices = list(dice_mapping(dice) for dice in dices)

# 첫 번째 주사위부터 그냥 lookup 적용하면 위는 알아서 결정됨.
res = []

for below_num in range(1, 7):
    tmp = 0
    for idx, dice in enumerate(mapped_dices):
        if idx == 0:
            up, sides = lookup(below_num, dice)
            tmp += sides
            # print('-------------')
            # print(below_num, up, sides)
            
        else:
            up, sides = lookup(up, dice)
            tmp += sides
            # print(below_num, up, sides)
    res.append(tmp)
    
print(max(res))
