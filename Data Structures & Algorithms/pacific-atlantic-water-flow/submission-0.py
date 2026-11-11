class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        #create matrix for pacific, mark them True if watre can flow from cell to  pacific ocean 
        pacific = [[False] * COLS for _ in range(ROWS)]
        atlantic = [[False] * COLS for _ in range(ROWS)] # same for atlntic ocean

        for i in range(ROWS):
            self.dfs(heights, i, 0, pacific, float('-inf'))
            self.dfs(heights, i, COLS - 1, atlantic, float('-inf'))
        
        for j in range(COLS):
            self.dfs(heights, 0, j, pacific, float('-inf'))
            self.dfs(heights, ROWS -1, j, atlantic, float('-inf'))
        
        result = []

        for i in range(ROWS):
            for j in range(COLS):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        
        return result
    
    def dfs(self, grid, x, y, visited, height):
        if( x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return
        
        if visited[x][y]:
            return
        
        if height > grid[x][y]:
            return # if height of this cell at (x, y) is more than previous cell height 
        
        visited[x][y] = True

        self.dfs(grid, x + 1, y, visited, grid[x][y])
        self.dfs(grid, x - 1, y, visited, grid[x][y])
        self.dfs(grid, x, y + 1, visited, grid[x][y])
        self.dfs(grid, x, y - 1, visited, grid[x][y])

