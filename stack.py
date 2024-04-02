class Stack:
    def __init__(self, max_size):
        self.size = size
        self.stack = []
        
    def push(self, element):
        if len(self.stack) < self.size:
            self.stack.append(element)
            print(f"{element} pushed to stack")
        else:
            print("Stack overflow")
            
    def pop(self):
        if self.isempty():
            print("-2147483648 popped from stack")
        else:
            popped_element = self.stack.pop()
            print(f"{popped_element} popped from stack")
            
            
    def display(self):
        if self.isempty():
            print("-2147483648")
        else:
            print(self.stack[-1])
            
    def isempty(self):
        return len(self.stack) == 0
        
    def isfull(self):
        return len(self.stack) == self.size
        
    def count_elements(self):
        print(len(self.stack))
        
    def display_stack(self):
        if self.isempty():
            print("This stack is empty")
        else:
            print(" ".join(map(str, self.stack)))
            
if __name__ == "__main__":
    size = 5
    
    stack = Stack(size)
    
    while True:
        choice = int(input())
        
        if choice == 1:
            element = int(input())
            stack.push(element)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            if stack.isempty():
                print("1")
            else:
                print("0")
        elif choice == 5:
            if stack.isfull():
                print("1")
            else:
                print("0")
        elif choice == 6:
            stack.count_elements()
        elif choice == 7:
            stack.display_stack()
        elif choice == 8:
            break
        else:
            print("Enter valid choice")
