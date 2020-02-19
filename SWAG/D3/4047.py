T = int(input())

for tc in range(1, T+1):
    # 카드 13 x 4
    trumps = {
        'S':[0 for _ in range(13)], 
        'D':[0 for _ in range(13)],
        'H':[0 for _ in range(13)], 
        'C':[0 for _ in range(13)], 
    }
    
    # 갖고있는 카드 나눠서 입력받기
    tmp = input() 

    cards = []    
    for idx, c in enumerate(tmp):
        if c in trumps.keys():
            cards.append(tmp[idx:idx+3])

    # 종류와 숫자로 다시 나눠주기
    pattern_cards = [(i[0],i[1:]) for i in cards]


    # trumps 딕셔너리에 추가하기
    for pc in pattern_cards:
        pattern = pc[0]
        num = int(pc[1])-1
        trumps[pattern][num] += 1
    
    # 만약 카드가 2장 이상인 게 있으면 ERROR
    result_dict = {
        'S':0,
        'D':0,
        'H':0,
        'C':0,
    }
    
    result = ''
    for key, val in trumps.items():
        for v in val:
            if v >= 2:
                result = 'ERROR'
                break
            else:
                if v == 0:
                    result_dict[key] += 1
    
    if result != 'ERROR':
        result = ' '.join([str(val) for key, val in result_dict.items()])

    print('#{} {}'.format(tc, result))