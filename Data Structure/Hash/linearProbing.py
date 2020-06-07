'''6.2. Linear Probing 기법
폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
충돌이 일어나면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈공간에 저장하는 기법
저장공간 활용도를 높이기 위한 기법
연습3: 연습1의 해쉬 테이블 코드에 Linear Probling 기법으로 충돌해결 코드를 추가해보기
1. 해쉬 함수: key % 8
2. 해쉬 키 생성: hash(data)'''

class linearProbingHash:
    def __init__(self,size):
        self.hash_table = list([0 for i in range(size)])
        self.size = size

    def get_key(self,data):
        return hash(data)

    def hash_function(self,key):
        return key % self.size

    def save_data(self,data,value):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        if self.hash_table[hash_address] != 0:
            for index in range(hash_address, len(self.hash_table)):
                if self.hash_table[index] == 0:
                    self.hash_table[hash_address] = [index_key, value]
                    return
                elif self.hash_table[index][0] == index_key:
                    self.hash_table[hash_address][1] = value
                    return
                # else:
                #     self.size += 1
                #     self.hash_table[self.size].append([index_key, value])
                #     return
        else:
            self.hash_table[hash_address] = [index_key, value]

    def read_data(self,data):
        index_key = self.get_key(data)
        hash_address = self.hash_function(index_key)
        if self.hash_table[hash_address] != 0:
            for index in range(hash_address, len(self.hash_table)):
                if self.hash_table[index] == 0:
                    return None
                elif self.hash_table[index][0] == index_key:
                    return self.hash_table[index][1]
        else:
            return None


if __name__ == '__main__':
    hash_table = linearProbingHash(8)
    print(hash('dk') % 8)
    print(hash('da') % 8)
    print(hash('dc') % 8)
    hash_table.save_data('dk', '01200123123')
    hash_table.save_data('da', '3333333333')
    print(hash_table.read_data('dk'))