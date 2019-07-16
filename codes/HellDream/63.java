class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int rows = obstacleGrid.length;
        int cols = obstacleGrid[0].length;
        int[][] paths = new int[rows][cols];
        for(int col=0;col<cols;col++){
            if(obstacleGrid[0][col]==1) break;
            paths[0][col] = 1;
        }
        for(int row=0;row<rows;row++){
            if(obstacleGrid[row][0]==1) break;
            paths[row][0] = 1;
        }
        
        for(int row=1;row<rows;row++){
            for(int col=1;col<cols;col++){
                if(obstacleGrid[row][col]==1){
                    paths[row][col] = 0;
                }else{
                    paths[row][col] = paths[row-1][col]+paths[row][col-1];
                }
            }
        }
        return paths[rows-1][cols-1];
    }
}