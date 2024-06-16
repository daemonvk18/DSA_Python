class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySeachTree:
    def __init__(self):
         self.root = None


    def insert(self,value)->bool:
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return True
        temp = self.root
        while (True):
            if temp.value == newNode.value:
                return False
            if temp.value > newNode.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right


    def contains(self,value)->bool:
        temp = self.root
        while temp is not None:
            if temp.value == value:return True
            elif temp.value>value:
                temp = temp.left
            else:
                temp = temp.right
        return False            

          


my_binary_search_tree = BinarySeachTree()
my_binary_search_tree.insert(47)
my_binary_search_tree.insert(21)
my_binary_search_tree.insert(18)
my_binary_search_tree.insert(27)
my_binary_search_tree.insert(52)
my_binary_search_tree.insert(84)
print(my_binary_search_tree.contains(90))
              