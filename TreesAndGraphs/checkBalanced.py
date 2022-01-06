class Node:
    def __init__(self, value, left=None, right=None):
        self.val=value
        self.right=right
        self.left=left

def getHeight(root):
    if not root:
        return -1
    return max(getHeight(root.left), getHeight(root.right))+1

def checkBalanced(root):
    if not root:
        return True
    diffH=getHeight(root.left)-getHeight(root.right)
    if abs(diffH)>1:
        return False
    else:
        return checkBalanced(root.left) and checkBalanced(root.right)



if __name__=='__main__':
    A = Node(8)
    B = Node(7, right=A)
    C = Node(5)
    D = Node(2, left=B, right=C)
    E = Node(3)
    F = Node(5)
    G = Node(6, left=E, right=F)
    root = Node(3, left=D, right=G)
    print(checkBalanced(root))
