class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def minimalTree(sortedList):
    if not sortedList:
        return None

    mid=len(sortedList)//2
    root=Node(sortedList[mid])
    root.left=minimalTree(sortedList[:mid])
    root.right=minimalTree(sortedList[mid+1:])
    return root



x=minimalTree([1,2,3,4,5,6,7])
print(x.left.right.value)
"""
            3
           /  \
          2     6
        /  \   / \
       1    3  5  7
"""
