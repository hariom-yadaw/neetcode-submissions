class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return self.is_land_perimeter_DFS(grid, i, j, visited)
        
        return 0
    
    def is_land_perimeter_DFS(self, matrix, x, y, visited):
        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return 1
        if matrix[x][y] == 0:
            return 1 # if this is retuned as 1, we can't use water for marking visited
        if visited[x][y]:
            return 0 # Already taken care

        visited[x][y] = True # Mark it visisted

        edgeCount = 0 # edgedCount = 1 will be wrong because we have to only count the edges
            # - this might be an land in the middle of lands, no water boundary
        edgeCount += self.is_land_perimeter_DFS(matrix, x + 1, y, visited)
        edgeCount += self.is_land_perimeter_DFS(matrix, x - 1, y, visited)
        edgeCount += self.is_land_perimeter_DFS(matrix, x, y + 1, visited)
        edgeCount += self.is_land_perimeter_DFS(matrix, x, y - 1, visited)

        return edgeCount