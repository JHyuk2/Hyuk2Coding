# 퍼펙트 셔플
# 큐로 구현 or zip함수 사용

def shuffle(str_data):
    tmp_list = str_data.split()

    # 1) 반으로 나누기
    middle = (len(tmp_list)+1)//2
    tmp_1 = tmp_list[:middle]
    tmp_2 = tmp_list[middle:]
    
    # 2) 큐에서 순서대로 꺼내기
    # 2-1) 서로 개수 안맞을 때, 맨 뒤에 공백 추가
    if len(tmp_1) != len(tmp_2):
        tmp_2.append(' ')
    
    tmp_res = list(zip(tmp_1, tmp_2))
    result = ''
    for r in tmp_res:
        result += r[0] + ' '
        result += r[1] + ' '
    
    # 마지막에 출력은 string형태로 출력...?
    return result.strip()

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    data = input()

    print(f'#{tc} {shuffle(data)}')