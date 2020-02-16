'''
3
123 1
2737 1
32888 2

count == 2 인 경우
32888 -> 82838
82828 -> 88832

count == 3:
32888 -> 82388
82838 -> 8

'''

def swap(numbers, count):
    # 1) 내림차순으로 정렬 => 가장 큰 수
    max_result = sorted(numbers, reverse = True)
    numbers = list(numbers)
    # 1-2) 들어온 숫자가 이미 최댓값인 경우

    if numbers == max_result:
        # 1-2-a) 동일한 숫자끼리 교환하면 최댓값을 유지할 수 있음
        isGetSame = False
        for n in numbers:
            if numbers.count(n) >=2:
                isGetSame = True
        if isGetSame == True:
            count = 0
            return numbers, count
        # 1-2-b) 동일한 숫자가 없고 count가 짝수인 경우
        elif count %2 == 0: 
            count = 0
            return numbers, count
        # 1-2-c) 동일한 숫자가 없고 count가 홀수인 경우
        else:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1] # 맨뒤숫자를 서로 바꿈
            count = 0
            return numbers, count
    
    # 2) max_result 값과 비교해서 같은 인덱스에 있으면 tmp로 저장 # 후에 같은 인덱스에 insert해줄 예정.
    tmp = []
    numbers_copy = []

    for idx, num in enumerate(numbers):
        if numbers[idx] == max_result[idx]:
            tmp.append((idx, num))

        else: # max값과 다른 값을 갖는경우 순서대로 저장
            numbers_copy.append(num)

    # 3) swap rule.     
    # 3-1) count >=2 & max값이 2개 이상인 경우.
    if count >= 2:
        max_count = numbers_copy.count(max(numbers_copy)) # max의 개수
        if max_count >=2:
            j = 0
            find_max = []
            for _ in range(max_count):
                t = numbers_copy[j+1:].index(max(numbers_copy)) # max의 인덱스를 모두 저장
                find_max.append(t+j+1)
                j += (t+1)
             
            max_count = max_count if max_count < count else count # max = 3
            find_max.reverse()
            swap_place = 0
            for n in numbers_copy[:max_count]:
                if int(n) < int(numbers_copy[0]):
                    swap_place +=1
            swap_index = find_max[swap_place] # 543777 & cnt=3 => 5는 index3의 7과 교환.
            numbers_copy[0], numbers_copy[swap_index] = numbers_copy[swap_index], numbers_copy[0]
    # 3-2) count >= 2 & max_count == 1 인 경우, 그냥 맨앞자리랑 최댓값 자리랑 바꿈
        else: 
            swap_index = numbers_copy.index(max(numbers_copy)) 
            numbers_copy[0], numbers_copy[swap_index] = numbers_copy[swap_index], numbers_copy[0]

    # 3-3) count == 1인 경우, 가장 뒤에 있는 최댓값이랑 바꿈
    else:
        reversed_copy = list(reversed(numbers_copy))
        find_max = reversed_copy.index(max(numbers_copy))
        swap_index = len(numbers_copy) - (find_max + 1)
        numbers_copy[0], numbers_copy[swap_index] = numbers_copy[swap_index], numbers_copy[0]

    # 4) 떼놨던 tmp를 붙여줌
    
    for t in tmp: # t[0] ==> index, t[1] => str
        numbers_copy.insert(t[0], t[1])
    
    count -= 1
    return numbers_copy, count

## 너무 지저분하지만... 다 왔다

T = int(input())

for test_case in range(1, T+1):
    numbers, count = input().split()
    count = int(count)

    while count != 0:
        numbers, count = swap(numbers, count)
    result = ''.join(numbers)
    print(f'#{ test_case } { result }')