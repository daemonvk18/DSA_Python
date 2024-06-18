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



my_hash_table = HashTable()
my_hash_table.set_item("bolts",1400)
my_hash_table.set_item("washers",50)
my_hash_table.set_item("lumber",1000)
my_hash_table.print_hashtable()                    