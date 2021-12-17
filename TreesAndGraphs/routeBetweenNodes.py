class Node:
    def __init__(self, value):
        self.value=value
        self.adj=[]
        self.visited=False
    
class Graph:
    def __init__(self, vertices):
        self.v=vertices

    def BFS(self, firstNode, secondNode):
        if firstNode==secondNode:
            return True
        
        for i in self.v:
            i.visited=False
            
        firstNode.visited=True
        queue=[firstNode]
        while queue:
            item=queue.pop()
            for i in item.adj:
                if not i.visited:
                    if i==secondNode:
                        return True
                    else:
                        i.visited=True
                        queue.insert(0, i)
                            
        return False


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
A.adj = [E]
B.adj = [A,C,D]
D.adj = [B]
E.adj = [C]
graph = Graph([A,B,C,D,E])

print(graph.BFS(D,E))
print(graph.BFS(A,C))