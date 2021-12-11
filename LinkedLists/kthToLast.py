class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.headval=None

def kToLast(linked_list, k):
    iter=linked_list.headval
    for i in range(k):
        iter=iter.next
    while iter is not None:
        print(iter.value)
        iter=iter.next
    return linked_list

nodes=[Node(0), Node(1), Node(2), Node(1), Node(0)]

L=LinkedList()

L.headval=nodes[0]
for i in range(len(nodes)-1):
    nodes[i].next=nodes[i+1]
L=kToLast(L, 3)