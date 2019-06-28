class Solution {
    public int minPathSum(int[][] grid) {
        if ((grid.length == 0) && (grid[0].length == 0)) return 0;
        int[][] f = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++)
            for (int j = 0; j < grid[0].length; j++) {
                if ((i == 0) && (j == 0)) 
                    f[i][j] = grid[i][j];
                else if (i == 0)
                    f[i][j] = f[i][j-1] + grid[i][j];
                else if (j == 0)
                    f[i][j] = f[i-1][j] + grid[i][j];                
                else
                    f[i][j] = Math.min(f[i-1][j], f[i][j-1]) + grid[i][j];
            }
        return f[grid.length - 1][grid[0].length - 1];
    }
}