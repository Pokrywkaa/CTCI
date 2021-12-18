class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList():
    def __init__(self, node=None):
        if not node:
            self.headval=None
        else:
            self.headval=Node(node)
    
    def addAtBeginning(self, node):
        if not node:
            return
        newNode=Node(node)
        newNode.next=self.headval
        self.headval=newNode

    def __iter__(self):
        if not self.headval:
            return True
        iter=self.headval
        while iter:
            yield iter.value
            iter=iter.next


class BinaryTree:
    def __init__(self, root):
        self.root=root

def listOfDepths(tree):
    linkedLists=[]
    D=LinkedList(tree.root)
    while D.headval:
        linkedLists.append(D)
        nextD=LinkedList()
        for i in D:
            nextD.addAtBeginning(i.left)
            nextD.addAtBeginning(i.right)
        for i in D:
            print(i.value)
        D=nextD
        print('\n')
    return linkedLists

A = TreeNode(8)
B = TreeNode(7, right=A)
C = TreeNode(5)
D = TreeNode(2, left=B, right=C)
E = TreeNode(3)
F = TreeNode(5)
G = TreeNode(6, left=E, right=F)
root = TreeNode(3, left=D, right=G)
tree = BinaryTree(root)

linkedLists=listOfDepths(tree)