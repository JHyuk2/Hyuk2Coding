## time complexity fail

# T = int(input()) # 테스트케이스 횟수

# for t in range(T):
#     days = int(input()) # 장이 열리는 날 & 물건 개수 _
#     result = 0
#     goods = list(map(int, input().split())) # 공백으로 가격을 입력받음.

#     for idx, price in enumerate(goods): # 각각 idx와 price로 받아서, 언제 팔지 얼마에 팔지 정함.
#         max_profit = 0 # 물건을 최대로 팔 수 있을 때의 가격
#         for p in goods[idx:]: # idx+1로 설정하면 인덱스 에러가 나며, 자기 자신과 비교했을 땐 이득이 생길 수 없으므로 idx부터 비교함.
#             if p - price > max_profit:
#                 max_profit = (p-price)
#         result += max_profit
#     print(f'#{t+1} {result}')

## ---------------------------------------------------------------------------------------------------------------------------------

# 마찬가지로 time complexity fail

# T = int(input()) # 테스트케이스 횟수

# for t in range(T):
#     days = int(input()) # 장이 열리는 날 & 물건 개수
#     result = 0
#     goods = list(map(int, input().split())) # 공백으로 가격을 입력받음.

#     for idx, price in enumerate(goods): # 각각 idx와 price로 받아서, 언제 팔지 얼마에 팔지 정함.
#         max_profit = max(goods[idx:]) - price # 물건을 최대로 팔 수 있을 때의 가격
#         result += max_profit
#     print(f'#{t+1} {result}')

## ---------------------------------------------------------------------------------------------------------------------------------

## 역방향으로 찾기.

T = int(input()) # 테스트케이스 횟수

for t in range(T):
    days = int(input()) # 장이 열리는 날 & 물건 개수
    result = 0
    goods = list(map(int, input().split())) # 공백으로 가격을 입력받음.
    max_profit = goods[-1] # 마지막 날의 가격을 max로 설정.
    goods.reverse() # 순서 뒤집기
    
    for price in goods:
        if price > max_profit:
            max_profit = price
        result += max_profit-price

    print(f'#{t+1} {result}')