'''6.3. 빈번한 충돌을 개선하는 기법
해쉬 함수을 재정의 및 해쉬 테이블 저장공간을 확대
    예: hash_table = list([None for i in range(16)])
        def hash_function(key):
            return key % 16
참고: 해쉬 함수와 키 생성 함수
파이썬의 hash() 함수는 실행할 때마다, 값이 달라질 수 있음
유명한 해쉬 함수들이 있음: SHA(Secure Hash Algorithm, 안전한 해시 알고리즘)
어떤 데이터도 유일한 고정된 크기의 고정값을 리턴해주므로, 해쉬 함수로 유용하게 활용 가능

7. 시간 복잡도
일반적인 경우(Collision이 없는 경우)는 O(1)
최악의 경우(Collision이 모두 발생하는 경우)는 O(n)
해쉬 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에, 시간 복잡도는 O(1) 이라고 말할 수 있음

검색에서 해쉬 테이블의 사용 예
16개의 배열에 데이터를 저장하고, 검색할 때 O(n)
16개의 데이터 저장공간을 가진 위의 해쉬 테이블에 데이터를 저장하고, 검색할 때 O(1)'''

import hashlib

def sha_1():
    ## String 을 Byte 로 변환
    data = 'test'.encode()
    hash_object = hashlib.sha1()
    hash_object.update(data)

    hex_dig = hash_object.hexdigest()
    print(hex_dig)

def sha_256():
    ## 고정된 길이의 일관된 데이터로 리턴해줌
    ## 블록체인에서 함수 사용하며, 결과값으로 원 데이터를 추론 불가능
    ## String 을 Byte 로 변환
    data = 'test'.encode()
    hash_object = hashlib.sha256()
    hash_object.update(data)

    hex_dig = hash_object.hexdigest()
    print(hex_dig)

## Chaining 기법에서 Key 를 sha256 hash Function을 사용하여 Key 값 추출
class Hash:
    def __init__(self, size):
        self.hash_table = list([0 for i in range(size)])
        self.size = size

    def get_key(self,data):
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_dig = hash_object.hexdigest()
        ## 추출된 hashCode를 16진수로 변환하여 Return
        print("-----------------------------------")
        print ("data >>", data)
        print ("hex_dig >>", hex_dig)
        return int(hex_dig, 16)

    def hash_function(self, key):
        print ("Origin key >>", key)
        print ("New Key >>", key%self.size)
        print ("-----------------------------------")
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
    sha_1()
    sha_256()
    hash_table = Hash(8)
    hash_table.save_data('Dd', '0102030203')
    hash_table.save_data('Date', '0102030204')
    print(hash_table.read_data('Dd'))

