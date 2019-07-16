class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        if(m == 0)
            return 0;
        int n  = obstacleGrid[0].size();
        if(obstacleGrid[0][0] == 1)
            return 0;
        vector<vector<long>> dp(m, vector<long>(n, 0));
        dp[0][0] = 1;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i == 0 && j == 0)
                    continue;
                if(obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                    continue;
                }
                int first = -1;
                int second = -1;
                if(j > 0 && obstacleGrid[i][j-1] != 1) {
                    first = dp[i][j-1];
                }
                if(i > 0 && obstacleGrid[i-1][j] != 1) {
                    second = dp[i-1][j];
                }
                dp[i][j] = (long)max(first, 0) + (long)max(second, 0);
            }
        }
        return dp[m-1][n-1];
    }
};