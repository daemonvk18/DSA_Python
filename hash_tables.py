class HashTable:
    def __init__(self,size:int= 7):
        self.data_map = [None]*size


    def _hash(self,key):
        my_hash = 0
        for letters in key:
            my_hash = (my_hash + ord(letters)*23)%len(self.data_map)
        return my_hash

    def print_hashtable(self):
        for i,val in enumerate(self.data_map):
            print(i,":",val)

    def set_item(self,key,value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in self.data_map[index]:
                if i[0] == key:
                    return i[1]
        return None


    def get_keys(self):
        all_keys  = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys                           



my_hash_table = HashTable()
my_hash_table.set_item("bolts",1400)
my_hash_table.set_item("washers",50)
my_hash_table.set_item("lumber",1000)
print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("preetham")) 
print(my_hash_table.get_keys())                  