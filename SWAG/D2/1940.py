# 급발진 RC카!

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    distance = 0
    accel = 0

    for i in range(N):
        if i <8:
            continue

        move = input()
        if move == '0':
            movement, speed = 0, 0
        else:
            movement, speed = tuple(map(int, move.split()))

        if movement == 1:
            accel += speed
        else: # movement ==2 or 0
            accel -= speed
            if accel < 0:
                accel = 0
        
        distance += accel
    print(f'#{ test_case } { distance }')