class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        countIslands = 0
        #directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == '1'):
                    countIslands += 1 
                    self.visit_is_land_DFS(grid, i, j)
                    
        return countIslands
    
    def visit_is_land_DFS(self, matrix, x, y):
        if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return 
        if matrix[x][y] == '0':
            return 

        matrix[x][y] = '0' # Mark it visited
        
        self.visit_is_land_DFS(matrix, x + 1, y)
        self.visit_is_land_DFS(matrix, x - 1, y)
        self.visit_is_land_DFS(matrix, x, y + 1)
        self.visit_is_land_DFS(matrix, x, y - 1)
