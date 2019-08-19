class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #TLE recursion
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        def recur(w1, w2, i, j):
            if len(w1) == i:
                return len(w2) - j
            if len(w2) == j:
                return len(w1) - i
            
            res = 0
            if w1[i] == w2[j]:
                res = recur(w1, w2, i + 1, j + 1)
            else:
                delete = recur(w1, w2, i + 1, j)
                replace = recur(w1, w2, i + 1, j + 1)
                insert = recur(w1, w2, i, j + 1) #insert a letter at w1[i], hoping w1[i + 1] can match w2[j + 1], but we are not actually inserting a letter here, so the the letter at w1[i] before insertion still stays at index i, therefore we only move j
                res = min(delete, replace, insert) + 1
            return res
        
        return recur(word1, word2, 0, 0)

    #DP
    def minDistance2(self, word1: str, word2: str) -> int:
        m = len(word2)
        n = len(word1)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
        #construct base case
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + 1
        
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[j - 1] != word2[i - 1]:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                    # + 1 is the operation you do in current cell:del/insert/replace
                    #dp[i][j - 1] is how many operations you need to do before deleting the current cell
                    #dp[i- 1][j - 1] is how many operations you need to do before replacing the current cell with word2[i - 1]
                    #dp[i - 1][j] is how many operations you need to do before inserting word2[i - 1] at the current cell. INSERTION: change dp[i-1][j] aka word1[i - 1] to word2[j - 2], then insert word2[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] #don't need to do any operation
        return dp[m][n]