'''
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
'''

for _ in range(4):
    ac1, ar1, ac2, ar2, bc1, br1, bc2, br2 = map(int, input().split())

    A = [ac1, ar1, ac2, ar2]
    B = [bc1, br1, bc2, br2]

    if ac1 > bc1 :
        ac1, ar1, ac2, ar2, bc1, br1, bc2, br2 =  bc1, br1, bc2, br2, ac1, ar1, ac2, ar2

    res = ''
    # case d) 닿지 않는 경우
    # 위 or 오른쪽 or 아래
    if ar2 < br1 or ac2 < bc1 or br2 < ar1:
        res = 'd'

    # case c) 점으로 닿는 경우
    elif ac2 == bc1 and (ar2 == br1 or ar1 == br2 ):
        res = 'c'

    # case b) 선으로 접하는 경우
    # 위, 아래, 오른쪽
    elif ar2 == br1 or ar1 == br2 or ac2 == bc1:
        res = 'b'

    # case a)
    else:
        res ='a'

    print(res)