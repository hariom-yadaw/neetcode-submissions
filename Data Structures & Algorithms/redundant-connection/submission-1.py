class UnionFindByRank:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        else:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # In graph with n nodes there are n - 1 edges. If there are n edges -
            # - there are n-1 edges which make it connected and non-cyclic
            # - nth edge makes it cyclic  
        n = len(edges)
        uf = UnionFindByRank(n + 1)

        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if uf.find(n1) == uf.find(n2):
                return edge
            uf.union(n1, n2)

        return []

