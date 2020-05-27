## DoubleLinkedList Delete / Search Function Plus

class Node:
    def __init__(self,data , prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class NodeMgnt():
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
        self.count = 0

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

    def SearchNode(self,side,data):
        if self.head == '':
            self.head = Node(data)
            self.tail = self.head
            print("data가 없어 해당 데이터를 첫 데이터로 삽입하였습니다.")
            return
        if side == "next":
            node = self.head
            while node:
                if node.data == data:
                    print("입력하신 데이터는 앞쪽부터 ", (self.count + 1), "번째 데이터 입니다.")
                    self.count = 0
                    return
                else:
                    node = node.next
                    self.count += 1
        else:
            node = self.tail
            while node:
                if node.data == data:
                    print("입력하신 데이터는 뒷쪽부터 ", (self.count + 1), "번째 데이터 입니다.")
                    self.count = 0
                    return
                else:
                    node = node.prev
                    self.count += 1


    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == '__main__':
    testLinkedList = NodeMgnt(0)
    testLinkedList.desc()
    for i in range(1,10):
        testLinkedList.insert(i)
    testLinkedList.desc()
    testLinkedList.SearchNode("next", 4)
    testLinkedList.SearchNode("prev", 0)
    testLinkedList.SearchNode("prev", 9)