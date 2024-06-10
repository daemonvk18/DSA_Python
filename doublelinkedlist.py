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


my_doubley_linkedlist = DoubelyLinkedList(11)
my_doubley_linkedlist.append(3)
my_doubley_linkedlist.printList()                