## 즉, 인덱스가 0~6까지 있으면 0 -> 6 (0+6) -> 1(8, 15) -> 5 -> 2 -> 4 의 순서로 순회해야 한다.

'''
1 0 0 0 0 0 2 
0 0 0 0 1 2 0
0 0 1 0 2 0 1
1 0 0 0 0 0 0
0 0 0 1 0 2 0
2 1 2 0 0 0 0
0 0 0 2 0 0 0
'''

# 한 줄씩
def one_line_magnetic(tmp_line):
    N = len(tmp_line)
    
    for i in range(N):
        # case 1) 양쪽 끝에서 떨어지는 애들
        if (i == 0 and tmp_line[i] == 2) or (i == N-1 and tmp_line[i] == 1):
            tmp_line[i] = 0

        # case 2) 값이 바뀌어야 되는 애들.
        elif tmp_line[i] == 1 and tmp_line[i+1] == 0:
            tmp_line[i], tmp_line[i+1] = tmp_line[i+1], tmp_line[i]
        elif tmp_line[i] == 2 and tmp_line[i-1] == 0:
            tmp_line[i], tmp_line[i-1] = tmp_line[i-1], tmp_line[i]

        # case 3) 1과 2가 만나는 경우 & 0 인 경우
        else:
            continue

    return tmp_line

# 교착상태가 중복되지 않게 바꿔줌.
def deadlock(tmp_line):
    new_tmp = one_line_magnetic(tmp_line)
    while new_tmp != one_line_magnetic(new_tmp):        
        new_tmp = one_line_magnetic(new_tmp)
        
    return new_tmp

## 문자열로 만든 후 '12', '21'을 골라서 찾아낸다.
def count_deadlock(new_tmp):        
    result = 0
    #
    tmp = ''
    for i in new_tmp:
        if i == 0:
            tmp += ' '
        elif i == 1:
            tmp += '1'
        else:
            tmp += '2'

    # 셀 수 있는 게 하나라도 있으면 무한 반복.
    while tmp.count('12') != 0:
        cnt_12 = 0 
        cnt_12 = tmp.count('12')
        tmp = tmp.replace('12', ' ', cnt_12)
        
        result += cnt_12

    return result
 
## 문제에서 요구하는 바는, 몇 개가 남아있냐가 아니라, 몇 개의 교착상태가 존재하느냐.
for test_case in range(1):
    N = int(input())
    tmp_list = []
    
    ## 1) 배열 생성
    for i in range(N):
        tmp = list(map(int, input().split()))
        tmp_list.append(tmp)
    
    rotate_tmp = list(map(list, zip(*tmp_list)))

    ## 2) 각 줄마다 실행
    result = 0

    for i in range(N):
        rotate_tmp[i] = deadlock(rotate_tmp[i])
        result += count_deadlock(rotate_tmp[i])
    
    print(f'#{test_case+1} {result}')

'''
testcase / real
#5 481 => 
#6 501
#7 488
#8 476
#9 464
#10 490

'''