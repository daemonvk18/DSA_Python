class Node:
    def __init__(self,value: int)->None:
        self.value = value
        self.next = None
        
     
class LinkedList:
    def __init__(self,value)->None:
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1
        
    def print_list(self)->None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
            
    def append(self,value:int)->bool:
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
            self.length = self.length+1
            return True
        
    def pop(self):
        if self.length==0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next is not None):
                pre = temp
                temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self,value)->bool:
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True
    
    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value 

    def get(self,index):
        if self.length < index and index <0:
            return None
        temp = self.head
        count = 0
        while count != index:
            temp = temp.next
            count += 1
        return temp       
                     
        
        
my_Linked_list = LinkedList(1)
# print(my_Linked_list.head.value)
# print(my_Linked_list.tail.value)
# print(my_Linked_list.length)
# my_Linked_list.print_list()
my_Linked_list.append(2)
my_Linked_list.print_list()
print(my_Linked_list.length)
my_Linked_list.pop()
#print(my_Linked_list.length)
my_Linked_list.print_list()
my_Linked_list.pop()
print(my_Linked_list.pop())
print(my_Linked_list.length)