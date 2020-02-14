import copy

V, E = map(int,input().split())

# 1. 인접행렬로 만들기. (2중 배열)
# [[]]
## V**2 사이즈의 행렬 만들기
tmp = []
graph = [[0 for _ in range(V)] for _ in range(V)] 

for _ in range(E):
    node1, node2 = map(int, input().split())
    graph[node1][node2] = 1
    graph[node2][node1] = 1

# for i in range(V):
#     print(graph[i])

def find_friends(graph, tmp, to):
    if len(tmp) == 5:
        print(tmp)
        return 1

    # 왔던 곳으로는 갈 수 없다.
    fr = [i[0] for i in tmp]
    flag = 0
    result = 0
    print(fr)

    # ex_) [1,7]을 받으면 [7, n]을 검사.
    for j in range(len(graph)):
        if graph[to][j] == 1 and j not in fr:
            print('here', (to, j))
            flag =1
            tmp_copy = copy.deepcopy(tmp)
            tmp_copy.append([to, j])
            result += find_friends(graph, tmp_copy, j)

    if flag == 0:
        return 0
    
    return result

res = 0
for i in range(V):
    for j in range(i+1, V):
        if graph[i][j] == 1:
            tmp = [[i,j]]
            res += find_friends(graph, tmp, j)
print(bool(res))


# 2. 인접 리스트로 만들기. (딕셔너리)
# {N: []}