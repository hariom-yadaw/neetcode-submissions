from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        queue = deque()
        visited = [[False] * COLS for _ in range(ROWS)]
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited[i][j] = True
        
        minutesElapsed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # queue might hold last items but fresh already > 0, hence fresh > 0 with and condition
        while queue and fresh > 0:
            levelSize = len(queue)

            for _ in range(levelSize):
                r, c = queue.popleft()

                for dr, dc in directions:
                    newR, newC = r + dr, c + dc

                    if (0 <= newR < ROWS and 0 <= newC < COLS and not visited[newR][newC] and grid[newR][newC] == 1):
                        queue.append((newR, newC))
                        visited[newR][newC] = True # grid[newR][newC] = 2
                        fresh -= 1 # Fresh gets decremented as soon as its appended
            
            minutesElapsed += 1
        
        return minutesElapsed if fresh == 0 else -1

                    
        