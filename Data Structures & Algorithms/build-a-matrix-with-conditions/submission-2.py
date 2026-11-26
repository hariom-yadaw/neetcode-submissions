from collections import deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges):
            inDegree = [0] * (k + 1) # 1 to k
            graph = [[] for _ in range(k + 1)]
            for parent, child in edges:
                graph[parent].append(child)
                inDegree[child] += 1
            
            sources = deque()
            for key in range(1, k + 1):
                if inDegree[key] == 0:
                    sources.append(key)
            
            sortedOrder = []
            while sources:
                node = sources.popleft()
                sortedOrder.append(node)

                for child in graph[node]:
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        sources.append(child)
            
            if len(sortedOrder) != k:
                return []
            return sortedOrder
        

        rowOrder = topo_sort(rowConditions)
        if not rowOrder: 
            return []

        colOrder = topo_sort(colConditions)
        if not colOrder: 
            return []

        val_to_row = {num : i for i, num in enumerate(rowOrder)}
        val_to_col = {num : i for i, num in enumerate(colOrder)}

        result = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            result[r][c] = num
        
        return result
