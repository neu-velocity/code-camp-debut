class Solution {
    public int uniquePaths(int m, int n) {
        int[][] path = new int[m][n];
        for(int col=0;col<n;col++){
            path[0][col] = 1;
        }
        for(int row=0;row<m;row++){
            path[row][0] = 1;
        }
        for(int row=1;row<m;row++){
            for(int col=1;col<n;col++){
                path[row][col] = path[row][col-1]+path[row-1][col];
            }
        }
        return path[m-1][n-1];
    }
}