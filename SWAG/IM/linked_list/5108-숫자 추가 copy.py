## Singly_LinkedList 구현하기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_data = 0
    
    # node append
    def append(self, data):
        new_node = Node(data)
        if self.num_of_data:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.tail = new_node
            self.head = new_node
        self.num_of_data += 1

    def size(self):
        return self.num_of_data
    
    # node insert
    def insert(self, idx, data):
        cur = self.head
        prevn = self.head
        nextn = None

        if not self.head :
            self.head = cur
            self.tail = cur     
        else:
            nextv = cur
            while index:
                prevn = cur
                nexvn = nextv.next
                index -=1
            prev.next = cur
            cur.next = nextv
        self.num_of_data += 1
    
    def get_indexnum(self, idx):
        
    

LL = LinkedList()
LL.append(1)
LL.insert(1, 2)
for i in range(LL.size()):
    print(LL.)

# print(LL.head, LL.tail)