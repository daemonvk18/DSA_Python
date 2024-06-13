class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1


    def print_queue(self)->None:
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next    


my_queue = Queue(11) 
my_queue.print_queue()               