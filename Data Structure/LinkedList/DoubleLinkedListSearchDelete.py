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
                after_node = self.head
                self.head = self.head.next
            else:
                node = self.head
                while node.next:
                    if node.next.data == data :
                        temp = node.next
                        node.next = node.next.next
                        del temp
                    else:
                        node = node.next


    def insert_after(self,nodeBefore, data):
        if self.head == None :
            self.head = Node(data)
            print ("노드가 없어 첫번째 데이터로 생성")
            return True
        else:
            node = self.head
            while node.data != nodeBefore :
                node = node.next
                if node.next == Node:
                    return False
            newNode = Node(data)
            print ("newNode >>" , newNode.data, newNode.next, newNode.prev)
            print("originNode >>", node.prev.data, node.data, node.next.data)
            after_node = node.next
            newNode.next = after_node
            newNode.prev = node
            print("newNode >>", newNode.prev.data, newNode.data, newNode.next.data)
            node.next = newNode
            print("originNode >>", node.prev.data, node.data, node.next.data)
            print("afterNode >>", after_node.prev.data, after_node.data, after_node.next.data)
            after_node.prev = newNode
            print("newNode >>", newNode.prev.data, newNode.data, newNode.next.data)
            print("afterNode >>", after_node.prev.data, after_node.data, after_node.next.data)


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
    # testLinkedList.searchNode("next", 4)
    # testLinkedList.searchNode("prev", 0)
    # testLinkedList.searchNode("prev", 9)
    # print("-----------")
    # testLinkedList.deleteNode(0)
    # testLinkedList.desc()
    # print("-----------")
    # testLinkedList.deleteNode(2)
    # testLinkedList.desc()
    # print("-----------")
    testLinkedList.deleteNode(8)
    testLinkedList.desc()
    testLinkedList.insert_after(3, 10)