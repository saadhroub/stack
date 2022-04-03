class Stack:
    def __init__(self, size):
        self.array = [None] * size # initialize the stack array by None
        self.limit = size 
        self.top = -1 
 
    def push(self, element):
        if self.isFull():
            print('No space in the stack')
            return False
 
        print("Inserting {} in the stack", element)
        self.top +=1
        self.array[self.top] = element
 
    def pop(self):
        if self.isEmpty():
            print('Stack is empty')
            return False
        print(' {}from the stack', self.peek())
 
        top = self.array[self.top]
        self.top-=1
        return top
 
    def peek(self):
        if self.isEmpty():
            return False
        return self.array[self.top]
 
    def size(self):
        return self.top + 1
 
    def isEmpty(self):
        return self.size() == 0
 
    def isFull(self):
        return self.size() == self.limit
 
 
if __name__ == '__main__':
 
    stack = Stack(3)
 
    stack.push(1)       # Inserting 1 in the stack
    stack.push(2)       # Inserting 2 in the stack
 
    stack.pop()         # removing the top element (2)
    stack.pop()         # removing the top element (1)
 
    stack.push(3)       # Inserting 3 in the stack
 
    print('Top element is', stack.peek())
    print('The stack size is', stack.size())
 
    stack.pop()         # removing the top element (3)
 
    # check if the stack is empty
    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')