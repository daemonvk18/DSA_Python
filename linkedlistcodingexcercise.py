class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail  = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1 

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
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


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self,index):
        if index<0 or index>= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
    

    def set_value(self,index,value):
        if index <0 or index>= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True


    def insert(self,index,value):
        if index<0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True 

    def removeNode(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev  = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp   
                            

                       
my_linked_list = LinkedList(4)
print(my_linked_list.head)
print(my_linked_list.tail)
print(my_linked_list.length)
my_linked_list.print_list()
my_linked_list.append(11) 
my_linked_list.print_list()
print(my_linked_list.pop())       