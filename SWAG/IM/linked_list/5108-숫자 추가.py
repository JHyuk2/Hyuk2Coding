'''
다음 줄부터 테스트 케이스의 별로 첫 줄에 수열의 길이 N, 추가 횟수 M, 출력할 인덱스 번호 L이 주어지고, 다음 줄에 수열이 주어진다.
1
5 2 5
1 2 3 4 5
2 7
4 8

5 5 4
13787 32221 32402 32498 4169
3 5902
3 9752
3 27737
1 14133
0 16547

10 10 8
16243 26767 22174 25277 17456 13398 29850 22297 1382 31246
9 23198
7 17514
11 24247
0 25306
2 9104
6 28112
12 7491
10 26972
17 22639
12 28722

#1 4
#2 32402
#3 13398
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# 링크드리스트에 필요한 기능
# 1) 노드 추가
# 2) 노드 삭제
# 3) 헤드, 테일 구하기
# 4) 길이 구하기

# doubly-linkedlist 구현
class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None
        self.num_of_data = 0

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def size(self):
        return self.num_of_data

    def appendleft(self, node):
        new_node = Node(data)
        if not self.head :
            self.head = new_node
            self.tail = new_node
            self.num_of_data += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    # append_right
    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.num_of_data += 1
        else:
            self.head = new_node
            self.tail = new_node
            self.num_of_data += 1

    # pop_left
    def pop_left(self):
        if self.head :
            self.head.next.prev = None
            self.head = self.head.next
            self.num_of_data -= 1
        # 데이터가 비어있는 경우
        else:
            print('리스트가 비어있습니다.')

    # pop_right
    def pop(self):
        if self.tail :
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.num_of_data -= 1
        else:
            print('리스트가 비어있습니다.')

    # index_insert
    def insert(self, index, data):
        if index > self.num_of_data:
            print('ERROR: index out of range error')

        elif index == self.num_of_data:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.num_of_data += 1
        else:
            cur = self.head
            print(type(cur), cur.data)
            while index:
                cur = cur.next
                index -= 1
            cur.data = data                
            cur.prev = cur.next.prev
            cur.prev.next = cur
            cur.next.prev = cur
            self.num_of_data += 1

    def get_indexnum(self, index):
        if index > self.num_of_data :
            return -1
        elif index == self.num_of_data:
            return self.tail.data
        else:
            self.cur = self.head
            while index:
                self.cur = self.cur.next
                index -= 1
            return self.cur.data

for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tmp_list = list(map(int, input().split()))
    
    LL = Linked_list()
    for i in range(len(tmp_list)):
        LL.append(tmp_list[i])
    
    for i in range(M):
        index, data = map(int, input().split())
        LL.insert(index, data)

    for i in range(LL.size()):
        res = LL.get_indexnum(i)
        print(res)
    
# 3
# 5 2 5
# 1 2 3 4 5
# 2 7
# 4 8

# 1 2 7 3 8 4 5