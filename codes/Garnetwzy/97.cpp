class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.length();
        int n = s2.length();
        if(m + n != s3.length())
            return false;
        vector<vector<bool>> dp(m+1, vector<bool>(n+1, false));
        dp[0][0] = true;
        for(int i = 1; i <= n; i++) {
            dp[0][i] = dp[0][i-1] && (s2[i-1] == s3[i-1]);
        }
        for(int i = 1; i <= m; i++) {
            dp[i][0] = dp[i-1][0] && (s1[i-1] == s3[i-1]);
        }
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                bool ans = false;
                if(s3[i+j-1] == s1[i-1] && !ans) {
                    ans = dp[i-1][j];
                }
                if(s3[i+j-1] == s2[j-1] && !ans) {
                    ans = dp[i][j-1];
                }
                dp[i][j] = ans;
            }
        }
        return dp[m][n];
    }
};