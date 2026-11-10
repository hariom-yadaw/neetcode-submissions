from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        countIslands = 0

        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == '1'):
                    countIslands += 1 
                    self.visit_is_land_DFS(grid, i, j)
                    #self.visit_is_land_BFS(grid, i, j)
                    
        return countIslands
    
    def visit_is_land_BFS(self, matrix, x , y):
        queue = deque()
        queue.append((x, y))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in direcions:
                newRow, newCol = row + dr, col + dc

                if (0 <= newRow < len(matrix) or 0 <= newCol < len(matrix[0]) or matrix[newRow][newCol == 1]):
                    queue.append((newRow, newCol))
                    matrix[newRow][newCol] == 0 # Mark the cell as visited by making it a water cell

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
