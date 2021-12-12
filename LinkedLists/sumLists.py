class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.headval=None

def sumLists(l1, l2):
    iter1=l1.headval
    iter2=l2.headval
    output=LinkedList()
    change=0
    while iter1 or iter2:
        if not iter1:
            sum=iter2.value+change
        elif not iter2:
            sum=iter1.value+change
        else:
            sum=iter1.value+iter2.value+change

        newvalue=sum%10
        change=sum//10
        newNode=Node(newvalue)
        if not output.headval:
            output.headval=newNode
            output_node=newNode
        else:
            output_node.next=Node(newvalue)
            output_node=output_node.next

        if iter1 is not None:
            iter1=iter1.next
        if iter2 is not None:
            iter2=iter2.next
    return output


nodes1=[Node(7), Node(1), Node(6)]
nodes2=[Node(5), Node(9), Node(2)]

L=LinkedList()
L.headval=nodes1[0]

S=LinkedList()
S.headval=nodes2[0]

for i in range(len(nodes1)-1):
    nodes1[i].next=nodes1[i+1]
for i in range(len(nodes2)-1):
    nodes2[i].next=nodes2[i+1]

sum=sumLists(L,S)


iter = sum.headval
while iter is not None:
    print(iter.value)
    iter=iter.next