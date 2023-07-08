N, M = int(input().split())

temp_list1 = []
temp_list2 = []
for i in range(2*M):
    temp = list(map(int, input().split()))
    print(temp)
    if i//M :
        temp_list2 + temp
    else:
        temp_list1 + temp