class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubelyLinkedList:
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length =  1

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  

    def append(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value


    def prepend(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            self.head.prev = None
        self.length -= 1
        return temp


    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp = temp.prev
        return temp.value


    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert(self,index,value):
        if index <0 or index>self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        prev = self.get(index-1)
        temp = prev.next

        newNode.prev = prev
        newNode.next = temp
        prev.next = newNode
        temp.prev = newNode

        self.length += 1
        return True
    

    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp



my_doubley_linkedlist = DoubelyLinkedList(11)
my_doubley_linkedlist.append(3)
my_doubley_linkedlist.append(23)
my_doubley_linkedlist.append(7)
my_doubley_linkedlist.append(4)
print(my_doubley_linkedlist.get(2))
my_doubley_linkedlist.printList()              