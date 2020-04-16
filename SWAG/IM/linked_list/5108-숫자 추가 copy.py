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
        if head:
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
    def insert(self, idx, node):
        curn = self.head
        curn.data = data
        prevn = None
        nextn = None

        if not self.head :
            self.head = curn
            self.tail = curn
        else:
            if idx >= self.num_of_data:
                self.tail.next = curn
                self.tail = curn
            else:
                nextn = self.head
                while idx:
                    prevn = nextn
                    nextn = nextn.next
                    idx -=1
                prevn.next = curn
                curn.next = nextn
        self.num_of_data += 1
    
    def get_indexnum(self, idx):
        cur = 0
        curn = self.head
        while idx:
            curn = curn.next
            idx -= 1
        return curn.data
    
    def head(self):
        return self.head
    def tail(self):
        return self.tail

LL = LinkedList()
LL.append(1)
LL.append(3)
LL.insert(1, 2)
print(LL.size())
print(LL.head())
# for i in range(LL.size()):
#     print(LL.get_indexnum(i))

# print(LL.head, LL.tail)