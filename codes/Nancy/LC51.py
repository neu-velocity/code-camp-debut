class Solution:
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        rowIndicator = [True for i in range(n)]
        colIndicator = [True for i in range(n)]
        diagDict = {}
        res = set()#record the position that can be filled with Queen
        ans = [] #final answer
        #print(res)
        
        #construct diagDict
        for j in range(n):
            row = 0
            hill = row + j
            dale = row - j
            key1 = ('hill', hill)
            key2 = ('dale', dale)
            diagDict[key1] = True
            diagDict[key2] = True
        
        for i in range(1, n):
            col = 0
            dale = i - col
            key = ('dale', dale)
            diagDict[key] = True
        
        for j in range(1, n):
            row = n - 1
            hill = row + j
            key = ('hill', hill)
            diagDict[key] = True
        
        def backtracking(i = 0):
            if i == n:
                solution = []
                for row, col in sorted(res):
                    solution.append('.' * col + 'Q' + '.' * (n - 1 - col))
                ans.append(solution)
                return

            for j in range(n):

                if rowIndicator[i] and colIndicator[j] and diagDict[('hill', i + j)] and diagDict[('dale', i - j)]:       
                    position = (i, j)
                    rowIndicator[i] = False
                    colIndicator[j] = False
                    diagDict[('hill', i + j)] = False
                    diagDict[('dale', i - j)] = False
                    res.add(position)
            
                    backtracking(i + 1)
                    
                    res.remove(position)
                    rowIndicator[i] = True
                    colIndicator[j] = True
                    diagDict[('hill', i + j)] = True
                    diagDict[('dale', i - j)] = True
            
                else:
                    continue
            return
        
        backtracking()
        return ans