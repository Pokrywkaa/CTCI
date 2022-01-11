class Node:
    def __init__(self, x, left=None, right=None, parent=None):
        self.left=left
        self.right=right
        self.parent=parent
        self.x=x

def Successor(node):
    if not node:
        return False
    if node.right:
        node=node.right
        while node.left:
            node=node.left
        return node.x
    else:
        while node.parent and node.parent.right==node:
            node=node.parent
        return node.parent.x

if __name__ == '__main__':
    B=Node(1)
    C=Node(3)
    A=Node(2,B,C)
    B.parent=A
    C.parent=C
    print(Successor(C))


    
