class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.headval=None

    def get_values(self):
        iter=self.headval
        count=0
        while iter:
            count+=1
            if iter.next is None:
                break
            iter=iter.next
        return count, iter

    def partition(self, x):
        values=self.get_values()
        lengthList=values[0]
        lastElement=values[1]
        current=self.headval
        prev=None

        for i in range(lengthList-1):
            if current.value<x:
                if prev:
                    prev.next=current
                prev=current
            else:
                lastElement.next=current
                lastElement=lastElement.next
            current=current.next

        lastElement.next=None
        if prev:
            if prev is not current:
                prev.next=current
        return self.headval


nodes=[Node(0), Node(7), Node(2), Node(1), Node(0), Node(10), Node(4)]

L=LinkedList()
L.headval=nodes[0]
for i in range(len(nodes)-1):
    nodes[i].next=nodes[i+1]

L.partition(3)


iter = L.headval
while iter is not None:
    print(iter.value)
    iter=iter.next

