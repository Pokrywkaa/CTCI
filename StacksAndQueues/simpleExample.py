class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items == []

    def pushItem(self, data):
        self.items.append(data)
    
    def removeItem(self):
        return self.items.pop()

s=Stack()

while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'push':
        s.pushItem(int(do[1]))
    elif operation == 'pop':
        if s.isEmpty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.removeItem())
    elif operation == 'quit':
        break