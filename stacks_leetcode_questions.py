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
        
    def peek_element(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]  
        

    def reverse_string(self,s)->str:
        stack = Stack()
        reversed_string = ""
        for char in s:
            stack.push_element(char)

        while not stack.is_empty():
            reversed_string += stack.pop_element()
        return reversed_string


    def sort_stack(self,old_stack):
        new_stack = Stack()
        while not old_stack.is_empty():
            temp = old_stack.pop_element()
            while not new_stack.is_empty() and new_stack.peek_element()>temp:
                old_stack.push_element(new_stack.pop_element())

            new_stack.push_element(temp)
        return new_stack                       




        
            


my_stack = Stack()
my_stack.push_element(5)
my_stack.push_element(1)
my_stack.push_element(3)
my_stack.push_element(2)
my_stack.push_element(6)
new_stack = my_stack.sort_stack(my_stack)
new_stack.print_stack()
