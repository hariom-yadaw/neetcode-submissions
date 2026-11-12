from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses <= 0:
            return True

        inDegree = {i : 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}

        for child, parent in prerequisites:
            inDegree[child] += 1
            graph[parent].append(child) 
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)

            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != numCourses:
            return []
        return sortedOrder