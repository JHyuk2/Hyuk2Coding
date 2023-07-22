# https://www.acmicpc.net/group/practice/view/18210/6

# 백트래킹으로 풀어야 하나?
# N = int(input())
# n = int(input())

from collections import deque
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

# 인접 리스트 사용
graph = []

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)
for i in range(1, n+1):
    graph[i].sort() # 순서 보장을 위해 오름차순

print(graph)




# 1. 만약 숫자가 break_nums에 들어가있으면 그냥 사용
# 1-1. 없으면 최근접 인덱스로 따라가기. (위로 한칸, 아래로 한칸)
# 1-2. 최근접 인덱스가 break_num에 포함되어있으면 위로 한칸 더 가기.
# 
# break_nums = list(map(int, input().split()))

'''
5457ㅇ
3
678
'''
# 0~9까지의 숫자리스트 생성

