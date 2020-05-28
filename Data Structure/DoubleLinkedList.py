## Double Linked List

class Node:
    def __init__(self,data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgnt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self,data):
        if self.head == '':
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            newNode = Node(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode


    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == '__main__' :
    doubleLinkedList = NodeMgnt(0)
    doubleLinkedList.desc()
    for i in range(1,10):
        doubleLinkedList.insert(i)
    doubleLinkedList.desc()

