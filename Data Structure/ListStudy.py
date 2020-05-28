class Node:
    def __init__(self,data,Next=None):
        self.data=data
        self.next=Next

class NodeMgnt:
    def __init__(self, data):
        self.head = Node(data)
    def add(self,data):
        if self.head == "":
            self.head=Node(data)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(data)
    def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

if __name__ == '__main__':
    linkedList1 = NodeMgnt(0)
    for i in range(1,10):
        linkedList1.add(i)
    linkedList1.desc()