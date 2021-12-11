class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.headval=None

def delMidNodeInList(linked_list):
    iter=linked_list.headval
    count=0
    while iter is not None:
        count+=1
        iter=iter.next
    iter=linked_list.headval
    for i in range(count//2-1):
        iter=iter.next
    iter.next=iter.next.next
    return linked_list

def delMidNode(n):
    if not n or not n.next:
        return False
    next=n.next
    n.value=next.value
    n.value=next.next


nodes=[Node(0), Node(1), Node(2), Node(1), Node(0), Node(10), Node(4)]

L=LinkedList()
L.headval=nodes[0]
for i in range(len(nodes)-1):
    nodes[i].next=nodes[i+1]

L=delMidNodeInList(L)

iter = L.headval
while iter is not None:
    print(iter.value)
    iter=iter.next