class Solution {
    public int minPathSum(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0] == null || grid[0].length == 0) {
            return 0;
        }
        int R = grid.length, C = grid[0].length;
        int[][] dp = new int[R][C];
        dp[0][0] = grid[0][0];
        for (int r = 0, c = 1; c < C; c++) {
            dp[r][c] = grid[r][c] + dp[r][c - 1];
        }
        for (int r = 1; r < R; r++) {
            dp[r][0] = grid[r][0] + dp[r - 1][0];
            for (int c = 1; c < C; c++) {
                dp[r][c] = grid[r][c] + Math.min(dp[r - 1][c], dp[r][c - 1]);
            }
        }
        return dp[R - 1][C - 1];
    }
}