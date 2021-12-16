class Stack:
    def __init__(self):
        self.arrayStack=[]
        self.size=0

    def append(self, value):
        self.arrayStack.append(value)
        self.size+=1

    def pop(self):
        x=self.arrayStack.pop()
        self.size-=1
        return x

class StackOfPlates:
    def __init__(self, treshold):
        self.stacks=[]
        self.treshold=treshold
        self.iter=0

    def append(self, value):
        if len(self.stacks)==0 or self.stacks[self.iter-1].size==self.treshold:
            self.stacks.append(Stack())
            self.iter+=1
        self.stacks[self.iter-1].append(value)

    def pop(self):
        x=self.stacks[self.iter-1].pop()
        if self.stacks[self.iter-1].size==0:
            del self.stacks[self.iter-1]
            self.iter-=1
        return x

    def popAt(self, indexStack):
        x=self.stacks[indexStack].pop()
        if self.stacks[indexStack].size==0:
            del self.stacks[indexStack]
            self.iter-=1
        return x



stacks=StackOfPlates(2)
stacks.append(10)
stacks.append(5)
stacks.append(12)
stacks.append(22)
stacks.append(33)

print(stacks.popAt(0))

print(stacks.pop())
print(stacks.pop())
print(stacks.pop())
