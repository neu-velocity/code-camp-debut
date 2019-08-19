class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for i in range(n)] for i in range(m)]#record how many ways we can reach position [i][j] from the start
        for i in range(m):
            memo[i][0] = 1
        for j in range(n):
            memo[0][j] = 1
        
        #print(memo)

        for i in range(1, m): #because when i = 0, there's only one way to reach those boxes on i = 0, which is moving from the left of start. Therefore we start at i = 1
            for j in range(1, n):#same theory for the left edge, only moving down from the start can reach them
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1] #current position = position above + position from the left
        #print(memo)
        return memo[m - 1][n - 1]