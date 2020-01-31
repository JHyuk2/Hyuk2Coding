T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # num of cards
    cards = list(map(int, list(input())))
    numbers = [0 for _ in range(10)] # 0~9까지 숫자를 담는 리스트

    card_set = set(cards) # 중복제거
    for card in card_set:
        numbers[card] = cards.count(card)

    max_cnt = 0
    for idx, cnt in enumerate(numbers):
        if cnt >= max_cnt:
            max_cnt = cnt
            result = (idx, cnt)

    print(f'#{ test_case } {result[0]} {result[1]}')