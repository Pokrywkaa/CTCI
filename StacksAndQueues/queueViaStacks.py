class Stack:
    def __init__(self):
        self.stack=[]
    
    def append(self, value):
        self.stack.append(value)

    def pop(self):
        x=self.stack.pop()
        return x

    def getLen(self):
        return len(self.stack)

class QueueViaStacks:
    def __init__(self):
        self.newElements=Stack()
        self.oldElements=Stack()

    def append(self, x):
        self.newElements.append(x)

    def pop(self):
        if self.oldElements.getLen()==0:
            while self.newElements.getLen():
                self.oldElements.append(self.newElements.pop())
        x=self.oldElements.pop()
        return x


Q=QueueViaStacks()
Q.append(10)
Q.append(2)
Q.append(6)

print(Q.pop())
print(Q.pop())

Q.append(12)

print(Q.pop())

Q.append(11)

print(Q.pop())
