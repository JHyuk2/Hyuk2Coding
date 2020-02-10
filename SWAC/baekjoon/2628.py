width, height = map(int, input().split())
cut = int(input())

if cut != 0:
    # 커팅 횟수에 맞게 일단 저장 [0, 4]의 형태로 저장.
    d = [list(map(int, input().split())) for _ in range(cut)] 

    # 0: 가로 / 1: 세로, 정렬해서 받아야 편함.
    hor = list(sorted([i[1] for i in d if i[0] == 1]))
    ver = list(sorted([i[1] for i in d if i[0] == 0]))


    # 연산을 위한 리스트
    # width는 hor로 잘라준다. height는 ver로 잘라준다.
    real_hor = []
    real_ver = []

    # 가로로 종이 쪼개기
    if hor != []:
        for i in range(len(hor)):
            if i == 0:
                real_hor.append(hor[i])
            else:
                real_hor.append(hor[i]-hor[i-1])
        real_hor.append(width-hor[-1])
    else:
        real_hor = [width]

    if ver != []:                
        # 세로로 종이 쪼개기
        for i in range(len(ver)):
            if i == 0:
                real_ver.append(ver[i])
            else:
                real_ver.append(ver[i]-ver[i-1])
        real_ver.append(height-ver[-1])
    else:
        real_hor = [height]
        
    ## 결과출력
    max_paper = 0
    for i in range(len(real_ver)):
        for j in range(len(real_hor)):
            max_paper = real_ver[i] * real_hor[j] if real_ver[i] * real_hor[j] > max_paper else max_paper

    print(max_paper)

else:
    print(width * height)