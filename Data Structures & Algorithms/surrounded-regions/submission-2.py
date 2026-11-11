class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # call DFS for all cells with 0 at the left and right border 
            # - Mark all those '0's wth 'T's temporarily
        for i in range(ROWS):
            if board[i][0] == 'O':
                self.DFS(board, i, 0)
            if board[i][COLS - 1] == 'O':
                self.DFS(board, i, COLS - 1)

        # call DFS for all cells with 0 at the upper and lower border
            # - Mark all those '0's with 'T's temporarily
        for j in range(COLS):
            if board[0][j] == 'O':
                self.DFS(board, 0, j)
            if board[ROWS - 1][j] == 'O':
                self.DFS(board, ROWS - 1, j)

        # Mark all the remaining '0's with X because they are surrounded by water
            # - Also revert back temporarily marked 'T's with 'O's
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O' 
    
    def DFS(self, matrix, x, y):
        if( x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
            return
        if matrix[x][y] != 'O':
            return
        
        matrix[x][y] = 'T'
        
        for dx, dy in self.DIRECTIONS:
            self.DFS(matrix, x + dx, y + dy)
