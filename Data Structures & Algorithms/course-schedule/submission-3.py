from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return True
        
        # Initialize graph
        inDegree = {i : 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}

        # build graph
        for child, parent in prerequisites:
            inDegree[child] += 1
            graph[parent].append(child)
        
        # Find Sources
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # BFS with sources
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return len(sortedOrder) == numCourses

