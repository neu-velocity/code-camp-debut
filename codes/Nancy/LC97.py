class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #recursion TLE
        def recursionHelper(s1, s2, i, j, s3, resStr):
            if resStr == s3 and i == len(s1) and j == len(s2):
                return True
            
            option1 = False
            option2 = False
            
            if i < len(s1):
                option1 = recursionHelper(s1, s2, i + 1, j, s3, resStr + s1[i])
            if j < len(s2):
                option2 = recursionHelper(s1, s2, i, j + 1, s3, resStr + s2[j])
            return option1 or option2
        
        return recursionHelper(s1, s2, 0, 0, s3, '')

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        #dp[i][j] represents if the combination of letters:s1[:i+ 1] and s2[:j + 1] can form 
        #the first (i + j) letters
        m = len(s1)
        n = len(s2)
        
        if m + n != len(s3):
            return False
        
        dp = [[None for j in range(n + 1)] for i in range(m + 1)]
        
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])
                

        return dp[m][n]