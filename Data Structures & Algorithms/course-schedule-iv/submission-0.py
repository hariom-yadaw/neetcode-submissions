class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        inDegree = {i : 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}
        isPrereq = [set() for i in range(numCourses)]

        for parent, child in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            vertex = sources.popleft()

            for child in graph[vertex]:
                isPrereq[child].add(vertex)
                isPrereq[child].update(isPrereq[vertex])

                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return [u in isPrereq[v] for u, v in queries]