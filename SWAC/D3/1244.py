'''
3
123 1
2737 1
32888 2
'''

T = int(input())

def swap(numbers, count):
    # 1) 내림차순으로 정렬 => 가장 큰 수
    max_result = sorted(numbers, reverse = True)
    
    # 2) max값과 같은 인덱스에 있으면 일단 제외.
    tmp = []
    numbers_copy = numbers[:]
    max_copy = max_result[:]

    for idx, num in enumerate(numbers):
        if numbers[idx] == max_result[idx]:
            tmp.append((idx, num)) # 임시저장 해놓고 numbers, max_result에서 제외해주자. 나중에 같은 부분에 insert 해주면 된다.
            del numbers_copy[idx]
            del max_copy[idx]
    
    # 3) 남은 것들끼리 비교해서, 첫 번재 자리수에 max값이 아닌 경우 조정해준다.
    for i in range(1,count+1):
        if count == 1: #카운트가 1일 때, 1이 아닐 때로 나뉜다.
