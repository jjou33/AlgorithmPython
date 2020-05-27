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

    def insertNode(self,data):
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

    def searchNode(self,side,data):
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

    def deleteNode(self,data):
        if self.head == None:
            print ("해당 노드가 없습니다.")
        else:
            if self.head.data == data:
                temp = self.head
                self.head = self.head.next
            else:
                node = self.head
                while node.next:
                    if node.data == data:
                        temp = node
                        node.next = node.next.next
                        del node
                        return
                    else:
                        node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

if __name__ == '__main__':
    testLinkedList = NodeMgnt(0)
    testLinkedList.desc()
    for i in range(1,10):
        testLinkedList.insertNode(i)
    testLinkedList.desc()
    testLinkedList.searchNode("next", 4)
    testLinkedList.searchNode("prev", 0)
    testLinkedList.searchNode("prev", 9)
    print("-----------")
    testLinkedList.deleteNode(0)
    testLinkedList.deleteNode(2)
    testLinkedList.desc()