class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    currentArea = self.calculateArea_DFS(grid, i, j)
                    maxArea = max(currentArea, maxArea)
        
        return maxArea

    def calculateArea_DFS(self, matrix, x, y):
        if(x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return 0
        if matrix[x][y] == 0:
            return 0
        
        matrix[x][y] = 0 # Mark the cell as visited by making it a water cell

        area = 1

        #Explore neighboring cells
        area += self.calculateArea_DFS(matrix, x + 1, y)
        area += self.calculateArea_DFS(matrix, x - 1, y)
        area += self.calculateArea_DFS(matrix, x, y + 1)
        area += self.calculateArea_DFS(matrix, x, y - 1)
        return area
