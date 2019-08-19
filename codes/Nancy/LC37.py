class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #record box position that needs to be filled in
        puzzles = []
        
        #create a list of numbers can be chosen for each row, col, and cell
        nums = set(str(i) for i in range(1,10))
        rowNums = [nums.copy() for x in range(9)]
        colNums = [nums.copy() for x in range(9)]
        cellNums = [nums.copy() for x in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    puzzles.append((i,j))
                else:
                    rowNums[i].remove(board[i][j])
                    colNums[j].remove(board[i][j])
                    cellNums[3*(i//3) + j//3].remove(board[i][j])
        
        
        
        def backtracking(puzzles, n, rowNums, colNums, cellNums):
            if n == len(puzzles):
                return True
            i,j = puzzles[n]
            solns = rowNums[i] & colNums[j] & cellNums[3*(i//3) + (j//3)]
   
            if len(solns) == 0:
                return False
            
            tmp = board[i][j]
            for sol in solns:
                rowNums[i].remove(sol)
                colNums[j].remove(sol)
                cellNums[3*(i//3) + (j//3)].remove(sol)
                board[i][j] = sol
                if backtracking(puzzles, n + 1, rowNums, colNums, cellNums):
                    return True
                rowNums[i].add(sol)
                colNums[j].add(sol)
                cellNums[3*(i//3) + (j//3)].add(sol)
                board[i][j] = tmp
            
            # return False
            
        backtracking(puzzles, 0, rowNums, colNums, cellNums)
            
                
                    
        