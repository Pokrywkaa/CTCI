class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.headval=None

    def printList(self):
        printval=self.headval
        while printval is not None:
            print(printval.value)
            printval=printval.next

    def atBegining(self, newdata):
        NewNode=Node(newdata)
        NewNode.next=self.headval
        self.headval=NewNode

    def atEnd(self, newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval=NewNode
            return
        last=self.headval
        while(last.next):
            last=last.next
        last.next=NewNode
    
    def inBetween(self, midNode, newdata):
        NewNode=Node(newdata)
        NewNode.next=midNode.next
        midNode.next=NewNode
    
    def removeNode(self, removeKey):
        HeadVal=self.headval
        if HeadVal is not None:
            if HeadVal.value==removeKey:
                self.headval=HeadVal.next
                HeadVal=None
                return
        while HeadVal is not None:
            if HeadVal.value==removeKey:
                break
            prev=HeadVal
            HeadVal=HeadVal.next
        if HeadVal == None:
            return
        prev.next=HeadVal.next
        HeadVal=None

list1=Linked_list()
list1.headval=Node('a')
e2=Node('b')
e3=Node('c')
e4=Node('d')
list1.headval.next=e2
e2.next=e3
e3.next=e4

list1.atBegining('beginning')
list1.atEnd('end')

list1.inBetween(e3, 'between')

list1.removeNode('d')

list1.printList()
