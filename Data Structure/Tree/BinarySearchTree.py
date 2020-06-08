'''
3. 이진 트리와 이진 탐색 트리 (Binary Search Tree)
    이진 트리: 노드의 최대 Branch가 2인 트리
    이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
        왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음!

4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
    주요 용도: 데이터 검색(탐색)
    장점: 탐색 속도를 개선할 수 있음
    단점: 이진 탐색 트리 알고리즘 이해 후에 살펴보기로 함
'''
# 5.1. 노드 클래스 만들기
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 5.2. 이진 탐색 트리에 데이터 넣기
# 이진 탐색 트리 조건에 부합하게 데이터를 넣어야 함

class NodeMgnt:
    def __init__(self,head):
        self.head = head

    def insert(self,value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

if __name__ == '__main__':
    head = Node(1)
    BST = NodeMgnt(head)
    BST.insert(2)
    print(BST.search(3))