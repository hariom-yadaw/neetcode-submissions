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

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        uf = UnionFindByRank(rows * cols) # initialize with no. of cells

        edges = [] # to store edges b/w two cells (horizontal, vertical)

        for i in range(rows):
            for j in range(cols):
                if i > 0: # for (i, j) add edge to the cell above (i-1, j) (if it exists)
                    edges.append(( i * cols + j, (i-1) * cols + j, abs(heights[i][j] - heights[i-1][j]) ))
                if j > 0: # for (i-1, j) add edge to the cell left (i, j -1) (if it exists)
                    edges.append(( i * cols + j, i * cols + (j - 1), abs(heights[i][j] - heights[i][j - 1]) ))
        
        edges.sort(key=lambda x: x[2])  # Sort the edges by difference in heights

        for cell1, cell2, diff in edges: # edges are connected
            uf.union(cell1, cell2) # union these two cells becuase are connected
            if uf.find(0) == uf.find(rows * cols - 1): # if the source and destinations cells are connected
                return diff
        
        return 0


