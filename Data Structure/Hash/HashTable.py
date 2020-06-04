## Hash Table

class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(10)])

    ## 값을 나눠서 주소를 정하는 방법
    def hash_func(self,key):
        return key%5

    ## 데이터의 ASCII 코드 값을 이용하여 Address 를 만들어 저장하는 방법
    def storage_data(self,data,value):
        key = ord(data[0])
        hash_address = self.hash_func(key)
        self.hash_table[hash_address] = value
    ## 동일한 방법으로 해당 데이터를 return 받는다(파이썬의 Dictionary 와 동일한 방식)
    def get_data(self,keyData):
        key = ord(keyData[0])
        hash_address = self.hash_func(key)
        return self.hash_table[hash_address]

if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.storage_data('Andy', '01022')
    hashTable.storage_data('Bake', '01033')
    hashTable.storage_data('Dave', '01044')
    print(hashTable.get_data('Andy'))
    print(hashTable.get_data('Bake'))
