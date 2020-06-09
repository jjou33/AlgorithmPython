'''
3. 이진 트리와 이진 탐색 트리 (Binary Search Tree)
    이진 트리: 노드의 최대 Branch가 2인 트리
    이진 탐색 트리 (Binary Search Tree, BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
        왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음!

4. 자료 구조 이진 탐색 트리의 장점과 주요 용도
    주요 용도: 데이터 검색(탐색)
    장점: 탐색 속도를 개선할 수 있음
    단점: 이진 탐색 트리 알고리즘 이해 후에 살펴보기로 함

5.4. 이진 탐색 트리 삭제
    매우 복잡함. 경우를 나누어서 이해하는 것이 좋음

5.4.1. Leaf Node 삭제
    Leaf Node: Child Node 가 없는 Node
    삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다

5.4.2. Child Node 가 하나인 Node 삭제
    삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.

5.4.3. Child Node 가 두 개인 Node 삭제
    - 삭제할 Node의 오른쪽 자식 중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키도록 한다.
    - 삭제할 Node의 왼쪽 자식 중, 가장 큰 값을 삭제할 Node의 Parent Node가 가리키도록 한다.

5.4.3.1. 삭제할 Node의 오른쪽 자식중, 가장 작은 값을 삭제할 Node의 Parent Node가 가리키게 할 경우
    - 삭제할 Node의 오른쪽 자식 선택
    - 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
    - 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가리키게 함
    - 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가리키게 함
    - 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가리키게 함
    - 만약 해당 Node가 오른쪽 Child Node를 가지고 있었을 경우에는, 해당 Node의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가리키게 함
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
    # 삽입
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
    # 검색
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

# 5.5. 이진 탐색 트리 삭제 코드 구현과 분석
#     5.5.1 삭제할 Node 탐색
#         삭제할 Node가 없는 경우도 처리해야 함
#         이를 위해 삭제할 Node가 없는 경우는 False를 리턴하고, 함수를 종료 시킴

    def delete(self,value):
        searchCkc = False
        self.current_node = self.head
        self.parent = self.head

        while self.current_node:
            if self.current_node == value:
                searchCkc = True
                break
            elif self.current_node > value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        # 해당 값을 찾지 못하였을 경우
        if not searchCkc:
            return False

# 5.5.2. Case1: 삭제할 Node가 Leaf Node인 경우
    # self.current_node 가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        elif self.current_node.left is None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
# 5.5.2. Case2: 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        elif self.current_node.left is not None and self.current_node.right is None:
            if self.parent.value > value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
            del self.current_node
        elif self.current_node.left is None and self.current_node.right is not None:
            if self.parent.value > value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
if __name__ == '__main__':
    head = Node(1)
    BST = NodeMgnt(head)
    BST.insert(2)
    print(BST.search(3))