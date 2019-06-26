class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        if(m == 0)
            return 0;
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[0][0] = grid[0][0];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i == 0 && j == 0)
                    continue;
                int first = INT_MAX;
                int second = INT_MAX;
                if(i > 0) {
                    first = dp[i-1][j];
                }
                if(j > 0) {
                    second = dp[i][j-1];
                }
                dp[i][j] = min(first, second) + grid[i][j];
            }
        }
        return dp[m-1][n-1];
    }
};