# STACK 
# Stack is a simple data structure that adds and removes elements in a particular order 
# every time an item is added it goes on top of the stack and only the item at the top of the stack can be removed
# this behaviour is called a LOFI behaviour -> Last In First Out 

#lets implement it a stack 
class Stack :
    def __init__(self):
        self.stack = []
    #adding to a stack 
    def push(self , new_item):
        self.stack.insert(0 , new_item)
    #deleting from a stack 
    def pop(self):
        return self.stack.pop(0)
        
    #checking if our stack is empty 
    def is_empty(self):
        return self.stack == []
    #printing out the content of our stack 
    def print_stack(self):
        print(self.stack)


#testing the stack 
#create an instance of the stack 
stack = Stack()
#adding items to the stack 
stack.push("Data structure")
stack.push("Simple")
#check the content of our stack 
stack.print_stack()

#now lets empty it 
while True:
    item = stack.pop()
    print(f"removed {item}")
    if stack.is_empty():
        break
    
#finaly print the contents of the stack 
stack.print_stack()


