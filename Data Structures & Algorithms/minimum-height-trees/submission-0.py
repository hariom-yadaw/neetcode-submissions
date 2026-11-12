class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Rules for Root of a MHT
            # 1. Root should be on longest path, not off the path
            # 2. Root should be in middle of longest path
        # Problem simplifies to find the middle nodes of longest path
        # We can simply prune the leaf nodes layer by layer

        if n <= 0:
            return []
        if n == 1:
            return [0] # node 0
        
        # A. Initialize graph
        inDegree = {i : 0 for i in range(n)}
        graph = {i : [] for i in range(n)}

        # B. Build the graph
        for edge in edges:
            n1, n2 = edge[0], edge [1]

            # Since this is undirected graph, but topological sort gets applied on directed graph
                # - but mechanisam is same. Here instead of dependecy/prerequisites we have
                # - double sided connection.
                # Leaf nodes will have atleast one in-degree, no 0 in-degree 
            inDegree[n1] += 1
            inDegree[n2] += 1
            # hence link for both nodes
            graph[n1].append(n2)
            graph[n2].append(n1)

        # C. find the sources
        leafQueue = collections.deque()
        for key in inDegree:
            if inDegree[key] == 1:
                leafQueue.append(key)
        
        # D.  Remove leaf nodes kevel by level and subtract each leaf's children's in-degrees
            # - repeat this untill we are left with 1 or 2 nodes, which will be middle nodes
        totalNodes = n
        while totalNodes > 2 and leafQueue:
            leafQueueSize = len(leafQueue) # these leaf nodes will be pruned

            for _ in range(leafQueueSize):
                vertex = leafQueue.popleft()

                for child in graph[vertex]:
                    inDegree[child] -=1 
                    if inDegree[child] == 1:
                        leafQueue.append(child)
            
            totalNodes -= leafQueueSize
        
        #return the remaining leafs in queue which will be root for MHT 
        return list(leafQueue)

        