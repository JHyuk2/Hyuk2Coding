# Doubly-LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.num_of_node = 0
        self.head = None
        self.tail = None
    
    def append(self, node):
        new_node = node
        if self.head :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        # head == None
        else:
            self.head = new_node
            self.tail = new_node
        self.num_of_node += 1

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

DLL = DoublyLinkedList()
DLL.append(n1)
DLL.append(n2)
DLL.append(n3)
DLL.append(n4)
