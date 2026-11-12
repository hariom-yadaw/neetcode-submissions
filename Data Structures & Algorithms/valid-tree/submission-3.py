from collections import defaultdict
class Solution:
    def __init__(self):
        self.Graph = defaultdict(list)
        self.visited = set()
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #self.Graph = defaultdict(list)
        #self.visited = set()

        for u, v in edges:
            self.Graph[u].append(v)
            self.Graph[v].append(u)
        
        if self.hasCycle_DFS(0, -1):
            return False
        
        return len(self.visited) == n
        
    def hasCycle_DFS(self, node, parent):
        #if node in self.visited:
        #    return True
        self.visited.add(node)

        for neighbor in self.Graph[node]:
            if neighbor == parent:
                continue
            if neighbor in self.visited or self.hasCycle_DFS(neighbor, node):
                return True

        return False 

        
