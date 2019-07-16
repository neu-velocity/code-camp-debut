class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid == null
                || obstacleGrid.length == 0
                || obstacleGrid[0] == null
                || obstacleGrid[0].length == 0
                || obstacleGrid[0][0] == 1
                || obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1] == 1
        ) {
            return 0;
        }

        int R = obstacleGrid.length, C = obstacleGrid[0].length;
        int[][] dp = new int[R][C];
        dp[0][0] = 1;
        for (int c = 1; c < C; c++) {
            if (obstacleGrid[0][c] == 0) {
                dp[0][c] = 1;
            } else {
                break;
            }
        }
        for (int r = 1; r < R; r++) {
            if (obstacleGrid[r][0] == 0) {
                dp[r][0] = dp[r - 1][0];
            }
            for (int c = 1; c < C; c++) {
                if (obstacleGrid[r][c] == 0) {
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1];
                }
            }
        }
        return dp[R - 1][C - 1];
    }
}