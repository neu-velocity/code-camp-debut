class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(t)
        n = len(s)
        
        if n == 0:
            return 0
        if m == 0:
            return 1
        
        dp = [[0 for i in range(n + 1)]for j in range(m + 1)] 
        
        for j in range(n + 1):
            dp[0][j] = 1
        #dp[i][j] represents the number of subsequence of s[:j] equals to t[:i]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[j - 1] == t[i - 1]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] #why don't we add dp[i - 1][j], b/c we wanted to find the the subsequence of s that matches t
                else:
                    dp[i][j] = dp[i][j - 1]
        
        return dp[m][n]