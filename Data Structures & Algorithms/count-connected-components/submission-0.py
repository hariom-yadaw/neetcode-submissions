from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        visited = set()
        countConnectedComp = 0

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):
            visited.add(node)
            
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                countConnectedComp += 1

        return countConnectedComp    
