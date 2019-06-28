class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(), n = word2.length();
        vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
        for(int i = 1; i <= n; i++) {
            dp[0][i] = i;
        }
        for(int i = 1; i <= m; i++) {
            dp[i][0] = i;
        }
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                int val = INT_MAX;
                int offset = 1;
                if(word1[i-1] == word2[j-1]) {
                    offset = 0;
                }
                val = min(val, dp[i-1][j] + 1);
                val = min(val, dp[i][j-1] + 1);
                val = min(val, dp[i-1][j-1] + offset);
                dp[i][j] = val;
            }
        }
        return dp[m][n];
    }
};