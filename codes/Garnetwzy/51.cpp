class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ret;
        vector<string> cur(n, string(n, '.'));
        dfs(ret, cur, 0);
        return ret;
    }
    
    void dfs(vector<vector<string>>& ret, vector<string>& cur, int row) {
        if(row == cur.size()) {
            ret.push_back(cur);
            return;
        }
        int n = cur.size();
        for(int i = 0; i < n; i++) {
            if(isValid(cur, row, i)) {
                cur[row][i] = 'Q';
                dfs(ret, cur, row+1);
                cur[row][i] = '.';
            }
            
        }
    }
    
    bool isValid(vector<string>& cur, int row, int colomn) {
        // check colomn
        for(int i = 0; i < row; i++) {
            if(cur[i][colomn] != '.')
                return false;
        }
        // check / direct
        for(int i = row - 1, j = colomn+1; i >= 0 && j < cur.size(); i--, j++) {
            if(cur[i][j] != '.')
                return false;
        }
        // check \ direct
        for(int i = row - 1, j = colomn-1; i >= 0 && j >= 0; j--, i--) {
            if(cur[i][j] != '.')
                return false;
        }
        return true;
    }
};