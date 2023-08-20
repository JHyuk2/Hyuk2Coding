# 셀프 넘버

# 10000 이하의 셀프 넘버를 하나씩 출력하기.
is_selfnum = [0] + [1 for _ in range(10001)]
           
for number in range(1, 10001):
    if is_selfnum[number] :
        print(number)
    temp_sum = number
    num_elements = list(map(int, str(number)))
    temp_sum += sum(num_elements)

    # index out of range 피하기
    if temp_sum < 10001:
        is_selfnum[temp_sum] = 0
