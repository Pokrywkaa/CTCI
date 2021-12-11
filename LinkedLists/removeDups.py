class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class linkedList:
    def __init__(self):
        self.headval=None
    
    def printNodes(self):
        printval=self.headval
        while printval is not None:
            print(printval.value)
            printval=printval.next

def removeDups(linked_list):
    hash={linked_list.headval.value: True}
    iter=linked_list.headval
    while iter.next is not None:
        item=hash.get(iter.next.value)
        if item:
            iter.next=iter.next.next
        else:
            hash[iter.next.value]=True
            iter=iter.next
    return linked_list



nodes=[Node(0), Node(1), Node(2), Node(1), Node(0)]

L=linkedList()

L.headval=nodes[0]
for i in range(len(nodes)-1):
    nodes[i].next=nodes[i+1]

L = removeDups(L)

L.printNodes()


