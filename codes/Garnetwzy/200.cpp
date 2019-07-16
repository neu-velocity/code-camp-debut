class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int row = grid.size();
        if(row == 0)
            return 0;
        int colomn = grid[0].size();
        vector<vector<bool>> visit(row, vector<bool>(colomn, false));
        int sum = 0;
        for(int i = 0; i < row; i++) {
            for(int j = 0; j < colomn; j++) {
                if(dfs(grid, i, j, visit)){
                    sum++;
                }
            }
        }
        return sum;
    }
    
    bool dfs(vector<vector<char>>& grid, int row, int colomn, vector<vector<bool>>& visit) {
        if(row < 0 || row >= grid.size() || colomn < 0 || colomn >= grid[0].size() 
           || grid[row][colomn] == '0' || visit[row][colomn]) {
            return false;
        }
        visit[row][colomn] = true;
        dfs(grid, row+1, colomn, visit);
        dfs(grid, row-1, colomn, visit);
        dfs(grid, row, colomn+1, visit);
        dfs(grid, row, colomn-1, visit);
        return true;
    }
    
};