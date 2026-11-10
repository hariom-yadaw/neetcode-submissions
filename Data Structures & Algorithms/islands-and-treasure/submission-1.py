from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque() # to hold the co-ordinates of cells with 0s

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))


        # Directions to move in the matrix
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                newR, newC = r + dr, c + dc

                if ( 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] > 0 and grid[newR][newC] > grid[r][c] + 1):
                    grid[newR][newC] = grid[r][c] + 1
                    queue.append((newR, newC))
        
        #return grid

