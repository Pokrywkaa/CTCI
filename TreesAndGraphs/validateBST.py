class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def copyTree(root, arr):
    if not root:
        return
    copyTree(root.left, arr)
    arr.append(root.val)
    copyTree(root.right, arr)
    return arr

def validateBST(root):
    arr=[]
    checkList=copyTree(root, arr)
    sortedCheckList=sorted(checkList)
    for i in range(len(checkList)):
        if checkList[i]!=sortedCheckList[i]:
            return False
    return True

#better solution
last_printed=None
def checkBST(root):
    global last_printed
    if not root:
        return True
    if not checkBST(root.left):
        return False
    if last_printed is not None and root.val>last_printed:
        return False
    last_printed=root.val
    if not checkBST(root.right):
        return False
    return True


if __name__=='__main__':
    A = Node(8)
    B = Node(7, right=A)
    C = Node(5)
    D = Node(2, left=B, right=C)
    E = Node(3)
    F = Node(5)
    G = Node(6, left=E, right=F)
    root1 = Node(3, left=D, right=G)
    print(validateBST(root1))
    print(checkBST(root1))


    O = Node(7)
    A = Node(4)
    B = Node(1)
    C = Node(6, left=A, right=O)
    D = Node(3, left=B, right=C)
    F = Node(13)
    E = Node(14, left=F)
    G = Node(10, right=E)
    root2 = Node(8, left=D, right=G)
    print(validateBST(root2))
