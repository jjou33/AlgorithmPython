'''6. 충돌(Collision) 해결 알고리즘 (좋은 해쉬 함수 사용하기)
해쉬 테이블의 가장 큰 문제는 충돌(Collision)의 경우입니다. 이 문제를 충돌(Collision) 또는 해쉬 충돌(Hash Collision)이라고 부릅니다.

6.1. Chaining 기법
개방 해슁 또는 Open Hashing 기법 중 하나: 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
충돌이 일어나면, 링크드 리스트라는 자료 구조를 사용해서, 링크드 리스트로 데이터를 추가로 뒤에 연결시켜서 저장하는 기법'''

## Chaining 기법 구현

## 'Andy' : 11 , 'Anthor' : 21
## 해쉬 테이블에 11 과 함께 해당 Hash 값을 같이 저장한다.

class Hash:
    def __init__(self, size):
        self.hash_table = list([0 for i in range(size)])
        self.size = size

    def get_key(self,data):
        return hash(data)

    def hash_function(self, key):
        return key % self.size

    def save_data(self,data,value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        if self.hash_table[hash_address] != 0:
            for index in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][index][0] == index_key:
                    self.hash_table[hash_address][index][1] = value
                    return
            self.hash_table[hash_address].append([index_key, value])
        else:
            self.hash_table[hash_address] = [[index_key, value]]

    def read_data(self,data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        if self.hash_table[hash_address] != 0:
            for index in range(len(self.hash_table[hash_address])):
                if self.hash_table[hash_address][index][0] == index_key:
                    return self.hash_table[hash_address][index][1]
            return None
        else:
            return None

if __name__ == '__main__':

    hash_table = Hash(8)
    hash_table.save_data('Dd', '0102030203')
    hash_table.save_data('Date', '0102030203')
    print(hash_table.read_data('Dd'))


