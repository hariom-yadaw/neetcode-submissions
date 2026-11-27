class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False

        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX

        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]

        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # Step1: add index of edge into list of edges
        for i, e in enumerate(edges):
            e.append(i) # [v1, v2, weight, original_index]
        
        # Step2: Sort the Edges
        edges.sort(key=lambda e: e[2]) # sorting needed for krushkal's algorithm

        #Step 3: Find the MST weight by using Unionfind (Krushkal's Algo)
        uf = UnionFind(n)
        std_weight = 0
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                std_weight += w
        
        critical, pseudo = [], []
        for n1, n2, e_weight , i in edges: # OUTER LOOP
            # Step 4: ignore current edge index i above
            ignoreUF = UnionFind(n)
            ignoreWeight = 0
            for v1, v2, w, j in edges: # INNER LOOP for IGNORE
                if i != j and ignoreUF.union(v1, v2):
                    ignoreWeight += w
            
            if max(ignoreUF.size) != n or ignoreWeight > std_weight: # either all nodes not conencted or weight breach 
                critical.append(i)
            else: # only if it is not critical, it should may be pseudo
                # Step 5: Force the Inclusion of the current edge i above
                forceUF = UnionFind(n)
                forceUF.union(n1, n2) # Force Union
                forceWeight = e_weight # start with this weight

                for v1, v2, w, j in edges: # INNER LOOP for FORCED INCLUSION
                    if i != j and forceUF.union(v1, v2):
                        forceWeight += w
                
                # if total weight is same as std_Weight, this edge is psuedo-critical
                    # It may not have all the components in included
                if forceWeight == std_weight:
                    pseudo.append(i)
        
        return [critical, pseudo]



        