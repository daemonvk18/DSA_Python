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
        if self.length <= index or  index <0:
            return None
        temp = self.head
        count = 0
        while count != index:
            temp = temp.next
            count += 1
        return temp
        #for _ in range(index):
        #   temp = temp.next
        #return temp  

    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        if index <0 or index > self.length:
            return False
        newNode = Node(value)
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

    def remove_node(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value     

    def reversell(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after    
                     
        
        
my_Linked_list = LinkedList(0)
my_Linked_list.append(1)
my_Linked_list.append(2)
my_Linked_list.append(3)
