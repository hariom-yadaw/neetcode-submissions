class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            adjList[a].append((b, values[i]))
            adjList[b].append((a, 1 / values[i]))
        
        def bfs(src, target):
            if src not in adjList or target not in adjList:
                return -1
            
            queue = deque()
            visited = set()

            queue.append((src, 1)) # source with weight = 1
            visited.add(src)

            while queue:
                node, pathWeight = queue.popleft()
                if node == target:
                    return pathWeight
                
                for neighbor, weight in adjList[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, pathWeight * weight))
                        visited.add(neighbor)

            return - 1 # if path from src to target not found (or not connected) 

        result = []
        for q in queries:
            result.append(bfs(q[0], q[1]))
        return result
