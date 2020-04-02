'''
3
3 10
5527 731 31274 
5 12
18140 14618 18641 22536 23097 
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907

#1 731
#2 18641
#3 2412
'''
def rotate(cnt, arr):
    length = len(arr)
    real_looper = cnt % length
    return arr[real_looper]

for tc in range(int(input())):
    c, loop_cnt = map(int, input().split())
    num_list = list(map(int, input().split()))
    res = rotate(loop_cnt, num_list)
    print(f'#{tc+1} {res}')