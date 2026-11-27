"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # for DFS,
            # n => lengh of quadrant
            # r, c => first cell index (0,0) in that quadrant
        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        allSame = False
                        break
            
            if allSame: # return a leaf node, val same as grid cells
                return Node(grid[r][c], True) # all 4 childern wiil ne null automaically by Node class constructor
            
            # if values in quadrant are different, its not a leaf node => find all 4 children
            n = n // 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            # if not a leaf node, any val will work
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)


        # Call DFS with starting cell
        dimension = len(grid) # its a square grid of n*n
        return dfs(dimension, 0, 0) # starting (r,c) = (0, 0) 