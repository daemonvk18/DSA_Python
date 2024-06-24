class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i]) 

    def is_empty(self):
        return len(self.stack_list)  == 0       

    def push_element(self,value):
        self.stack_list.append(value)
        return True

    def pop_element(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
            


my_stack = Stack()
my_stack.push_element(11)
my_stack.push_element(13)
my_stack.push_element(2)
my_stack.push_element(6)
my_stack.print_stack()
poped_element = my_stack.pop_element()
print(poped_element)        