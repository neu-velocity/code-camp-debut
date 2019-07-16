class Solution {
    public int minPathSum(int[][] grid) {
        int rows = grid.length;
        int cols=  grid[0].length;
        int[][] costs = new int[rows][cols];
        costs[0][0] = grid[0][0];
        for(int i=1;i<rows;i++){
            costs[i][0] = costs[i-1][0]+grid[i][0];
        }
        for(int i=1;i<cols;i++){
            costs[0][i] = costs[0][i-1]+grid[0][i];
        }
        for(int row=1;row<rows;row++){
            for(int col=1;col<cols;col++){
                costs[row][col] = Math.min(costs[row-1][col],costs[row][col-1])+grid[row][col];
            }
        }
        return costs[rows-1][cols-1];
    }
}