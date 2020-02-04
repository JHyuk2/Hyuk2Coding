def find_min(number_list, length):
    # len 1인 경우 0부터
    if length ==1:
        start_num = 0
    
    # 나머지는 10, 100.. 부터 시작
    else:
        start_num = 10

    if length == 1:
        tmp = [i for i in range(10)] # 0~9
    else:
        tmp = [i for i in range(10**(length-1), 10**length)]

    # 2자리, 3자리씩 끊었을 때 04, 05, 06처럼 나오는 숫자 방지
    compare = []
    for i in range(len(numbers)-length+1):
        if int(number_list[i:i+length]) >= start_num:
            compare.append(int(number_list[i:i+length]))
    
    # 중복제거하고 정렬
    compare = list(sorted(list(set(compare))))
    # 모든 숫자가 있으면 다음으로 패스
    if tmp == compare:
        return find_min(number_list, length+1)
    else:
        for idx, num in enumerate(tmp):
            if compare[idx] != num:
                return num

T = int(input())

for tc in range(1, T+1):
    # N에 따라서 20개씩 끊어받음. => 조심히 보자..
    N = int(input()) # 입력받을 자리수
    iter_num = (N-1)//20 + 1
    # 그냥 붙어있는 문자열로 처리하고싶음.
    numbers = ''.join(list(''.join(list(input().split())) for _ in range(iter_num)))
    length = 1 
    result = find_min(numbers, length)
    
    print('#{} {}'.format(tc, result))