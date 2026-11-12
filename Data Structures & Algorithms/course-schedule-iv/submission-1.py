class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        inDegree = {i : 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}
        preReqForV = [set() for i in range(numCourses)] # isPrereq[v] = (u1, u2, u3, ...)

        # 'parent' is prereq for course 'child'
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
                # child is course, vertex is prereq
                # For Course 'child', add current prereq 'vertex', also add all prereqs for vertex
                    # - at the start preReqforV[vertex] will be empty [] because these have '0' in-degrees 
                preReqForV[child].add(vertex)
                preReqForV[child].update(preReqForV[vertex])

                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        return [u in preReqForV[v] for u, v in queries]