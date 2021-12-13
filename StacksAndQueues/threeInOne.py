class threeStack:
    def __init__(self):
        self.t1=0
        self.t2=0
        self.t3=0
        self.array=[]

    def append(self, numberOfStack, value):
        if numberOfStack==1:
            self.array.insert(self.t1, value)
            self.t1+=1
            self.t2+=1
            self.t3+=1
        if numberOfStack==2:
            self.array.insert(self.t2, value)
            self.t2+=1
            self.t3+=1
        if numberOfStack==3:
            self.array.insert(self.t3, value)
            self.t3+=1

    def pop(self, numberOfStack):
        if numberOfStack==1:
            removedItem=self.array.pop(self.t1-1)
            self.t1-=1
            self.t2-=1
            self.t3-=1
        elif numberOfStack==2:
            removedItem=self.array.pop(self.t2-1)
            self.t2-=1
            self.t3-=1
        elif numberOfStack==3:
            removedItem=self.array.pop(self.t3-1)
            self.t3-=1
        return removedItem

if '__main__' == __name__:
    stack = threeStack()
    stack.append(1,3)
    stack.append(3,5)
    stack.append(1,10)
    stack.append(1,12)
    stack.append(2,15)
    stack.append(3,7)
    print(stack.pop(1))
    print(stack.pop(1))
    print(stack.pop(2))
