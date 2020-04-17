# 서브트리 노드 개수 구하기.
from copy import deepcopy

class Node:
    def __init__(self, num, parent=None, child=None):
        self.num = num
        self.parent = parent
        self.child = child

for tc in range(int(input())):
    # 간선의 개수 E, 서브트리 루트노드 N
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    node_list = [0] # 선언

    # 1) 노드리스트생성 & 엣지연결
    for idx, num in enumerate(set(edges)):
        node_list.append(Node(num))
        # print(node_list[idx+1].num)
    
    tmp_dict = {i+1:[] for i in range(E)}
    
    print(tmp_dict)
    for i in range(E):
        tmp_n = edges[i*2]
        tmp_child = edges[i*2+1]
        tmp_dict[tmp_n].append(tmp_child)
    print(tmp_dict)
    
    # print('---num, parent, child--------')
    # for idx, n in enumerate(node_list):
    #     if idx==0:
    #         continue
    #     print(n.num, n.parent, n.child)
