class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        if (m == 0) return 0;
        int n = obstacleGrid[0].length;
        if (n == 0) return 0;        
        int[][] f = new int[m + 1][n + 1];
        f[1][1] = 1;
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <= n; j++)
                if (obstacleGrid[i - 1][j - 1] == 1)
                    f[i][j] = 0;
                else if (!((i == 1) && (j == 1)))
                    f[i][j] = f[i-1][j] + f[i][j-1];
        return f[m][n];        
    }
}