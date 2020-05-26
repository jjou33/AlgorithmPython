class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class NodeMgnt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    def delete(self,data):
        if self.head == '':
            print("데이터 없음")
            return
        else:
            if self.head.data == data:
                temp = self.head
                self.head = self.head.next
                del temp
            else:
                node = self.head
                while node.next:
                    if node.next.data == data:
                        temp = node.next
                        node.next = node.next.next
                        del temp
                        return
                    else:
                        node = node.next


if __name__ == '__main__':
    link = NodeMgnt(0)
    link.desc()
    for i in range(1,10):
        link.add(i)
    link.desc()
    link.delete(3)
    link.desc()
    link.delete(9)
    link.desc()