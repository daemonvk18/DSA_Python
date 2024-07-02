class Node:
    def __init__(self,value)->None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self)->None:
        self.root = None

    # def insert(self,value):
    #     newNode = Node(value)
    #     if self.root is None:
    #         self.root = newNode
    #         return True
    #     temp = self.root
    #     while True:
    #         if temp.value == value:return False
    #         if temp.value >value:
    #             if temp.left == None:
    #                 temp.left = newNode
    #                 return True
    #             else:
    #                 temp = temp.left
    #         else:
    #             if temp.right == None:
    #                 temp.right = newNode
    #                 return True
    #             else:
    #                 temp = temp.right


    def __r_contains(self,current_Node,value)->bool:
        if current_Node == None:
            return False
        if current_Node.value == value:
            return True
        if value < current_Node.value:
            return self.__r_contains(current_Node.left,value)
        if value > current_Node.value:
            return self.__r_contains(current_Node.right,value)



    def r_contains(self,value)->bool:
        return self.__r_contains(self.root,value)
    

    def __r_insert(self,current_Node,value)->bool:
        if current_Node == None:
            return Node(value)
        if value < current_Node.value:
            current_Node.left = self.__r_insert(current_Node.left,value)
        if value > current_Node.value:
            current_Node.right = self.__r_insert(current_Node.right,value)
        return current_Node        


    def r_insert(self,value)->bool:
        if self.root == None:
            self.root = None(value)
        self.__r_insert(self.root,value)


    def __r_delete(self,current_Node,value):
        if current_Node == None:
            return None
        if value < current_Node.value:
            current_Node.left = self.__r_delete(current_Node.left,value)
        elif value > current_Node.value:
            current_Node.right = self.__r_delete(current_Node.right,value)
        else:
            #here comes the diffferent scenarios to delete a node(leafnode,node containing left,containing right,both)
            print("delete")
        return current_Node             



    def r_delete(self,value):
        self.root = self.__r_delete(self.root,value)                         



my_bst = BinarySearchTree()
print(my_bst.insert(47))
print(my_bst.insert(21))
print(my_bst.insert(76)) 
print(my_bst.insert(18)) 
print(my_bst.insert(27))
print(my_bst.insert(62))
print(my_bst.insert(82))
print(my_bst.r_contains(17))                                      
