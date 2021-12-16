class Stack:
    def __init__(self):
        self.array=[]

    def append(self,value):
        if len(self.array)==0:
            self.array.append((value, value))
            self.actual_min=value
        else:
            if value<self.actual_min:
                self.actual_min=value
            self.array.append((value, self.actual_min))

    def pop(self):
        self.array.pop()
        return self.array[-1][1]



s=Stack()
s.append(10)
s.append(5)
s.append(20)
s.append(4)
s.append(10)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
