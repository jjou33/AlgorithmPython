class Hash:
    def __init__(self, size):
        self.hash_table = list([0 for i in range(size)])

    def get_key(self,data):
        return hash(data)

    def hash_function(self,key):
        return key % 8

    def save_data(self,data,value):
        hash_address = self.hash_function(self.get_key(data))
        self.hash_table[hash_address] = value

    def read_data(self,data):
        hash_address = self.hash_function(self.get_key(data))
        return self.hash_table[hash_address]

if __name__ == '__main__':

    hash_table = Hash(8)
    hash_table.save_data('Dave', '0102030200')
    hash_table.save_data('Andy', '0102030201')
    hash_table.save_data('Richard', '0102030202')
    print (hash_table)
    print(hash_table.read_data('Dave'))
