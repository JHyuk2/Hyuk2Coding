from collections import deque

def find_num(start_num, target_num):
    queue = deque([(start_num, 0)])
    visited = [0] * 1000001
    visited[start_num] = 1

    while queue:
        elem = queue.popleft()
        cur, cnt = elem
        for cn in [cur+1, cur-1, cur*2, cur-10]:
            if cn < 0 or cn > 1000001:
                continue
            elif visited[cn]:
                continue
            else:
                if cn == target_num:
                    return cnt+1
                visited[cn] = 1
                queue.append((cn, cnt+1))

for tc in range(int(input())):
    start, target = map(int, input().split())
    res = find_num(start, target)
    print(f'#{ tc+1 } {res}')