# Swimming Pool

def membership(month, fee = 0):
    global min_price

    if month >= 12:
        if fee < min_price:
            min_price = fee
        return
    # 출석일수가 0인 월
    if not days[month]:
        membership(month+1, fee)
    else:
        tmp = prices[0] * days[month] if prices[0] * days[month] < prices[1] else prices[1]
        membership(month +1, fee + tmp)
        membership(month +3, fee + prices[2])
                
T = int(input())

for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    days = list(map(int, input().split()))
    tmp = sum(days) * prices[0] # 전부 1일권으로 계산했을 때
    min_price = tmp if tmp < prices[-1] else prices[-1] # 초기화
    membership(0)
    print(f'#{tc} {min_price}')