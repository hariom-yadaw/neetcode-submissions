class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        minHeap = [(grid[0][0], 0, 0)] # Add start point to the minHeap
        visited.add((0, 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)

            if r == rows - 1 and c == cols - 1:
                return t
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (0 <= newR < rows and 0 <= newC < cols and (newR, newC) not in visited):
                    heapq.heappush(minHeap, (max(t, grid[newR][newC]), newR, newC))
                    visited.add((newR, newC))
        
        return -1 # if we can't reach bottom right corner (nevers happens in valid input)