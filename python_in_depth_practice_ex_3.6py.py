class Stack:

    Max_Size = 10

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        if self.size == Stack.Max_Size:
            raise RuntimeError('Stack is full')
        self.items.append(item)
      
    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        if self.is_empty():
            raise RuntimeError('Stack is empty')
        return self.items.pop()

    def display(self):
        print(self.items)
           

        
