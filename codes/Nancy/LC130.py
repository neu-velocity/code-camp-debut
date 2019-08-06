class Solution:
    """
    recursion to modify boarder O and its neighbours to $
    """
    def helper(self, board, x, y):
        if board[x][y] == 'O':
            board[x][y] = '$'
            
            #checking neighbours
            if x < len(board) - 1 and board[x + 1][y] == 'O':
                self.helper(board, x + 1, y)
            if x  > 0 and board[x - 1][y] == 'O':
                self.helper(board, x - 1, y )
            if y < len(board[x]) - 1 and board[x][y + 1] == 'O':
                self.helper(board, x, y + 1)
            if y > 0 and board[x][y - 1] == 'O':
                self.helper(board, x, y - 1)
            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #start with boarder, run helper to modify appropriate O to $
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[i]) - 1) and board[i][j] == 'O':
                    self.helper(board, i, j)
        
        #run through board
        for i in range(len(board)):
            for j in range(len(board[i])):
                #flip O to X
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                #flip $ to O
                if board[i][j] == '$':
                    board[i][j] = 'O'
        
        return board
        