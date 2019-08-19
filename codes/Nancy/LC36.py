class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        n = len(board)
        rowFlag = [[False for x in range(n)] for y in range(n)]
        colFlag = [[False for x in range(n)] for y in range(n)]
        cellFlag = [[False for x in range(n)] for y in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] >= '1' and board[i][j] <= '9':
                    num = int(board[i][j]) - 1
                    #print([i,j],num)
                    #print(rowFlag[i][num], colFlag[j][num],cellFlag[3 * (i // 3) + (j // 3)][num])
                    if rowFlag[i][num] or colFlag[j][num] or cellFlag[3 * (i // 3) + (j //3)][num]:
                        return False
                    
                    rowFlag[i][num] = True
                    colFlag[j][num] = True
                    cellFlag[3 * (i // 3) + (j // 3)][num] = True
                    
        return True